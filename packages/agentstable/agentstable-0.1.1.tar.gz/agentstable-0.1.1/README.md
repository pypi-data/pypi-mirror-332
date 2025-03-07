# AgentStable SDK

A Python SDK for integrating with the AgentStable Search Action Service. This SDK helps AI agents find and execute appropriate API actions based on natural language queries using the agents.json schema.

## Installation

```bash
pip install agentstable
```

## Quick Start

### Using with OpenAI

```python
import agentstable
from openai import OpenAI

# 1. Search for actions that match a natural language query
query = "Create a product called Premium Access for $100"
flow = agentstable.search(
    query=query,
    collection_id="your_collection_id",  # Optional
    base_url="http://localhost:8081/api"  # Change to your service URL
)

# 2. Generate OpenAI tools from the flow
tools = agentstable.get_tools(flow)

# 3. Use the tools with an LLM
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": query
    }],
    tools=tools
)

# 4. Execute the API calls using the LLM's output
auth = agentstable.BearerAuth(token="your_api_token")
result = agentstable.execute(flow, response, auth)

print(f"Execution results: {result}")
```

### Using with Anthropic

```python
import agentstable
from anthropic import Anthropic

# 1. Search and generate Anthropic tools in one step
query = "Plan a vacation to Hawaii"
result = agentstable.search_and_generate_anthropic_tools(
    query=query,
    collection_id="your_collection_id",  # Optional
)

flow = result["flow"]
tools = result["tools"]

# 2. Use the tools with Anthropic
client = Anthropic()
response = client.messages.create(
    model="claude-3-sonnet-20240229",
    messages=[{
        "role": "user",
        "content": query
    }],
    tools=tools
)

# 3. Execute the API calls using the Claude's output
auth = agentstable.BearerAuth(token="your_api_token")
result = agentstable.execute_anthropic(flow, response, auth)

print(f"Execution results: {result}")
```

## Advanced Usage

### Memory and Context Management

AgentStable SDK provides memory and context management capabilities to maintain state across API calls:

```python
import agentstable

# Create a session to manage context
session = agentstable.create_session("my_session")

# Add context variables manually
session.set_context("user_id", "12345", flow_id="user_flow")
session.set_context("preferences", {"theme": "dark"}, flow_id="user_flow")

# Execute actions with the session
result = agentstable.execute_openai(
    flow, response, auth, session=session
)

# The session automatically stores results from previous actions
# and makes them available to subsequent calls
print(session.get_all_context("user_flow"))

# Access specific context variables
user_id = session.get_context("user_id", flow_id="user_flow")
```

#### Persistent Redis Storage

For persistent storage across restarts and processes, AgentStable supports Redis:

```python
# Create a session with Redis as the storage backend
session = agentstable.create_session(
    session_id="persistent_session_id",
    use_redis=True,
    redis_url="redis://username:password@host:port"
)

# Or use the REDIS_URL environment variable
import os
os.environ["REDIS_URL"] = "redis://username:password@host:port"
session = agentstable.create_session(
    session_id="persistent_session_id",
    use_redis=True
)

# Use the session as normal - all data will be stored in Redis
session.set_context("user_data", {"name": "Alice"}, "user_flow")

# Data persists across sessions with the same ID
new_session = agentstable.create_session(
    session_id="persistent_session_id",
    use_redis=True
)
user_data = new_session.get_context("user_data", "user_flow")  # Returns {"name": "Alice"}
```

#### Session Features

- **Persistence across calls**: Context is maintained between different API calls
- **Flow-specific context**: Each flow can have its own isolated context
- **Automatic context sharing**: Results from previous actions are available to future actions
- **Conversation history**: Track the history of user-assistant interactions
- **Redis storage**: Optional persistent storage using Redis

### Direct Search and Tool Generation

You can combine searching and tool generation in a single call:

```python
# For OpenAI
openai_result = agentstable.search_and_generate_openai_tools(
    query="Create a product called Premium Access for $100",
    collection_id="your_collection_id"
)

# For Anthropic
anthropic_result = agentstable.search_and_generate_anthropic_tools(
    query="Create a product called Premium Access for $100",
    collection_id="your_collection_id"
)
```

### Different Authentication Methods

The SDK supports multiple authentication methods:

```python
# Bearer token authentication
auth = agentstable.BearerAuth(token="your_token")

# API key authentication
auth = agentstable.ApiKeyAuth(api_key="your_api_key", header_name="X-API-Key")

# Basic authentication
auth = agentstable.BasicAuth(username="your_username", password="your_password")

# No authentication
auth = agentstable.NoAuth()
```

### Get Available Collections and Schemas

```python
# Get all collections
collections = agentstable.get_all_collections()

# Get all schemas in a collection
schemas = agentstable.get_all_schemas(collection_id="your_collection_id")
```

## API Reference

### Search Functions

- `search(query, collection_id, base_url)` - Search for a flow using natural language
- `search_and_generate_tools(query, collection_id, base_url, provider)` - Search and generate tools for any supported provider
- `search_and_generate_openai_tools(query, collection_id, base_url)` - Search and generate OpenAI tools
- `search_and_generate_anthropic_tools(query, collection_id, base_url)` - Search and generate Anthropic tools

### Tool Generation

- `get_tools(response)` - Generate OpenAI tools from a flow response
- `get_anthropic_tools(response)` - Generate Anthropic tools from a flow response

### Execution Functions

- `execute(flow_response, llm_response, auth, base_url, provider, session)` - Execute API calls based on LLM output
- `execute_openai(flow_response, openai_response, auth, base_url, session)` - Execute using OpenAI responses
- `execute_anthropic(flow_response, anthropic_response, auth, base_url, session)` - Execute using Anthropic responses

### Memory and Context Management

- `create_session(session_id, use_redis, redis_url)` - Create a new session for context management
- `get_session()` - Get the default session
- `session.set_context(key, value, flow_id)` - Store a value in session context
- `session.get_context(key, flow_id, default)` - Retrieve a value from session context
- `session.get_all_context(flow_id)` - Get all context for a flow
- `session.clear_context(flow_id)` - Clear context for a flow

## Documentation

For complete documentation, visit [the GitHub repository](https://github.com/clayton-dcruze/agentstable-sdk).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
