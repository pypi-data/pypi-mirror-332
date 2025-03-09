"""
Component Discovery module for AgentStable SDK.

This module helps search for UI components using natural language queries,
similar to how the Action Generator searches for tools. It connects to a
component discovery service to find and retrieve UI components.
"""

import json
import logging
import requests
from typing import Dict, List, Any, Optional, Union
from urllib.parse import urljoin

# Set up logging
logger = logging.getLogger(__name__)

class ComponentDiscoveryClient:
    """
    Client for searching UI components via a component discovery service.
    
    This class provides methods to search for components using natural language
    queries and retrieve component details.
    """
    
    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8000",
        auth_token: Optional[str] = None,
        timeout: int = 10
    ):
        """
        Initialize the ComponentDiscoveryClient.
        
        Args:
            base_url: The base URL of the component discovery service
            auth_token: Optional authentication token for the service
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.auth_token = auth_token
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set up authentication if provided
        if auth_token:
            self.session.headers.update({
                "Authorization": f"Bearer {auth_token}"
            })
        
        # Set common headers
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        
    def search_components(
        self,
        query: str,
        collection_id: Optional[str] = None,
        limit: int = 10
    ) -> Dict[str, Any]:
        """
        Search for UI components using a natural language query.
        
        Args:
            query: Natural language query describing the component
            collection_id: Optional collection to search within
            limit: Maximum number of results to return
            
        Returns:
            Dict containing search results with component information
        """
        search_endpoint = urljoin(self.base_url, "/search")
        
        payload = {
            "query": query,
            "limit": limit
        }
        
        if collection_id:
            payload["collection_id"] = collection_id
            
        try:
            response = self.session.post(
                search_endpoint,
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error searching components: {e}")
            return {"results": [], "count": 0}
        
    def get_component(self, component_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific component by ID.
        
        Args:
            component_id: ID of the component to retrieve
            
        Returns:
            Dict containing component information or None if not found
        """
        component_endpoint = urljoin(self.base_url, f"/components/{component_id}")
        
        try:
            response = self.session.get(
                component_endpoint,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error getting component {component_id}: {e}")
            return None
    
    def get_collections(self) -> List[Dict[str, Any]]:
        """
        Get a list of available component collections.
        
        Returns:
            List of collections with their details
        """
        collections_endpoint = urljoin(self.base_url, "/collections")
        
        try:
            response = self.session.get(
                collections_endpoint,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error getting collections: {e}")
            return []

# Simplified interface for component discovery
def search_components(
    query: str,
    base_url: str = "http://127.0.0.1:8000",
    collection_id: Optional[str] = None,
    limit: int = 10,
    auth_token: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search for UI components using a natural language query.
    
    Args:
        query: Natural language query describing the component
        base_url: The base URL of the component discovery service
        collection_id: Optional collection to search within
        limit: Maximum number of results to return
        auth_token: Optional authentication token for the service
        
    Returns:
        Dict containing search results with component information
    """
    client = ComponentDiscoveryClient(
        base_url=base_url,
        auth_token=auth_token
    )
    
    return client.search_components(
        query=query,
        collection_id=collection_id,
        limit=limit
    )

def get_component(
    component_id: str,
    base_url: str = "http://127.0.0.1:8000",
    auth_token: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a specific component by ID.
    
    Args:
        component_id: ID of the component to retrieve
        base_url: The base URL of the component discovery service
        auth_token: Optional authentication token for the service
        
    Returns:
        Dict containing component information or None if not found
    """
    client = ComponentDiscoveryClient(
        base_url=base_url,
        auth_token=auth_token
    )
    
    return client.get_component(component_id=component_id)

def get_component_collections(
    base_url: str = "http://127.0.0.1:8000",
    auth_token: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Get a list of available component collections.
    
    Args:
        base_url: The base URL of the component discovery service
        auth_token: Optional authentication token for the service
        
    Returns:
        List of collections with their details
    """
    client = ComponentDiscoveryClient(
        base_url=base_url,
        auth_token=auth_token
    )
    
    return client.get_collections() 