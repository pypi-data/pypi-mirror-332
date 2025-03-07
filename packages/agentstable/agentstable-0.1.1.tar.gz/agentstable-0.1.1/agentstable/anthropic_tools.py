"""
Tools module for converting agents.json schemas to Anthropic-compatible tools.
"""

from typing import Any, Dict, List, Optional, Union, cast
import json


def get_anthropic_tools(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Convert an agents.json schema into Anthropic tools format.

    Args:
        response: The response from the search action service containing the agents.json schema

    Returns:
        A list of tools in Anthropic format
    """
    if not response or "schema" not in response or "flow_id" not in response:
        raise ValueError("Invalid response format: missing schema or flow_id")

    schema = response["schema"]
    flow_id = response["flow_id"]

    # Find the specific flow in the schema
    flow = None
    for f in schema.get("flows", []):
        if f.get("id") == flow_id:
            flow = f
            break

    if not flow:
        raise ValueError(f"Flow with ID '{flow_id}' not found in schema")

    # Convert the flow to an Anthropic tool
    tool = {
        "name": flow_id,
        "description": flow.get("description", f"Execute the {flow_id} flow"),
        "input_schema": _convert_anthropic_parameters(flow)
    }

    return [tool]


def _convert_anthropic_parameters(flow: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert flow parameters to Anthropic tool parameters format.

    Args:
        flow: The flow definition from the agents.json schema

    Returns:
        Anthropic-compatible parameters schema
    """
    # Start with basic JSON schema structure
    schema = {
        "type": "object",
        "properties": {},
        "required": []
    }

    # Get parameters from the flow
    parameters = flow.get("fields", {}).get("parameters", [])
    
    for param in parameters:
        param_name = param.get("name")
        if not param_name:
            continue

        # Add the property
        schema["properties"][param_name] = {
            "type": param.get("type", "string"),
            "description": param.get("description", f"Parameter {param_name}")
        }

        # Add enum values if available
        if param.get("enum"):
            schema["properties"][param_name]["enum"] = param.get("enum")

        # Add to required list if needed
        if param.get("required", False):
            schema["required"].append(param_name)

    return schema


def extract_anthropic_tool_calls(message: Any) -> List[Dict[str, Any]]:
    """
    Extract tool calls from an Anthropic message.

    Args:
        message: The message from Anthropic API containing tool use

    Returns:
        A list of extracted tool calls
    """
    tool_calls = []
    
    try:
        # Handle both raw dictionary and Anthropic Message object
        content = None
        
        # Check if it's an Anthropic Message object with content attribute
        if hasattr(message, "content"):
            content = message.content
        # Check if it's a dictionary with a 'content' key
        elif isinstance(message, dict) and "content" in message:
            content = message["content"]
        else:
            return []
            
        # Process the content
        for block in content:
            if hasattr(block, "type") and block.type == "tool_use":
                tool_calls.append({
                    "id": block.id,
                    "name": block.name,
                    "arguments": block.input
                })
            elif isinstance(block, dict) and block.get("type") == "tool_use":
                tool_use = block.get("tool_use", {})
                tool_calls.append({
                    "id": tool_use.get("id", ""),
                    "name": tool_use.get("name", ""),
                    "arguments": tool_use.get("input", "{}")
                })
                
    except Exception as e:
        print(f"Error extracting Anthropic tool calls: {e}")
        
    return tool_calls


def parse_anthropic_arguments(arguments: Any) -> Dict[str, Any]:
    """
    Parse arguments from an Anthropic tool use.
    
    Args:
        arguments: The arguments string or object from Anthropic tool use
        
    Returns:
        A dictionary of parsed arguments
    """
    if isinstance(arguments, dict):
        return arguments
        
    try:
        if isinstance(arguments, str):
            return json.loads(arguments)
        return {}
    except (json.JSONDecodeError, TypeError):
        # If it's already a valid dict or if parsing fails
        return {} 