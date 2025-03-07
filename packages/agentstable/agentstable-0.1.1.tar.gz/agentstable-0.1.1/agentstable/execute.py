"""
Execute module for running API actions based on tool outputs from LLMs.
"""

import json
import requests
from typing import Any, Dict, List, Optional, Union, Literal

from .auth import Auth, NoAuth
from .tools import extract_tool_calls
from .anthropic_tools import extract_anthropic_tool_calls, parse_anthropic_arguments
from .memory import Session, get_session


def execute(
    flow_response: Dict[str, Any], 
    llm_response: Any,
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    provider: Literal["openai", "anthropic"] = "openai",
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute API calls based on the flow and LLM tool output.

    Args:
        flow_response: The response from the search action service
        llm_response: The response from an LLM API (OpenAI or Anthropic)
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None, will use the schema's base URL)
        provider: The LLM provider, either "openai" or "anthropic" (default: "openai")
        session: Session object for context management (default: None, will use default session)

    Returns:
        The response from the API calls
    """
    if not auth:
        auth = NoAuth()
        
    # Get session for context management
    if session is None:
        session = get_session()

    # Extract the schema and flow ID
    schema = flow_response.get("schema", {})
    flow_id = flow_response.get("flow_id")

    if not schema or not flow_id:
        raise ValueError("Invalid flow response: missing schema or flow_id")

    # Find the flow in the schema
    flow = None
    for f in schema.get("flows", []):
        if f.get("id") == flow_id:
            flow = f
            break

    if not flow:
        raise ValueError(f"Flow with ID '{flow_id}' not found in schema")

    # Extract tool calls based on provider
    tool_calls = []
    if provider == "openai":
        # For OpenAI, use the regular extractor
        tool_calls = extract_tool_calls(llm_response)
    elif provider == "anthropic":
        # For Anthropic, use the specialized extractor
        tool_calls = extract_anthropic_tool_calls(llm_response)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    if not tool_calls:
        raise ValueError(f"No valid tool calls found in the {provider} response")

    # Get the first matching tool call
    tool_call = None
    for call in tool_calls:
        if call.get("name") == flow_id:
            tool_call = call
            break

    if not tool_call:
        raise ValueError(f"No tool call found for flow '{flow_id}'")

    # Parse the arguments
    arguments = {}
    try:
        if provider == "openai":
            arguments_str = tool_call.get("arguments", "{}")
            if isinstance(arguments_str, str):
                arguments = json.loads(arguments_str)
            else:
                arguments = arguments_str
        else:  # anthropic
            arguments = parse_anthropic_arguments(tool_call.get("arguments", "{}"))
    except (json.JSONDecodeError, AttributeError, TypeError) as e:
        raise ValueError(f"Invalid arguments in tool call: {e}")
    
    # Enhance arguments with context from session if available
    context = session.get_all_context(flow_id)
    for key, value in context.items():
        # Only add context variables that aren't already in the arguments
        if key not in arguments:
            arguments[key] = value

    # Get the flow actions
    actions = flow.get("actions", [])
    
    if not actions:
        raise ValueError(f"No actions defined in flow '{flow_id}'")

    # Get the sources from the schema
    sources = {source.get("id"): source.get("path") for source in schema.get("sources", [])}

    # Execute actions in sequence
    results = {}
    action_results = {}

    # Determine the default base URL to use
    default_base_url = schema.get("info", {}).get("server", "")
    if not base_url:
        base_url = default_base_url

    # For each action in the flow
    for i, action in enumerate(actions):
        action_id = action.get("id")
        
        if not action_id:
            action_id = f"action_{i}"
            
        # Check how this action is defined - regular path or sourceId/operationId
        path = action.get("path", "")
        source_id = action.get("sourceId")
        operation_id = action.get("operationId")
        
        # Handle actions defined with sourceId and operationId
        if source_id and operation_id:
            # Look up the source path from the schema
            if source_id not in sources:
                raise ValueError(f"Source ID '{source_id}' not found in schema sources")
                
            source_path = sources[source_id]
            if not source_path:
                raise ValueError(f"Source path for source ID '{source_id}' is empty")
                
            # Use the source path as the endpoint
            url = source_path
            
            # If the URL is a full URL, use it as is; otherwise, combine with base_url
            if not (url.startswith("http://") or url.startswith("https://")):
                url = f"{base_url.rstrip('/')}/{url.lstrip('/')}"
                
            print(f"Executing action '{action_id}' with sourceId={source_id}, operationId={operation_id}")
            
            # Get authentication headers
            headers = auth.get_headers()
            headers["Content-Type"] = "application/json"
            
            # Make the request - assume it's a POST by default
            http_method = action.get("method", "POST").upper()
            
            # Add any query parameters
            params = {k: v for k, v in arguments.items() if action.get("parameterIn", {}).get(k) == "query"}
            
            # Add request body
            body = {k: v for k, v in arguments.items() if action.get("parameterIn", {}).get(k) != "query"}
            
            # Add operation ID parameter if needed
            if "?" not in url and operation_id:
                params["operation"] = operation_id
                
            # Make the request
            response = requests.request(
                method=http_method,
                url=url,
                params=params,
                json=body if body else None,
                headers=headers
            )
            
            # Store the result
            action_results[action_id] = {
                "status_code": response.status_code,
                "response": response.json() if _is_json(response) else response.text
            }
            
        elif path:
            # Handle regular path-based actions
            # Construct the full URL
            url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
            
            # Replace path parameters
            for param_name, param_value in arguments.items():
                placeholder = f"{{{param_name}}}"
                if placeholder in url:
                    url = url.replace(placeholder, str(param_value))
            
            # Prepare request parameters
            request_params = {}
            request_json = None
            
            # Handle different HTTP methods
            http_method = action.get("method", "GET").upper()
            if http_method in ["GET", "DELETE"]:
                request_params = {k: v for k, v in arguments.items() if f"{{{k}}}" not in path}
            else:  # POST, PUT, PATCH
                request_json = {k: v for k, v in arguments.items() if f"{{{k}}}" not in path}
            
            # Get authentication headers
            headers = auth.get_headers()
            
            # Add content type for JSON requests
            if request_json:
                headers["Content-Type"] = "application/json"
            
            # Make the request
            response = requests.request(
                method=http_method,
                url=url,
                params=request_params,
                json=request_json,
                headers=headers
            )
            
            # Store the result
            action_results[action_id] = {
                "status_code": response.status_code,
                "response": response.json() if _is_json(response) else response.text
            }
        else:
            # No valid action definition
            raise ValueError(f"Action '{action_id}' has neither path nor valid sourceId/operationId")
        
        # Handle links between actions (data passed from one action to another)
        if i < len(actions) - 1:
            # Process any links for this action
            for link in flow.get("links", []):
                source_action = None
                source_field = None
                
                # Check for different link formats
                if "source" in link and "source_path" in link:
                    # Standard format
                    source_action = link.get("source")
                    source_field = link.get("source_path")
                elif "origin" in link and "target" in link:
                    # Alternative format with origin/target objects
                    origin = link.get("origin", {})
                    source_action = origin.get("actionId")
                    source_field = origin.get("fieldPath")
                
                # Get target information
                target_action = None
                target_field = None
                
                if "target" in link and "target_path" in link:
                    # Standard format
                    target_action = link.get("target")
                    target_field = link.get("target_path")
                elif "target" in link and isinstance(link["target"], dict):
                    # Alternative format with target object
                    target = link.get("target", {})
                    target_action = target.get("actionId")
                    target_field = target.get("fieldPath")
                
                if source_action == action_id and source_field and target_field:
                    # Extract data from the source response
                    source_data = _extract_data_by_path(
                        action_results[action_id]["response"], 
                        source_field
                    )
                    
                    # Add to arguments for future actions
                    if source_data is not None:
                        arguments[target_field] = source_data
                        
                        # Also store in session context
                        memory_key = f"{target_field}"
                        session.set_context(memory_key, source_data, flow_id)
                        
                # Check for memory links (links with useMemory=true)
                if link.get("useMemory") or link.get("memory"):
                    memory_source = source_action
                    memory_field = source_field
                    memory_key = f"{memory_source}.{memory_field}" if memory_field else memory_source
                    
                    if memory_source == action_id:
                        # Extract memory value
                        memory_value = None
                        
                        if memory_field:
                            memory_value = _extract_data_by_path(
                                action_results[action_id]["response"], 
                                memory_field
                            )
                        else:
                            memory_value = action_results[action_id]["response"]
                            
                        # Store in context with the appropriate key
                        if memory_value is not None:
                            session.set_context(memory_key, memory_value, flow_id)
    
    # Store the entire result in context
    session.set_context("last_result", action_results, flow_id)
    
    # Return the results of all actions
    return {
        "flow_id": flow_id,
        "action_results": action_results,
        "context": session.get_all_context(flow_id)  # Include context in the response
    }


def execute_openai(
    flow_response: Dict[str, Any],
    openai_response: Dict[str, Any],
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute API calls based on OpenAI tool output.
    
    This is a convenience wrapper around the execute function.

    Args:
        flow_response: The response from the search action service
        openai_response: The response from OpenAI chat completions API
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None, will use the schema's base URL)
        session: Session object for context management (default: None, will use default session)

    Returns:
        The response from the API calls
    """
    return execute(flow_response, openai_response, auth, base_url, provider="openai", session=session)


def execute_anthropic(
    flow_response: Dict[str, Any],
    anthropic_response: Any,
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute API calls based on Anthropic tool output.
    
    This is a convenience wrapper around the execute function.

    Args:
        flow_response: The response from the search action service
        anthropic_response: The response from Anthropic API
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None, will use the schema's base URL)
        session: Session object for context management (default: None, will use default session)

    Returns:
        The response from the API calls
    """
    return execute(flow_response, anthropic_response, auth, base_url, provider="anthropic", session=session)


def _is_json(response: requests.Response) -> bool:
    """Check if a response contains JSON data."""
    content_type = response.headers.get("Content-Type", "")
    return "application/json" in content_type


def _extract_data_by_path(data: Any, path: str) -> Any:
    """
    Extract data from a nested structure using a dot-notation path.
    
    Example: "data.items[0].id" would extract the id from the first item.
    """
    if not path:
        return data
        
    parts = path.split(".")
    current = data
    
    for part in parts:
        # Handle array indexing
        if "[" in part and part.endswith("]"):
            key, index_str = part.split("[", 1)
            index = int(index_str.rstrip("]"))
            
            if key:
                current = current.get(key, {})[index] if isinstance(current, dict) else None
            else:
                current = current[index] if isinstance(current, list) and 0 <= index < len(current) else None
        else:
            # Handle dictionary key
            current = current.get(part) if isinstance(current, dict) else None
            
        if current is None:
            break
            
    return current 