import openai
import json
import inspect
from typing import Any, Callable, Dict, List, get_type_hints, Annotated

# Helper functions for schema generation

def _python_type_to_json_type(py_type: Any) -> str:
    origin = getattr(py_type, '__origin__', None)
    if origin is not None and origin is Annotated:
        args = getattr(py_type, '__args__', [])
        if args:
            py_type = args[0]
    if py_type in [int, float]:
        return "number"
    elif py_type == bool:
        return "boolean"
    elif py_type == str:
        return "string"
    else:
        return "string"

def _extract_annotation_description(py_type: Any) -> str:
    origin = getattr(py_type, '__origin__', None)
    if origin is Annotated:
        args = getattr(py_type, '__args__', [])
        if len(args) > 1 and isinstance(args[1], str):
            return args[1]
    return ""

def _build_openai_parameters_schema(func: Callable) -> Dict[str, Any]:
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)
    properties = {}
    required_fields = []
    for param_name, param in sig.parameters.items():
        param_type = type_hints.get(param_name, str)
        json_type = _python_type_to_json_type(param_type)
        param_desc = _extract_annotation_description(param_type)
        if not param_desc:
            param_desc = f"Parameter '{param_name}' of type {json_type}."
        properties[param_name] = {
            "type": json_type,
            "description": param_desc
        }
        if param.default is inspect.Parameter.empty:
            required_fields.append(param_name)
    return {
        "type": "object",
        "properties": properties,
        "required": required_fields
    }

def _extract_function_description(func: Callable) -> str:
    doc = func.__doc__ or ""
    return doc.strip() if doc else "No description provided."

# Decorator to register a tool

def action(toolname: str = None, requires: List[str] = []):
    def decorator(func: Callable):
        name = toolname or func.__name__
        func._tool_name = name
        func._tool_requires = requires
        parameters_schema = _build_openai_parameters_schema(func)
        description = _extract_function_description(func)
        func._openai_name = name
        func._openai_description = description
        func._openai_parameters = parameters_schema
        return func
    return decorator

# Main class that manages the tools

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register_tool(self, func: Callable):
        name = getattr(func, "_openai_name", func.__name__)
        self._tools[name] = func

    def get_openai_functions(self) -> List[Dict[str, Any]]:
        functions = []
        for name, func in self._tools.items():
            functions.append({
                "name": func._openai_name,
                "description": func._openai_description,
                "parameters": func._openai_parameters
            })
        return functions

    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        func = self._tools.get(tool_name)
        if not func:
            return f"Error: function '{tool_name}' not found."
        try:
            result = func(**arguments)
            return str(result)
        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

# Function to run the conversation with the LLM

def run_llm_conversation(
    registry: ToolRegistry,
    messages: List[Dict[str, Any]],
    model: str = "gpt-3.5-turbo-0613"
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        functions=registry.get_openai_functions(),
        function_call="auto",
    )
    msg = response["choices"][0]["message"]

    tool_calls = []
    if "tool_calls" in msg and msg["tool_calls"]:
        tool_calls = msg["tool_calls"]
    elif "function_call" in msg and msg["function_call"]:
        tool_calls = [{
            "name": msg["function_call"]["name"],
            "arguments": msg["function_call"]["arguments"]
        }]

    if not tool_calls:
        print("Model response:", msg.get("content", ""))
        return

    tool_messages = []
    for tc in tool_calls:
        name = tc["name"]
        args_str = tc["arguments"]
        try:
            parsed_args = json.loads(args_str) if args_str else {}
        except Exception:
            parsed_args = {}
        result_str = registry.call_tool(name, parsed_args)
        tool_messages.append({
            "role": "function",
            "name": name,
            "content": result_str
        })

    messages.append(msg)
    messages.extend(tool_messages)

    second_response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    final_msg = second_response["choices"][0]["message"]
    print("Final model response:", final_msg.get("content", ""))