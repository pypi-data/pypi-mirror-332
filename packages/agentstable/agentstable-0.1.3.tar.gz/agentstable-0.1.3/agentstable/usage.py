"""
Token usage tracking for AgentStable SDK.

This module provides utilities for tracking token usage across API calls.
"""

from typing import Dict, List, Optional, Union, Any
import time
import json
from datetime import datetime


class UsageRecord:
    """A record of token usage for a single API call."""
    
    def __init__(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        timestamp: Optional[float] = None,
        request_id: Optional[str] = None,
        flow_id: Optional[str] = None,
        session_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.provider = provider
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = input_tokens + output_tokens
        self.timestamp = timestamp or time.time()
        self.request_id = request_id
        self.flow_id = flow_id
        self.session_id = session_id
        self.metadata = metadata or {}
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert the usage record to a dictionary."""
        return {
            "provider": self.provider,
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "timestamp": self.timestamp,
            "datetime": datetime.fromtimestamp(self.timestamp).isoformat(),
            "request_id": self.request_id,
            "flow_id": self.flow_id,
            "session_id": self.session_id,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UsageRecord':
        """Create a usage record from a dictionary."""
        input_tokens = data.get("input_tokens", 0)
        output_tokens = data.get("output_tokens", 0)
        
        return cls(
            provider=data.get("provider", "unknown"),
            model=data.get("model", "unknown"),
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            timestamp=data.get("timestamp"),
            request_id=data.get("request_id"),
            flow_id=data.get("flow_id"),
            session_id=data.get("session_id"),
            metadata=data.get("metadata", {})
        )
    
    def __str__(self) -> str:
        """String representation of the usage record."""
        dt = datetime.fromtimestamp(self.timestamp).strftime("%Y-%m-%d %H:%M:%S")
        return (f"[{dt}] {self.provider}/{self.model}: "
                f"{self.input_tokens} in, {self.output_tokens} out, "
                f"{self.total_tokens} total")


class UsageTracker:
    """
    Track token usage across API calls.
    
    This class provides methods for recording and analyzing token usage
    for different providers and models.
    """
    
    def __init__(self, session=None):
        """Initialize the usage tracker."""
        self.records: List[UsageRecord] = []
        self.session = session
        self._load_from_session()
    
    def _load_from_session(self):
        """Load usage records from the session if available."""
        if self.session is None:
            return
        
        try:
            # Try to get usage records from the session context
            usage_data = self.session.get_context("usage_records", "system")
            
            if not usage_data:
                print("No usage records found in session.")
                return
            
            # If the data is a string, try to parse it as JSON
            if isinstance(usage_data, str):
                try:
                    usage_data = json.loads(usage_data)
                    print(f"Loaded {len(usage_data)} usage records from session (JSON string).")
                except json.JSONDecodeError as e:
                    print(f"Error decoding usage records JSON: {e}")
                    return
            
            # Ensure usage_data is a list
            if not isinstance(usage_data, list):
                print(f"Usage data is not a list: {type(usage_data)}")
                return
            
            # Clear existing records before loading
            self.records = []
            
            # Load each record
            for record_data in usage_data:
                try:
                    record = UsageRecord.from_dict(record_data)
                    self.records.append(record)
                except Exception as e:
                    print(f"Error loading usage record: {e}")
                    continue
            
            print(f"Successfully loaded {len(self.records)} usage records from session.")
        except Exception as e:
            print(f"Error loading usage records from session: {e}")
    
    def _save_to_session(self):
        """Save usage records to the session if available."""
        if self.session is None:
            print("No session available to save usage records.")
            return
        
        try:
            # Convert records to dictionaries
            usage_data = [record.to_dict() for record in self.records]
            
            # Save as JSON string
            json_data = json.dumps(usage_data)
            
            # Save to session context
            self.session.set_context("usage_records", json_data, "system")
            print(f"Saved {len(self.records)} usage records to session.")
        except Exception as e:
            print(f"Error saving usage records to session: {e}")
    
    def add_record(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        request_id: Optional[str] = None,
        flow_id: Optional[str] = None,
        session_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> UsageRecord:
        """
        Add a new usage record.
        
        Args:
            provider: The provider name (e.g., "anthropic", "openai")
            model: The model name (e.g., "claude-3-haiku", "gpt-4")
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            request_id: Optional request identifier
            flow_id: Optional flow identifier
            session_id: Optional session identifier
            metadata: Optional additional metadata
            
        Returns:
            The created usage record
        """
        # Use session ID from the session if available
        if self.session and session_id is None:
            session_id = getattr(self.session, "session_id", None)
        
        # Create the record
        record = UsageRecord(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            request_id=request_id,
            flow_id=flow_id,
            session_id=session_id,
            metadata=metadata
        )
        
        # Add to the list of records
        self.records.append(record)
        
        # Save to session
        print(f"Adding usage record: {provider}/{model} - {input_tokens} in, {output_tokens} out")
        self._save_to_session()
        
        return record
    
    def add_record_from_response(
        self,
        response: Any,
        provider: str,
        model: Optional[str] = None,
        flow_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Optional[UsageRecord]:
        """
        Add a usage record from an API response.
        
        This method extracts usage information from various API response formats.
        
        Args:
            response: The API response
            provider: The provider name
            model: Optional model name (extracted from response if possible)
            flow_id: Optional flow identifier
            metadata: Optional additional metadata
            
        Returns:
            The created usage record, or None if usage info couldn't be extracted
        """
        # Default values
        input_tokens = 0
        output_tokens = 0
        request_id = None
        actual_model = model
        
        # Extract usage based on provider
        if provider.lower() == "anthropic":
            # Handle Anthropic message object
            if hasattr(response, "usage"):
                usage = response.usage
                input_tokens = getattr(usage, "input_tokens", 0)
                output_tokens = getattr(usage, "output_tokens", 0)
                
            # Handle dictionary with usage key
            elif isinstance(response, dict) and "usage" in response:
                usage = response["usage"]
                if isinstance(usage, dict):
                    input_tokens = usage.get("input_tokens", 0)
                    output_tokens = usage.get("output_tokens", 0)
            
            # Get model name if available
            if hasattr(response, "model") and actual_model is None:
                actual_model = response.model
                
            # Get message ID as request ID if available
            if hasattr(response, "id"):
                request_id = response.id
        
        elif provider.lower() == "openai":
            # Handle OpenAI completion object
            if hasattr(response, "usage"):
                usage = response.usage
                input_tokens = getattr(usage, "prompt_tokens", 0)
                output_tokens = getattr(usage, "completion_tokens", 0)
            
            # Handle dictionary with usage key
            elif isinstance(response, dict) and "usage" in response:
                usage = response["usage"]
                if isinstance(usage, dict):
                    input_tokens = usage.get("prompt_tokens", 0)
                    output_tokens = usage.get("completion_tokens", 0)
            
            # Get model name if available
            if hasattr(response, "model") and actual_model is None:
                actual_model = response.model
                
            # Get ID as request ID if available
            if hasattr(response, "id"):
                request_id = response.id
        
        # If we couldn't extract any token usage, return None
        if input_tokens == 0 and output_tokens == 0:
            return None
        
        # Add the record
        return self.add_record(
            provider=provider,
            model=actual_model or "unknown",
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            request_id=request_id,
            flow_id=flow_id,
            metadata=metadata
        )
    
    def get_records(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        flow_id: Optional[str] = None,
        session_id: Optional[str] = None,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None
    ) -> List[UsageRecord]:
        """
        Get usage records matching the given filters.
        
        Args:
            provider: Filter by provider name (e.g., "anthropic", "openai")
            model: Filter by model name
            flow_id: Filter by flow identifier
            session_id: Filter by session identifier
            start_time: Filter by start timestamp (inclusive)
            end_time: Filter by end timestamp (inclusive)
            
        Returns:
            A list of matching usage records
        """
        filtered_records = self.records
        
        if provider:
            filtered_records = [r for r in filtered_records if r.provider == provider]
            
        if model:
            filtered_records = [r for r in filtered_records if r.model == model]
            
        if flow_id:
            filtered_records = [r for r in filtered_records if r.flow_id == flow_id]
            
        if session_id:
            filtered_records = [r for r in filtered_records if r.session_id == session_id]
            
        if start_time is not None:
            filtered_records = [r for r in filtered_records if r.timestamp >= start_time]
            
        if end_time is not None:
            filtered_records = [r for r in filtered_records if r.timestamp <= end_time]
            
        return filtered_records
    
    def get_usage_summary(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        flow_id: Optional[str] = None,
        session_id: Optional[str] = None,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Get a summary of token usage.
        
        Args:
            provider: Filter by provider name (e.g., "anthropic", "openai")
            model: Filter by model name
            flow_id: Filter by flow identifier
            session_id: Filter by session identifier
            start_time: Filter by start timestamp (inclusive)
            end_time: Filter by end timestamp (inclusive)
            
        Returns:
            A dictionary containing token usage statistics
        """
        records = self.get_records(provider, model, flow_id, session_id, start_time, end_time)
        
        total_input_tokens = sum(r.input_tokens for r in records)
        total_output_tokens = sum(r.output_tokens for r in records)
        total_tokens = total_input_tokens + total_output_tokens
        
        # Group by provider
        usage_by_provider = {}
        for record in records:
            if record.provider not in usage_by_provider:
                usage_by_provider[record.provider] = {
                    "calls": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0
                }
                
            usage_by_provider[record.provider]["calls"] += 1
            usage_by_provider[record.provider]["input_tokens"] += record.input_tokens
            usage_by_provider[record.provider]["output_tokens"] += record.output_tokens
            usage_by_provider[record.provider]["total_tokens"] += record.total_tokens
        
        # Group by model
        usage_by_model = {}
        for record in records:
            if record.model not in usage_by_model:
                usage_by_model[record.model] = {
                    "calls": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0
                }
                
            usage_by_model[record.model]["calls"] += 1
            usage_by_model[record.model]["input_tokens"] += record.input_tokens
            usage_by_model[record.model]["output_tokens"] += record.output_tokens
            usage_by_model[record.model]["total_tokens"] += record.total_tokens
        
        # Group by flow
        usage_by_flow = {}
        for record in records:
            if not record.flow_id:
                continue
                
            if record.flow_id not in usage_by_flow:
                usage_by_flow[record.flow_id] = {
                    "calls": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0
                }
                
            usage_by_flow[record.flow_id]["calls"] += 1
            usage_by_flow[record.flow_id]["input_tokens"] += record.input_tokens
            usage_by_flow[record.flow_id]["output_tokens"] += record.output_tokens
            usage_by_flow[record.flow_id]["total_tokens"] += record.total_tokens
        
        return {
            "total_calls": len(records),
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_tokens": total_tokens,
            "usage_by_provider": usage_by_provider,
            "usage_by_model": usage_by_model,
            "usage_by_flow": usage_by_flow
        }
    
    def clear_records(self):
        """Clear all usage records."""
        self.records = []
        self._save_to_session()
    
    def export_records(self, format: str = "json") -> str:
        """
        Export usage records in the specified format.
        
        Args:
            format: The export format (currently only "json" is supported)
            
        Returns:
            A string representation of the usage records
        """
        data = [record.to_dict() for record in self.records]
        
        if format.lower() == "json":
            return json.dumps(data, indent=2)
        else:
            raise ValueError(f"Unsupported export format: {format}")
    
    def print_summary(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        flow_id: Optional[str] = None,
        session_id: Optional[str] = None
    ):
        """
        Print a summary of token usage.
        
        Args:
            provider: Filter by provider name (e.g., "anthropic", "openai")
            model: Filter by model name
            flow_id: Filter by flow identifier
            session_id: Filter by session identifier
        """
        summary = self.get_usage_summary(provider, model, flow_id, session_id)
        
        print("===== TOKEN USAGE SUMMARY =====")
        print(f"Total API calls: {summary['total_calls']}")
        print(f"Total tokens: {summary['total_tokens']}")
        print(f"  - Input tokens: {summary['total_input_tokens']}")
        print(f"  - Output tokens: {summary['total_output_tokens']}")
        
        if summary["usage_by_provider"]:
            print("\nUsage by Provider:")
            for provider_name, data in summary["usage_by_provider"].items():
                print(f"  {provider_name}:")
                print(f"    Calls: {data['calls']}")
                print(f"    Tokens: {data['total_tokens']} ({data['input_tokens']} in, {data['output_tokens']} out)")
        
        if summary["usage_by_model"]:
            print("\nUsage by Model:")
            for model_name, data in summary["usage_by_model"].items():
                print(f"  {model_name}:")
                print(f"    Calls: {data['calls']}")
                print(f"    Tokens: {data['total_tokens']} ({data['input_tokens']} in, {data['output_tokens']} out)")
        
        if summary["usage_by_flow"]:
            print("\nUsage by Flow:")
            for flow_id, data in summary["usage_by_flow"].items():
                print(f"  {flow_id}:")
                print(f"    Calls: {data['calls']}")
                print(f"    Tokens: {data['total_tokens']} ({data['input_tokens']} in, {data['output_tokens']} out)")


# Global singleton instance
global_usage_tracker = UsageTracker()

def get_usage_tracker(session=None) -> UsageTracker:
    """
    Get the usage tracker instance.
    
    If a session is provided, it will be used for storage.
    Otherwise, the global tracker instance will be used.
    
    Args:
        session: Optional session object for storing usage data
        
    Returns:
        A UsageTracker instance
    """
    if session is None:
        return global_usage_tracker
        
    return UsageTracker(session) 