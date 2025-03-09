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

# Handle missing modules gracefully
try:
    from .parallel import execute_actions_parallel, execute_flows_parallel, execute_tasks_parallel
except ImportError:
    # Define placeholder functions that raise NotImplementedError when called
    def execute_actions_parallel(*args, **kwargs):
        raise NotImplementedError("The parallel module is not available in this version of the SDK")
    
    def execute_flows_parallel(*args, **kwargs):
        raise NotImplementedError("The parallel module is not available in this version of the SDK")
    
    def execute_tasks_parallel(*args, **kwargs):
        raise NotImplementedError("The parallel module is not available in this version of the SDK")

from .usage import UsageTracker, UsageRecord, get_usage_tracker
from .component_discovery import (
    search_components,
    get_component,
    get_component_collections
)
from .components import (
    search as search_ui_components,
    search_and_format as search_and_format_components,
    get_all_collections as get_all_component_collections,
    get_components,
    search_and_format_components as _search_and_format_components,
    get_component_by_id,
    get_all_component_collections as _get_all_component_collections,
    format_component_for_display
)
from .action_generator import (
    ActionGenerator, 
    OpenAIActionGenerator, 
    AnthropicActionGenerator,
    convert_to_action_service_format,
    agents_json_schema_validator,
    get_schema_validation_errors,
    repair_schema
)

# Simplified interfaces for action generator workflow
def generate_action_schema_openai(
    query: str,
    api_key: str = None,
    model: str = "gpt-4-turbo-preview",
    temperature: float = 0.2,
    max_tokens: int = 4000,
    system_prompt: str = None,
    existing_schema: dict = None
):
    """
    Generate an action schema using OpenAI without requiring manual client setup.
    
    The generated schema strictly follows the agents.json format with the following components:
    - agentsJson: version string
    - info: with title, version, and description
    - sources: array of API sources with id and path
    - flows: array of flows, each with id, title, description, actions, and fields
    - Each flow includes actions, links (data connections), and fields (parameters and responses)
    
    Args:
        query: The natural language query to convert to a schema
        api_key: OpenAI API key (uses environment variable if not provided)
        model: The OpenAI model to use
        temperature: Temperature for generation
        max_tokens: Maximum tokens to generate
        system_prompt: Optional system prompt to guide generation
        existing_schema: Optional existing schema to extend
        
    Returns:
        A dictionary containing the generated schema in agents.json format
    """
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)
    generator = OpenAIActionGenerator(client=client, model=model)
    
    return generator.generate_from_query(
        query=query,
        system_prompt=system_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        existing_schema=existing_schema
    )

def generate_action_schema_anthropic(
    query: str,
    api_key: str = None,
    model: str = "claude-3-opus-20240229",
    temperature: float = 0.2,
    max_tokens: int = 4000,
    system_prompt: str = None,
    existing_schema: dict = None
):
    """
    Generate an action schema using Anthropic without requiring manual client setup.
    
    The generated schema strictly follows the agents.json format with the following components:
    - agentsJson: version string
    - info: with title, version, and description
    - sources: array of API sources with id and path
    - flows: array of flows, each with id, title, description, actions, and fields
    - Each flow includes actions, links (data connections), and fields (parameters and responses)
    
    Args:
        query: The natural language query to convert to a schema
        api_key: Anthropic API key (uses environment variable if not provided)
        model: The Anthropic model to use
        temperature: Temperature for generation
        max_tokens: Maximum tokens to generate
        system_prompt: Optional system prompt to guide generation
        existing_schema: Optional existing schema to extend
        
    Returns:
        A dictionary containing the generated schema in agents.json format
    """
    from anthropic import Anthropic
    
    client = Anthropic(api_key=api_key)
    generator = AnthropicActionGenerator(client=client, model=model)
    
    return generator.generate_from_query(
        query=query,
        system_prompt=system_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        existing_schema=existing_schema
    )

def clarify_and_generate_openai(
    initial_query: str,
    clarification_response: str = None,
    api_key: str = None,
    model: str = "gpt-4-turbo-preview",
    temperature: float = 0.2,
    max_tokens: int = 4000,
    system_prompt: str = None,
    existing_schema: dict = None
):
    """
    Generate an action schema with clarification using OpenAI.
    
    If clarification_response is None, this function returns the clarifying questions.
    If clarification_response is provided, it generates the schema based on both the
    initial query and the clarification responses.
    
    The generated schema strictly follows the agents.json format with the following components:
    - agentsJson: version string
    - info: with title, version, and description
    - sources: array of API sources with id and path
    - flows: array of flows, each with id, title, description, actions, and fields
    - Each flow includes actions, links (data connections), and fields (parameters and responses)
    
    Args:
        initial_query: The initial natural language query
        clarification_response: The user's responses to clarifying questions (or None)
        api_key: OpenAI API key (uses environment variable if not provided)
        model: The OpenAI model to use
        temperature: Temperature for generation
        max_tokens: Maximum tokens to generate
        system_prompt: Optional system prompt to guide generation
        existing_schema: Optional existing schema to extend
        
    Returns:
        If clarification_response is None: A string with clarifying questions
        If clarification_response is provided: A dictionary containing the generated schema in agents.json format
    """
    from openai import OpenAI
    
    client = OpenAI(api_key=api_key)
    generator = OpenAIActionGenerator(client=client, model=model)
    
    if clarification_response is None:
        # First step: Generate clarifying questions
        return generator.clarify_query(
            query=initial_query,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
    else:
        # Second step: Generate schema with clarifications
        return generator.generate_with_clarification(
            initial_query=initial_query,
            clarification_response=clarification_response,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            existing_schema=existing_schema
        )

def clarify_and_generate_anthropic(
    initial_query: str,
    clarification_response: str = None,
    api_key: str = None,
    model: str = "claude-3-opus-20240229",
    temperature: float = 0.2,
    max_tokens: int = 4000,
    system_prompt: str = None,
    existing_schema: dict = None
):
    """
    Generate an action schema with clarification using Anthropic.
    
    If clarification_response is None, this function returns the clarifying questions.
    If clarification_response is provided, it generates the schema based on both the
    initial query and the clarification responses.
    
    The generated schema strictly follows the agents.json format with the following components:
    - agentsJson: version string
    - info: with title, version, and description
    - sources: array of API sources with id and path
    - flows: array of flows, each with id, title, description, actions, and fields
    - Each flow includes actions, links (data connections), and fields (parameters and responses)
    
    Args:
        initial_query: The initial natural language query
        clarification_response: The user's responses to clarifying questions (or None)
        api_key: Anthropic API key (uses environment variable if not provided)
        model: The Anthropic model to use
        temperature: Temperature for generation
        max_tokens: Maximum tokens to generate
        system_prompt: Optional system prompt to guide generation
        existing_schema: Optional existing schema to extend
        
    Returns:
        If clarification_response is None: A string with clarifying questions
        If clarification_response is provided: A dictionary containing the generated schema in agents.json format
    """
    from anthropic import Anthropic
    
    client = Anthropic(api_key=api_key)
    generator = AnthropicActionGenerator(client=client, model=model)
    
    if clarification_response is None:
        # First step: Generate clarifying questions
        return generator.clarify_query(
            query=initial_query,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
    else:
        # Second step: Generate schema with clarifications
        return generator.generate_with_clarification(
            initial_query=initial_query,
            clarification_response=clarification_response,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            existing_schema=existing_schema
        )

__version__ = "0.1.2" 