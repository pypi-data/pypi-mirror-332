import unittest
from llm_tools_hub import ToolRegistry, action
from typing import Annotated

@action(toolname="calculate_sum", requires=["math"])
def calculate_sum(
    a: Annotated[int, "First number"],
    b: Annotated[int, "Second number"]
) -> int:
    return a + b

class TestToolRegistry(unittest.TestCase):
    def test_calculate_sum(self):
        tools = ToolRegistry()
        tools.register_tools([calculate_sum])
        result = tools.call_tool("calculate_sum", {"a": 50, "b": 75})
        self.assertEqual(result, "125")

if __name__ == '__main__':
    unittest.main()