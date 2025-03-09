"""
Memory module for storing and managing context across actions in a flow.
"""

from typing import Any, Dict, Optional, List, Union
import uuid
import json
import os

# Try to import Redis, but don't fail if it's not installed
try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False


class Memory:
    """Base in-memory class for storing context information."""
    
    def __init__(self):
        """Initialize the memory store."""
        self._store = {}
        self._flow_contexts = {}
        
    def set(self, key: str, value: Any, flow_id: Optional[str] = None) -> None:
        """
        Store a value in memory.
        
        Args:
            key: The key to store the value under
            value: The value to store
            flow_id: Optional flow ID to scope the memory
        """
        if flow_id:
            if flow_id not in self._flow_contexts:
                self._flow_contexts[flow_id] = {}
            self._flow_contexts[flow_id][key] = value
        else:
            self._store[key] = value
            
    def get(self, key: str, flow_id: Optional[str] = None, default: Any = None) -> Any:
        """
        Retrieve a value from memory.
        
        Args:
            key: The key to retrieve
            flow_id: Optional flow ID to scope the memory
            default: Default value to return if key is not found
            
        Returns:
            The stored value or default if not found
        """
        if flow_id:
            if flow_id in self._flow_contexts:
                return self._flow_contexts[flow_id].get(key, default)
            return default
        return self._store.get(key, default)
        
    def clear(self, flow_id: Optional[str] = None) -> None:
        """
        Clear memory.
        
        Args:
            flow_id: Optional flow ID to clear only that flow's context
        """
        if flow_id:
            if flow_id in self._flow_contexts:
                self._flow_contexts[flow_id] = {}
        else:
            self._store = {}
            self._flow_contexts = {}
            
    def get_all(self, flow_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get all stored values.
        
        Args:
            flow_id: Optional flow ID to get only that flow's context
            
        Returns:
            Dictionary of all stored values
        """
        if flow_id:
            return self._flow_contexts.get(flow_id, {}).copy()
        return self._store.copy()


class RedisMemory(Memory):
    """Redis-backed memory storage for persistent context across processes and restarts."""
    
    def __init__(self, redis_url: Optional[str] = None, prefix: str = "agentstable:"):
        """
        Initialize Redis memory storage.
        
        Args:
            redis_url: Redis connection URL. If None, uses REDIS_URL environment variable.
            prefix: Key prefix for Redis storage to avoid collisions with other applications.
        """
        if not REDIS_AVAILABLE:
            raise ImportError(
                "Redis package is not installed. Please install it with: pip install redis"
            )
            
        self.prefix = prefix
        redis_url = redis_url or os.environ.get("REDIS_URL")
        
        if not redis_url:
            raise ValueError(
                "Redis URL not provided. Either pass it directly or set the REDIS_URL environment variable."
            )
            
        self.redis_client = redis.from_url(redis_url)
        
        # Check connection
        try:
            self.redis_client.ping()
        except redis.exceptions.ConnectionError as e:
            raise ConnectionError(f"Failed to connect to Redis: {e}")
    
    def _get_key(self, key: str, flow_id: Optional[str] = None) -> str:
        """Generate a Redis key with proper prefix and scoping."""
        if flow_id:
            return f"{self.prefix}flow:{flow_id}:{key}"
        return f"{self.prefix}{key}"
    
    def _serialize(self, value: Any) -> str:
        """Serialize a value to JSON string for Redis storage."""
        return json.dumps(value)
    
    def _deserialize(self, value: Optional[str]) -> Any:
        """Deserialize a JSON string from Redis to a Python object."""
        if value is None:
            return None
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    
    def set(self, key: str, value: Any, flow_id: Optional[str] = None) -> None:
        """
        Store a value in Redis.
        
        Args:
            key: The key to store the value under
            value: The value to store
            flow_id: Optional flow ID to scope the memory
        """
        redis_key = self._get_key(key, flow_id)
        serialized_value = self._serialize(value)
        self.redis_client.set(redis_key, serialized_value)
        
        # Add key to the list of keys for this flow
        if flow_id:
            # Track keys for each flow to support get_all and clear operations
            flow_keys_key = f"{self.prefix}flow_keys:{flow_id}"
            self.redis_client.sadd(flow_keys_key, key)
        else:
            # Track global keys
            global_keys_key = f"{self.prefix}global_keys"
            self.redis_client.sadd(global_keys_key, key)
            
    def get(self, key: str, flow_id: Optional[str] = None, default: Any = None) -> Any:
        """
        Retrieve a value from Redis.
        
        Args:
            key: The key to retrieve
            flow_id: Optional flow ID to scope the memory
            default: Default value to return if key is not found
            
        Returns:
            The stored value or default if not found
        """
        redis_key = self._get_key(key, flow_id)
        value = self.redis_client.get(redis_key)
        if value is None:
            return default
        return self._deserialize(value)
        
    def clear(self, flow_id: Optional[str] = None) -> None:
        """
        Clear Redis storage.
        
        Args:
            flow_id: Optional flow ID to clear only that flow's context
        """
        if flow_id:
            # Get all keys for this flow
            flow_keys_key = f"{self.prefix}flow_keys:{flow_id}"
            keys = self.redis_client.smembers(flow_keys_key)
            
            # Delete each key
            pipeline = self.redis_client.pipeline()
            for key in keys:
                redis_key = self._get_key(key.decode('utf-8') if isinstance(key, bytes) else key, flow_id)
                pipeline.delete(redis_key)
            
            # Delete the flow keys set itself
            pipeline.delete(flow_keys_key)
            pipeline.execute()
        else:
            # Clear entire storage - find all keys with our prefix and delete them
            keys = self.redis_client.keys(f"{self.prefix}*")
            if keys:
                self.redis_client.delete(*keys)
            
    def get_all(self, flow_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get all stored values from Redis.
        
        Args:
            flow_id: Optional flow ID to get only that flow's context
            
        Returns:
            Dictionary of all stored values
        """
        result = {}
        
        if flow_id:
            # Get all keys for this flow
            flow_keys_key = f"{self.prefix}flow_keys:{flow_id}"
            keys = self.redis_client.smembers(flow_keys_key)
            
            # Get each key's value
            for key in keys:
                key_str = key.decode('utf-8') if isinstance(key, bytes) else key
                value = self.get(key_str, flow_id)
                result[key_str] = value
        else:
            # Get all global keys
            global_keys_key = f"{self.prefix}global_keys"
            keys = self.redis_client.smembers(global_keys_key)
            
            # Get each key's value
            for key in keys:
                key_str = key.decode('utf-8') if isinstance(key, bytes) else key
                value = self.get(key_str)
                result[key_str] = value
                
        return result


class Session:
    """Session class for managing conversation context and flow execution."""
    
    def __init__(self, session_id: Optional[str] = None, memory: Optional[Memory] = None):
        """
        Initialize a new session.
        
        Args:
            session_id: Optional ID for the session. A UUID will be generated if not provided.
            memory: Memory backend to use. If None, in-memory storage will be used.
        """
        self.session_id = session_id or str(uuid.uuid4())
        self.memory = memory or Memory()
        self.history: List[Dict[str, Any]] = []
        
    def add_to_history(self, role: str, content: Any) -> None:
        """
        Add an item to the conversation history.
        
        Args:
            role: The role of the speaker (user, assistant, etc.)
            content: The content of the message
        """
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": uuid.uuid1().hex
        })
        
    def get_history(self) -> List[Dict[str, Any]]:
        """
        Get the conversation history.
        
        Returns:
            List of conversation history items
        """
        return self.history.copy()
        
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.history = []
        
    def set_context(self, key: str, value: Any, flow_id: Optional[str] = None) -> None:
        """
        Store a value in the session context.
        
        Args:
            key: The key to store the value under
            value: The value to store
            flow_id: Optional flow ID to scope the context
        """
        self.memory.set(key, value, flow_id)
        
    def get_context(self, key: str, flow_id: Optional[str] = None, default: Any = None) -> Any:
        """
        Retrieve a value from the session context.
        
        Args:
            key: The key to retrieve
            flow_id: Optional flow ID to scope the context
            default: Default value to return if key is not found
            
        Returns:
            The stored value or default if not found
        """
        return self.memory.get(key, flow_id, default)
        
    def get_all_context(self, flow_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get all context values.
        
        Args:
            flow_id: Optional flow ID to get only that flow's context
            
        Returns:
            Dictionary of all context values
        """
        return self.memory.get_all(flow_id)
        
    def clear_context(self, flow_id: Optional[str] = None) -> None:
        """
        Clear context values.
        
        Args:
            flow_id: Optional flow ID to clear only that flow's context
        """
        self.memory.clear(flow_id)


# Global default session for convenience
default_session = Session()


def get_session() -> Session:
    """Get the default session."""
    return default_session


def create_session(session_id: Optional[str] = None, use_redis: bool = False, redis_url: Optional[str] = None) -> Session:
    """
    Create a new session.
    
    Args:
        session_id: Optional ID for the session
        use_redis: Whether to use Redis for storage
        redis_url: Redis connection URL. If None, uses REDIS_URL environment variable.
        
    Returns:
        A new Session instance
    """
    if use_redis:
        if not REDIS_AVAILABLE:
            raise ImportError(
                "Redis package is not installed. Please install it with: pip install redis"
            )
        memory = RedisMemory(redis_url=redis_url)
        return Session(session_id, memory=memory)
    
    return Session(session_id) 