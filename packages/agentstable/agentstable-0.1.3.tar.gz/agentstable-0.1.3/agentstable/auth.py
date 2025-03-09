"""
Authentication classes for the AgentStable SDK.
These classes provide different authentication methods for API requests.
"""

import base64
from abc import ABC, abstractmethod
from typing import Dict, Optional


class Auth(ABC):
    """Base authentication class."""

    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """Return headers needed for authentication."""
        pass


class BearerAuth(Auth):
    """Bearer token authentication."""

    def __init__(self, token: str):
        """
        Initialize with a bearer token.

        Args:
            token: The bearer token for authentication
        """
        self.token = token

    def get_headers(self) -> Dict[str, str]:
        """
        Return headers for bearer token authentication.

        Returns:
            Dict with Authorization header
        """
        return {"Authorization": f"Bearer {self.token}"}


class ApiKeyAuth(Auth):
    """API key authentication."""

    def __init__(self, api_key: str, header_name: str = "X-API-Key"):
        """
        Initialize with an API key.

        Args:
            api_key: The API key for authentication
            header_name: The header name to use for the API key (default: X-API-Key)
        """
        self.api_key = api_key
        self.header_name = header_name

    def get_headers(self) -> Dict[str, str]:
        """
        Return headers for API key authentication.

        Returns:
            Dict with API key header
        """
        return {self.header_name: self.api_key}


class BasicAuth(Auth):
    """Basic authentication."""

    def __init__(self, username: str, password: str):
        """
        Initialize with username and password.

        Args:
            username: The username for basic authentication
            password: The password for basic authentication
        """
        self.username = username
        self.password = password

    def get_headers(self) -> Dict[str, str]:
        """
        Return headers for basic authentication.

        Returns:
            Dict with Authorization header
        """
        auth_str = f"{self.username}:{self.password}"
        auth_bytes = auth_str.encode("ascii")
        auth_b64 = base64.b64encode(auth_bytes).decode("ascii")
        return {"Authorization": f"Basic {auth_b64}"}


class NoAuth(Auth):
    """No authentication."""

    def get_headers(self) -> Dict[str, str]:
        """
        Return empty headers (no authentication).

        Returns:
            Empty dict
        """ 