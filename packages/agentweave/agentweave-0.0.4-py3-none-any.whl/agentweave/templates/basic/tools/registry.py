"""
Tool registry for {{ project_name }}.

This module provides a central registry for all tools available to the agent.
"""

import importlib
import inspect
import logging
import os
import pkgutil
from typing import Any, Dict, List, Optional, Type

from langchain_core.tools import BaseTool

logger = logging.getLogger(__name__)

# Global registry of available tools
_tools = {}


def register_tool(tool_class: Type[BaseTool]) -> Type[BaseTool]:
    """
    Register a tool class in the global registry.

    This function can be used as a decorator or called directly.
    """
    # Handle tool name access correctly
    if hasattr(tool_class, "name"):
        if isinstance(tool_class.name, property):
            # If name is a property, try to get its value from a dummy instance
            try:
                dummy = tool_class()
                tool_name = dummy.name
            except Exception:
                tool_name = tool_class.__name__
        else:
            tool_name = tool_class.name
    else:
        tool_name = tool_class.__name__

    _tools[tool_name] = tool_class
    logger.info(f"Registered tool: {tool_name}")
    return tool_class


def get_available_tools() -> List[BaseTool]:
    """
    Get a list of all available tool instances.

    Returns:
        A list of instantiated tool objects
    """
    # Load all tools from the tools directory
    _load_tools()

    if not _tools:
        logger.warning("No tools were loaded from the tools directory")

    # Create instances of all registered tools
    tools = []
    for name, tool_class in _tools.items():
        try:
            tool_instance = tool_class()
            tools.append(tool_instance)
            logger.info(f"Instantiated tool: {name}")
        except Exception as e:
            logger.error(f"Error instantiating tool {name}: {str(e)}")

    logger.info(f"Total tools available: {len(tools)}")
    return tools


def get_tools_schema() -> List[Dict[str, Any]]:
    """
    Get a list of all registered tools with their schemas.
    """
    # Load all tools from the tools directory
    _load_tools()

    tools_list = []
    for name, tool_class in _tools.items():
        try:
            # Create an instance to get the schema
            tool_instance = tool_class()

            # Make sure required attributes exist
            if not hasattr(tool_instance, "name") or not tool_instance.name:
                logger.warning(f"Tool {name} missing name attribute, skipping")
                continue

            if not hasattr(tool_instance, "description"):
                logger.warning(f"Tool {name} missing description, using class name")
                description = tool_class.__name__
            else:
                description = tool_instance.description

            # Extract parameters schema
            if hasattr(tool_instance, "args_schema") and tool_instance.args_schema:
                try:
                    parameters = tool_instance.args_schema.schema()
                    required_parameters = parameters.get("required", [])
                except Exception as e:
                    logger.warning(f"Could not extract schema for {name}: {e}")
                    parameters = {}
                    required_parameters = []
            else:
                parameters = {}
                required_parameters = []

            # Extract tool schema
            schema = {
                "name": tool_instance.name,
                "description": description,
                "parameters": parameters,
                "required_parameters": required_parameters,
            }

            tools_list.append(schema)
        except Exception as e:
            logger.error(f"Error loading tool {name}: {str(e)}")

    logger.info(f"Available tools: {[t['name'] for t in tools_list]}")
    return tools_list


def get_tool_by_name(
    name: str, config: Optional[Dict[str, Any]] = None
) -> Optional[BaseTool]:
    """
    Get a tool instance by name with optional configuration.
    """
    # Load all tools from the tools directory
    _load_tools()

    if name not in _tools:
        logger.warning(
            f"Tool {name} not found in registry. Available tools: {list(_tools.keys())}"
        )
        return None

    try:
        # Create the tool instance
        tool_class = _tools[name]

        if config:
            # Initialize with config
            return tool_class(**config)
        else:
            # Initialize with defaults
            return tool_class()
    except Exception as e:
        logger.error(f"Error creating tool {name}: {str(e)}")
        return None


def _load_tools():
    """
    Load all tool modules from the tools directory.
    """
    if _tools:
        # Already loaded
        logger.debug(f"Tools already loaded: {list(_tools.keys())}")
        return

    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logger.info(f"Loading tools from directory: {current_dir}")

    # Import all modules in the tools directory
    modules_found = list(pkgutil.iter_modules([current_dir]))
    logger.info(f"Found modules: {[name for _, name, _ in modules_found]}")

    for _, name, is_pkg in modules_found:
        if name != "registry" and not name.startswith("_"):
            try:
                logger.info(f"Attempting to import module: tools.{name}")
                module = importlib.import_module(f"tools.{name}")

                # Find all tool classes in the module
                tool_classes_found = []
                for attr_name, attr_value in module.__dict__.items():
                    if (
                        inspect.isclass(attr_value)
                        and issubclass(attr_value, BaseTool)
                        and attr_value != BaseTool
                    ):
                        # Register the tool
                        register_tool(attr_value)
                        tool_classes_found.append(attr_name)

                if tool_classes_found:
                    logger.info(
                        f"Registered tool classes from {name}: {tool_classes_found}"
                    )
                else:
                    logger.warning(f"No tool classes found in module {name}")

            except Exception as e:
                logger.error(f"Error loading tool module {name}: {str(e)}")
                # Print the full traceback for debugging
                import traceback

                logger.error(traceback.format_exc())

    logger.info(f"Finished loading tools. Available tools: {list(_tools.keys())}")


# Try to load tools on module import
_load_tools()
