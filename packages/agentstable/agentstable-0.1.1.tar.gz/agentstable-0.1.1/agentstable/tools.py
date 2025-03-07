"""
Tools module for converting agents.json schemas to OpenAI-compatible tools.
"""

from typing import Any, Dict, List, Optional, Union, cast
import json


def get_tools(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Convert an agents.json schema into OpenAI tools format.

    Args:
        response: The response from the search action service containing the agents.json schema

    Returns:
        A list of tools in OpenAI format
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

    # Convert the flow to an OpenAI tool
    tool = {
        "type": "function",
        "function": {
            "name": flow_id,
            "description": flow.get("description", f"Execute the {flow_id} flow"),
            "parameters": _convert_parameters(flow)
        }
    }

    return [tool]


def _convert_parameters(flow: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert flow parameters to OpenAI tool parameters format.

    Args:
        flow: The flow definition from the agents.json schema

    Returns:
        OpenAI-compatible parameters schema
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
        prop = {
            "type": param.get("type", "string"),
            "description": param.get("description", f"Parameter {param_name}")
        }
        
        # Add items property for arrays (required by OpenAI)
        if prop["type"] == "array":
            # Default to string items if not specified
            prop["items"] = {"type": "object"}
            
            # Try to infer item type from description
            desc = prop["description"].lower()
            if "string" in desc or "text" in desc or "name" in desc:
                prop["items"] = {"type": "string"}
            elif "number" in desc or "integer" in desc or "count" in desc or "amount" in desc:
                prop["items"] = {"type": "number"}
            elif "boolean" in desc or "flag" in desc or "true/false" in desc:
                prop["items"] = {"type": "boolean"}
                
        schema["properties"][param_name] = prop

        # Add enum values if available
        if param.get("enum"):
            schema["properties"][param_name]["enum"] = param.get("enum")

        # Add to required list if needed
        if param.get("required", False):
            schema["required"].append(param_name)

    return schema


def extract_tool_calls(completion_response: Any) -> List[Dict[str, Any]]:
    """
    Extract tool calls from an OpenAI completion response.

    Args:
        completion_response: The response from OpenAI chat completions API

    Returns:
        A list of extracted tool calls
    """
    tool_calls = []
    
    try:
        # Handle both dictionary responses and OpenAI API objects
        if hasattr(completion_response, "choices") and hasattr(completion_response.choices, "__getitem__"):
            # Handle OpenAI API response object
            choice = completion_response.choices[0]
            if hasattr(choice, "message") and hasattr(choice.message, "tool_calls"):
                for tool_call in choice.message.tool_calls:
                    if tool_call.type == "function":
                        tool_calls.append({
                            "id": tool_call.id,
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        })
        elif isinstance(completion_response, dict):
            # Handle dictionary response
            choices = completion_response.get("choices", [])
            if choices:
                message = choices[0].get("message", {})
                raw_tool_calls = message.get("tool_calls", [])
                
                for call in raw_tool_calls:
                    if call.get("type") == "function":
                        function = call.get("function", {})
                        tool_calls.append({
                            "id": call.get("id", ""),
                            "name": function.get("name", ""),
                            "arguments": function.get("arguments", "{}")
                        })
                
    except Exception as e:
        print(f"Error extracting tool calls: {e}")
        
    return tool_calls 