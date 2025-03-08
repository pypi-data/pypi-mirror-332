"""
Router for tool-related endpoints.
"""

import logging
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Import tools registry
from tools.registry import get_available_tools

logger = logging.getLogger(__name__)

router = APIRouter()


class ToolSchema(BaseModel):
    """Model for tool schema."""

    name: str
    description: str
    parameters: Dict[str, Any]
    required_parameters: List[str]


@router.get("/")
async def list_tools():
    """List all available tools."""
    try:
        tools = get_available_tools()
        return {"tools": tools}
    except Exception as e:
        logger.error(f"Error listing tools: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{tool_name}/schema")
async def get_tool_schema(tool_name: str):
    """Get the schema for a specific tool."""
    try:
        tools = get_available_tools()

        # Find the tool with the given name
        tool = next((t for t in tools if t["name"] == tool_name), None)

        if not tool:
            raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")

        return tool
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        logger.error(f"Error getting tool schema: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/{tool_name}/execute")
async def execute_tool(tool_name: str, parameters: Dict[str, Any]):
    """Execute a tool with the given parameters."""
    try:
        # This would need to be implemented in the tools registry
        # For now, return a placeholder
        return {
            "status": "ok",
            "tool": tool_name,
            "result": f"Executed {tool_name} with parameters: {parameters}",
        }
    except Exception as e:
        logger.error(f"Error executing tool: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
