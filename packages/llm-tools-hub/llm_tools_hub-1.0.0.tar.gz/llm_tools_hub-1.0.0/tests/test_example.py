import unittest
from llm_tools_hub import ToolRegistry, action, run_llm_conversation
from typing import Annotated

@action(toolname="calculate_sum", requires=["math"])
def calculate_sum(
    a: Annotated[int, "First number"],
    b: Annotated[int, "Second number"]
) -> int:
    return a + b

@action(toolname="get_exchange_rate", requires=[])
def get_exchange_rate(
    base_currency: Annotated[str, "Base currency. e.g. USD"],
    target_currency: Annotated[str, "Target currency. e.g. JPY"],
    date: Annotated[str, "Date in YYYY-MM-DD format"] = "latest"
) -> float:
    # For testing, return a dummy value
    return 123.45

class TestToolRegistry(unittest.TestCase):
    def test_calculate_sum(self):
        tools = ToolRegistry()
        tools.register_tool(calculate_sum)
        result = tools.call_tool("calculate_sum", {"a": 50, "b": 75})
        self.assertEqual(result, "125")

    def test_get_exchange_rate(self):
        tools = ToolRegistry()
        tools.register_tool(get_exchange_rate)
        result = tools.call_tool("get_exchange_rate", {"base_currency": "USD", "target_currency": "JPY"})
        self.assertEqual(result, "123.45")

if __name__ == '__main__':
    unittest.main()