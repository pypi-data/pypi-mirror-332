"""
Helper module for direct interactions with the AgentStable Search Action Service.
"""

import requests
from typing import Dict, Optional, Any, Literal

from .auth import Auth, NoAuth
from .tools import get_tools
from .anthropic_tools import get_anthropic_tools


def search(
    query: str,
    collection_id: Optional[str] = None,
    base_url: str = "http://localhost:8081/api",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Search for a flow using the AgentStable Search Action Service.

    Args:
        query: The natural language query to search for
        collection_id: The ID of the collection to search in (optional)
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        auth: The authentication method to use (optional)

    Returns:
        The response from the Search Action Service containing the matched schema and flow
    """
    params = {"query": query}
    
    if collection_id:
        params["collection_id"] = collection_id
    
    # Get authentication headers if provided
    headers = {}
    if auth:
        headers.update(auth.get_headers())
    
    response = requests.get(f"{base_url}/search", params=params, headers=headers)
    response.raise_for_status()  # Raise an exception for error status codes
    
    return response.json()


def search_and_generate_tools(
    query: str,
    collection_id: Optional[str] = None,
    base_url: str = "http://localhost:8081/api",
    provider: Literal["openai", "anthropic"] = "openai",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Search for a flow and generate LLM tools in a single operation.

    Args:
        query: The natural language query to search for
        collection_id: The ID of the collection to search in (optional)
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        provider: The LLM provider, either "openai" or "anthropic" (default: "openai")
        auth: The authentication method to use (optional)

    Returns:
        A dictionary containing the flow response and the generated tools
    """
    flow_response = search(query, collection_id, base_url, auth)
    
    if provider == "openai":
        tools = get_tools(flow_response)
    elif provider == "anthropic":
        tools = get_anthropic_tools(flow_response)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
    
    return {
        "flow": flow_response,
        "tools": tools
    }


def search_and_generate_openai_tools(
    query: str,
    collection_id: Optional[str] = None,
    base_url: str = "http://localhost:8081/api",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Search for a flow and generate OpenAI tools in a single operation.
    
    This is a convenience wrapper around the search_and_generate_tools function.

    Args:
        query: The natural language query to search for
        collection_id: The ID of the collection to search in (optional)
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        auth: The authentication method to use (optional)

    Returns:
        A dictionary containing the flow response and the generated OpenAI tools
    """
    return search_and_generate_tools(query, collection_id, base_url, provider="openai", auth=auth)


def search_and_generate_anthropic_tools(
    query: str,
    collection_id: Optional[str] = None,
    base_url: str = "http://localhost:8081/api",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Search for a flow and generate Anthropic tools in a single operation.
    
    This is a convenience wrapper around the search_and_generate_tools function.

    Args:
        query: The natural language query to search for
        collection_id: The ID of the collection to search in (optional)
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        auth: The authentication method to use (optional)

    Returns:
        A dictionary containing the flow response and the generated Anthropic tools
    """
    return search_and_generate_tools(query, collection_id, base_url, provider="anthropic", auth=auth)


def get_all_collections(
    base_url: str = "http://localhost:8081/api",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Get all available collections from the Search Action Service.

    Args:
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        auth: The authentication method to use (optional)

    Returns:
        The response from the Search Action Service containing all collections
    """
    # Get authentication headers if provided
    headers = {}
    if auth:
        headers.update(auth.get_headers())
        
    response = requests.get(f"{base_url}/collections", headers=headers)
    response.raise_for_status()
    
    return response.json()


def get_all_schemas(
    collection_id: Optional[str] = None,
    base_url: str = "http://localhost:8081/api",
    auth: Optional[Auth] = None
) -> Dict[str, Any]:
    """
    Get all available schemas from the Search Action Service.

    Args:
        collection_id: The ID of the collection to get schemas from (optional)
        base_url: The base URL of the Search Action Service (default: http://localhost:8081/api)
        auth: The authentication method to use (optional)

    Returns:
        The response from the Search Action Service containing the schemas
    """
    params = {}
    
    if collection_id:
        params["collection_id"] = collection_id
    
    # Get authentication headers if provided
    headers = {}
    if auth:
        headers.update(auth.get_headers())
        
    response = requests.get(f"{base_url}/schemas", params=params, headers=headers)
    response.raise_for_status()
    
    return response.json() 