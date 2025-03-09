"""
Component discovery module for AgentStable SDK.

This module helps AI agents find and use appropriate UI components based on natural language queries.
It uses the component discovery service to match queries with relevant components.
"""

import json
import logging
from typing import Any, Dict, List, Optional, Union, Callable, Tuple

from .component_discovery import search_components as _search_components
from .component_discovery import get_component, get_component_collections
from .usage import get_usage_tracker

# Set up logging
logger = logging.getLogger(__name__)

def search(
    query: str,
    base_url: str = "http://127.0.0.1:8000",
    collection_id: Optional[str] = None,
    limit: int = 10,
    auth_token: Optional[str] = None,
    track_usage: bool = True
) -> List[Dict[str, Any]]:
    """
    Search for components from the component discovery service based on a natural language query.
    
    Args:
        query: The natural language query to search for
        base_url: The base URL of the component discovery service
        collection_id: Optional collection ID to restrict the search
        limit: Maximum number of components to return
        auth_token: Optional authentication token
        track_usage: Whether to track usage
        
    Returns:
        A list of matching components
    """
    try:
        # Call the component discovery service
        response = _search_components(
            query=query,
            base_url=base_url,
            collection_id=collection_id,
            limit=limit,
            auth_token=auth_token
        )
        
        # Extract the component results
        components = response.get("results", [])
        
        # Track usage if enabled
        if track_usage:
            usage_tracker = get_usage_tracker()
            if usage_tracker:
                usage_tracker.add_record(
                    provider="component_discovery",
                    model="component_search",
                    input_tokens=len(query.split()),
                    output_tokens=0,  # No tokens for components
                    metadata={
                        "operation": "search_components",
                        "components_found": len(components),
                        "query": query
                    }
                )
        
        return components
    
    except Exception as e:
        logger.error(f"Error searching components: {e}")
        return []

# Keep the original function name for backward compatibility
def get_components(
    query: str,
    base_url: str = "http://127.0.0.1:8000",
    collection_id: Optional[str] = None,
    limit: int = 10,
    auth_token: Optional[str] = None,
    track_usage: bool = True
) -> List[Dict[str, Any]]:
    """
    Get components from the component discovery service based on a natural language query.
    
    This is an alias for `search()` for backward compatibility.
    
    Args:
        query: The natural language query to search for
        base_url: The base URL of the component discovery service
        collection_id: Optional collection ID to restrict the search
        limit: Maximum number of components to return
        auth_token: Optional authentication token
        track_usage: Whether to track usage
        
    Returns:
        A list of matching components
    """
    return search(
        query=query,
        base_url=base_url,
        collection_id=collection_id,
        limit=limit,
        auth_token=auth_token,
        track_usage=track_usage
    )

def format_component_for_display(component: Dict[str, Any]) -> str:
    """
    Format a component for display to the user.
    
    Args:
        component: The component data
        
    Returns:
        A formatted string representation of the component
    """
    formatted = f"### {component.get('name', 'Unnamed Component')}\n\n"
    
    # Add description if available
    if "description" in component:
        formatted += f"{component['description']}\n\n"
    
    # Add tags if available
    if "tags" in component and component["tags"]:
        tags = ", ".join(component["tags"])
        formatted += f"**Tags**: {tags}\n\n"
    
    # Add metadata if available
    if "metadata" in component and component["metadata"]:
        formatted += "**Metadata**:\n"
        for key, value in component["metadata"].items():
            formatted += f"- {key}: {value}\n"
        formatted += "\n"
    
    # Add code preview (truncated if long)
    if "code" in component:
        code = component["code"]
        if len(code) > 500:
            code = code[:500] + "...\n[truncated]"
        formatted += f"```jsx\n{code}\n```\n"
    
    return formatted

def search_and_format(
    query: str,
    base_url: str = "http://127.0.0.1:8000",
    collection_id: Optional[str] = None,
    limit: int = 5,
    auth_token: Optional[str] = None
) -> str:
    """
    Search for components and format them for display.
    
    Args:
        query: The natural language query to search for
        base_url: The base URL of the component discovery service
        collection_id: Optional collection ID to restrict the search
        limit: Maximum number of components to return
        auth_token: Optional authentication token
        
    Returns:
        A formatted string with component information
    """
    components = search(
        query=query,
        base_url=base_url,
        collection_id=collection_id,
        limit=limit,
        auth_token=auth_token
    )
    
    if not components:
        return "No matching components found."
    
    formatted_components = [format_component_for_display(component) for component in components]
    return "\n\n".join(formatted_components)

# Keep the original function name for backward compatibility
def search_and_format_components(
    query: str,
    base_url: str = "http://127.0.0.1:8000",
    collection_id: Optional[str] = None,
    limit: int = 5,
    auth_token: Optional[str] = None
) -> str:
    """
    Search for components and format them for display.
    
    This is an alias for `search_and_format()` for backward compatibility.
    
    Args:
        query: The natural language query to search for
        base_url: The base URL of the component discovery service
        collection_id: Optional collection ID to restrict the search
        limit: Maximum number of components to return
        auth_token: Optional authentication token
        
    Returns:
        A formatted string with component information
    """
    return search_and_format(
        query=query,
        base_url=base_url,
        collection_id=collection_id,
        limit=limit,
        auth_token=auth_token
    )

def get_component_by_id(
    component_id: str,
    base_url: str = "http://127.0.0.1:8000",
    auth_token: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a specific component by ID.
    
    Args:
        component_id: The ID of the component to retrieve
        base_url: The base URL of the component discovery service
        auth_token: Optional authentication token
        
    Returns:
        The component data if found, None otherwise
    """
    return get_component(
        component_id=component_id,
        base_url=base_url,
        auth_token=auth_token
    )

def get_all_collections(
    base_url: str = "http://127.0.0.1:8000",
    auth_token: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get all available component collections.
    
    Args:
        base_url: The base URL of the component discovery service
        auth_token: Optional authentication token
        
    Returns:
        A list of available component collections
    """
    return get_component_collections(
        base_url=base_url,
        auth_token=auth_token
    )

# Keep the original function name for backward compatibility
def get_all_component_collections(
    base_url: str = "http://127.0.0.1:8000",
    auth_token: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get all available component collections.
    
    This is an alias for `get_all_collections()` for backward compatibility.
    
    Args:
        base_url: The base URL of the component discovery service
        auth_token: Optional authentication token
        
    Returns:
        A list of available component collections
    """
    return get_all_collections(
        base_url=base_url,
        auth_token=auth_token
    ) 