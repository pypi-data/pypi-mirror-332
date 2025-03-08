"""
Calculator tool for performing mathematical calculations.
"""

import logging
import math
from typing import Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from .registry import register_tool

logger = logging.getLogger(__name__)


class CalculatorInput(BaseModel):
    """Input schema for the calculator tool."""

    expression: str = Field(
        description="The mathematical expression to evaluate.",
    )


@register_tool
class CalculatorTool(BaseTool):
    """Tool for performing mathematical calculations."""

    name: str = "calculator"
    description: str = "A calculator tool for evaluating mathematical expressions. Input should be a mathematical expression to evaluate."
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            # Create a safe dictionary of allowed functions
            safe_dict = {
                "abs": abs,
                "round": round,
                "min": min,
                "max": max,
                "sum": sum,
                "pow": pow,
                "int": int,
                "float": float,
            }

            # Add safe math functions
            for name in dir(math):
                if not name.startswith("_"):
                    safe_dict[name] = getattr(math, name)

            # Evaluate the expression in the safe environment
            # Warning: eval is inherently unsafe, but we're limiting available functions
            result = eval(expression, {"__builtins__": {}}, safe_dict)

            return str(result)
        except Exception as e:
            logger.error(f"Error evaluating expression '{expression}': {str(e)}")
            return f"Error: {str(e)}"


# Example of using the tool
if __name__ == "__main__":
    calculator = CalculatorTool()
    result = calculator.invoke({"expression": "2 + 2 * 3"})
    print(f"2 + 2 * 3 = {result}")
