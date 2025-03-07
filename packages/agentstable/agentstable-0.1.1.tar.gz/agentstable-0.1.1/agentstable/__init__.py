"""
AgentStable SDK - A Python library for integrating with the AgentStable Search Action Service.

This SDK helps AI agents find and execute appropriate API actions based on natural language queries.
It uses semantic search to match user intents with actions defined in agents.json schemas.
"""

from .auth import BearerAuth, ApiKeyAuth, BasicAuth, NoAuth
from .tools import get_tools, extract_tool_calls
from .anthropic_tools import get_anthropic_tools, extract_anthropic_tool_calls
from .execute import execute, execute_openai, execute_anthropic
from .search import (
    search, 
    search_and_generate_tools,
    search_and_generate_openai_tools,
    search_and_generate_anthropic_tools,
    get_all_collections, 
    get_all_schemas
)
from .memory import Session, Memory, get_session, create_session, default_session
from .streaming import stream_anthropic, stream_openai
from .parallel import execute_actions_parallel, execute_flows_parallel, execute_tasks_parallel

__version__ = "0.1.1" 