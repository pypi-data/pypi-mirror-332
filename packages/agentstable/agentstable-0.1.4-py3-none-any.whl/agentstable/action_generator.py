"""
Action Generator module for AgentStable SDK.

This module helps create services that generate action schemas from natural language.
It simplifies the process of building action generator services that can take
natural language queries and convert them to the JSON schema required for actions.
"""

from typing import Any, Dict, List, Optional, Union, Callable
import json
import logging

from .usage import get_usage_tracker

# Set up logging
logger = logging.getLogger(__name__)

# Define the agents.json schema structure for validation
AGENTS_JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["agentsJson", "info", "sources", "flows"],
    "properties": {
        "agentsJson": {
            "type": "string",
            "description": "Version of the agents.json specification being used"
        },
        "info": {
            "type": "object",
            "required": ["title", "version", "description"],
            "properties": {
                "title": {"type": "string"},
                "version": {"type": "string"},
                "description": {"type": "string"}
            }
        },
        "sources": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "path"],
                "properties": {
                    "id": {"type": "string"},
                    "path": {"type": "string"}
                }
            }
        },
        "flows": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "title", "description", "actions", "fields"],
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "actions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["id", "sourceId", "operationId"],
                            "properties": {
                                "id": {"type": "string"},
                                "sourceId": {"type": "string"},
                                "operationId": {"type": "string"}
                            }
                        }
                    },
                    "links": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["origin", "target"],
                            "properties": {
                                "origin": {
                                    "type": "object",
                                    "required": ["fieldPath", "actionId"],
                                    "properties": {
                                        "actionId": {"type": ["string", "null"]},
                                        "fieldPath": {"type": "string"}
                                    }
                                },
                                "target": {
                                    "type": "object",
                                    "required": ["fieldPath", "actionId"],
                                    "properties": {
                                        "actionId": {"type": "string"},
                                        "fieldPath": {"type": "string"}
                                    }
                                }
                            }
                        }
                    },
                    "fields": {
                        "type": "object",
                        "required": ["parameters", "responses"],
                        "properties": {
                            "parameters": {"type": "array"},
                            "responses": {
                                "type": "object",
                                "required": ["success"]
                            }
                        }
                    }
                }
            }
        }
    }
}

def agents_json_schema_validator(schema: Dict[str, Any]) -> bool:
    """
    Validate that a schema conforms to the agents.json schema format.
    
    Args:
        schema: The schema to validate
        
    Returns:
        True if the schema is valid, False otherwise
    """
    validation_errors = get_schema_validation_errors(schema)
    return len(validation_errors) == 0

def get_schema_validation_errors(schema: Dict[str, Any]) -> List[str]:
    """
    Get a list of validation errors for a schema against the agents.json format.
    
    Args:
        schema: The schema to validate
        
    Returns:
        List of error messages, empty if valid
    """
    errors = []
    
    # Check for required top-level fields
    for field in ["agentsJson", "info", "sources", "flows"]:
        if field not in schema:
            errors.append(f"Missing required top-level field '{field}' in schema")
    
    if len(errors) > 0:
        return errors  # Return early if missing top-level fields
    
    # Validate info section
    info = schema.get("info", {})
    for field in ["title", "version", "description"]:
        if field not in info:
            errors.append(f"Missing required field '{field}' in info section")
    
    # Validate sources
    sources = schema.get("sources", [])
    if not isinstance(sources, list):
        errors.append("Sources must be an array")
    else:
        for i, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"Source at index {i} must be an object")
            else:
                for field in ["id", "path"]:
                    if field not in source:
                        errors.append(f"Missing required field '{field}' in source at index {i}")
    
    # Validate flows
    flows = schema.get("flows", [])
    if not isinstance(flows, list):
        errors.append("Flows must be an array")
    else:
        for i, flow in enumerate(flows):
            if not isinstance(flow, dict):
                errors.append(f"Flow at index {i} must be an object")
            else:
                for field in ["id", "title", "description", "actions", "fields"]:
                    if field not in flow:
                        errors.append(f"Missing required field '{field}' in flow at index {i}")
                
                # Validate actions
                actions = flow.get("actions", [])
                if not isinstance(actions, list):
                    errors.append(f"Actions in flow '{flow.get('id', i)}' must be an array")
                else:
                    for j, action in enumerate(actions):
                        if not isinstance(action, dict):
                            errors.append(f"Action at index {j} in flow '{flow.get('id', i)}' must be an object")
                        else:
                            for field in ["id", "sourceId", "operationId"]:
                                if field not in action:
                                    errors.append(f"Missing required field '{field}' in action at index {j} in flow '{flow.get('id', i)}'")
                
                # Validate fields section
                fields = flow.get("fields", {})
                if "parameters" not in fields:
                    errors.append(f"Missing required field 'parameters' in fields section of flow '{flow.get('id', i)}'")
                
                if "responses" not in fields:
                    errors.append(f"Missing required field 'responses' in fields section of flow '{flow.get('id', i)}'")
                else:
                    responses = fields.get("responses", {})
                    if "success" not in responses:
                        errors.append(f"Missing required field 'success' in responses in flow '{flow.get('id', i)}'")
                
                # If links are present, validate them
                if "links" in flow:
                    links = flow.get("links", [])
                    if not isinstance(links, list):
                        errors.append(f"Links in flow '{flow.get('id', i)}' must be an array")
                    else:
                        for k, link in enumerate(links):
                            if not isinstance(link, dict):
                                errors.append(f"Link at index {k} in flow '{flow.get('id', i)}' must be an object")
                            else:
                                for field in ["origin", "target"]:
                                    if field not in link:
                                        errors.append(f"Missing required field '{field}' in link at index {k} in flow '{flow.get('id', i)}'")
                                
                                origin = link.get("origin", {})
                                target = link.get("target", {})
                                
                                for field in ["fieldPath", "actionId"]:
                                    if field not in origin:
                                        errors.append(f"Missing required field '{field}' in origin of link at index {k} in flow '{flow.get('id', i)}'")
                                    if field not in target:
                                        errors.append(f"Missing required field '{field}' in target of link at index {k} in flow '{flow.get('id', i)}'")
    
    return errors

def repair_schema(schema: Dict[str, Any], llm_client: Any, provider: str, model: str) -> Dict[str, Any]:
    """
    Repair an invalid schema to conform to the agents.json format.
    
    Args:
        schema: The invalid schema to repair
        llm_client: The LLM client to use for repair
        provider: The provider name (openai or anthropic)
        model: The model to use
        
    Returns:
        A repaired schema that conforms to the agents.json format
    """
    # Check if the schema is already valid
    validation_errors = get_schema_validation_errors(schema)
    if len(validation_errors) == 0:
        return schema
    
    # Prepare a detailed message about the errors
    error_message = "\n".join(validation_errors)
    
    # Create a prompt for the LLM to repair the schema
    system_prompt = """
    You are an expert at correcting JSON schemas. You will be given a JSON schema that needs to be fixed to match the required format.
    The schema should follow the agents.json format with the following requirements:

    1. Top-level fields must include: agentsJson, info, sources, and flows
    2. info must include: title, version, and description
    3. sources must be an array of objects, each with id and path
    4. flows must be an array of objects, each with:
       - id, title, description
       - actions: array of objects with id, sourceId, and operationId (not path/method)
       - fields: object with parameters and responses
       - links (optional): array of objects with origin and target, each with fieldPath and actionId

    Your task is to transform the schema to match this format while preserving as much of the original content as possible.
    The required format uses references (sourceId/operationId) instead of direct path/method specifications.

    Return only the fixed JSON schema with no additional explanation.
    """
    
    # Create a message with the schema and errors
    user_message = f"""
    The following schema has validation errors:

    {error_message}

    Here is the invalid schema:
    {json.dumps(schema, indent=2)}

    Please fix the schema to conform to the required format while preserving the functionality.
    Specifically, convert any direct path/method specifications in actions to the required sourceId/operationId reference pattern.
    """
    
    try:
        logger.info(f"Attempting to repair schema with {len(validation_errors)} validation errors")
        
        if provider == "openai":
            # Use OpenAI to repair the schema
            response = llm_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.2,
                max_tokens=8000,
                response_format={"type": "json_object"}
            )
            
            repaired_schema_str = response.choices[0].message.content
            
        elif provider == "anthropic":
            # Use Anthropic to repair the schema
            response = llm_client.messages.create(
                model=model,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_message}
                ],
                temperature=0.2,
                max_tokens=8000
            )
            
            content = response.content[0].text
            
            # Extract JSON from the response
            if "```json" in content:
                repaired_schema_str = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                repaired_schema_str = content.split("```")[1].strip()
            else:
                repaired_schema_str = content.strip()
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        
        # Parse the repaired schema
        repaired_schema = json.loads(repaired_schema_str)
        
        # Verify the repaired schema is valid
        new_validation_errors = get_schema_validation_errors(repaired_schema)
        if len(new_validation_errors) > 0:
            logger.warning(f"Repaired schema still has {len(new_validation_errors)} validation errors")
            logger.warning("\n".join(new_validation_errors))
            return schema  # Return the original if repair failed
        
        logger.info("Schema repaired successfully")
        return repaired_schema
        
    except Exception as e:
        logger.error(f"Error repairing schema: {e}")
        return schema  # Return the original if repair failed

def convert_to_action_service_format(schema: Dict[str, Any], collection_id: str) -> Dict[str, Any]:
    """
    Convert an OpenAPI schema to the format required by the AgentStable Search Action Service.
    
    Args:
        schema: The OpenAPI schema to convert
        collection_id: The ID of the collection to associate with the schema
        
    Returns:
        A dictionary in the format expected by the Search Action Service
    """
    # Start with the base structure expected by the Search Action Service
    action_service_schema = {
        "collection_id": collection_id,
        "schema": schema
    }
    
    # Extract sources from the schema
    sources = {}
    paths = schema.get("paths", {})
    
    for path, path_details in paths.items():
        # Skip paths that don't have operations
        if not path_details:
            continue
            
        # Use the path as source ID (without leading slash)
        source_id = path.lstrip("/").replace("/", "_")
        
        # Get all operations for this path
        operations = {}
        for method, operation_details in path_details.items():
            if method.lower() in ["get", "post", "put", "delete", "patch"]:
                # Use operation ID if available, otherwise generate one
                operation_id = operation_details.get("operationId")
                if not operation_id:
                    # Generate operation ID from method and path
                    operation_id = f"{method.lower()}_{source_id}"
                    
                operations[operation_id] = {
                    "method": method.upper(),
                    "path": path
                }
                
        # Add to sources if we have operations
        if operations:
            sources[source_id] = {
                "url": path,
                "operations": operations
            }
    
    # Add sources to the schema
    action_service_schema["sources"] = sources
    
    return action_service_schema


class ActionGenerator:
    """
    A class to help build action generator services.
    
    This class provides methods to convert natural language queries into
    properly formatted JSON schemas for actions. It handles the common tasks
    of validation, formatting, and integration with LLMs.
    """
    
    def __init__(
        self,
        llm_client: Any,
        schema_validator: Optional[Callable[[Dict[str, Any]], bool]] = None,
        provider: str = "generic",
        model: Optional[str] = None,
    ):
        """
        Initialize the ActionGenerator.
        
        Args:
            llm_client: The LLM client to use for generating schemas (e.g. OpenAI, Anthropic, etc.)
            schema_validator: Optional function to validate generated schemas
            provider: The LLM provider name for usage tracking
            model: The specific model name for usage tracking
        """
        self.llm_client = llm_client
        self.schema_validator = schema_validator
        self.provider = provider
        self.model = model
        self._usage_tracker = get_usage_tracker()
        
    def validate_schema(self, schema: Dict[str, Any]) -> bool:
        """
        Validate a generated schema.
        
        Args:
            schema: The schema to validate
            
        Returns:
            True if the schema is valid, False otherwise
        """
        if self.schema_validator:
            return self.schema_validator(schema)
            
        # Default to using the agents.json validator
        return agents_json_schema_validator(schema)
    
    def generate_from_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4000,
        temperature: float = 0.2,
        existing_schema: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate an action schema from a natural language query.
        
        This is a generic implementation that should be overridden by subclasses
        to implement provider-specific schema generation.
        
        Args:
            query: The natural language query to convert to a schema
            system_prompt: Optional system prompt to guide generation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            existing_schema: Optional existing schema to extend
            
        Returns:
            A dictionary containing the generated schema
        """
        raise NotImplementedError("This method should be implemented by a subclass")
    
    def track_usage(self, input_tokens: int, output_tokens: int) -> None:
        """
        Track token usage for schema generation.
        
        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
        """
        if not self._usage_tracker:
            return
            
        self._usage_tracker.add_record(
            provider=self.provider,
            model=self.model or "unknown",
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            metadata={"operation": "schema_generation"}
        )
    
    def format_schema(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Format a schema to ensure it conforms to the expected structure.
        
        Args:
            schema: The schema to format
            
        Returns:
            The formatted schema
        """
        # Ensure required agents.json fields are present
        if "agentsJson" not in schema:
            schema["agentsJson"] = "1.0.0"
            
        # Ensure info is present
        if "info" not in schema:
            schema["info"] = {
                "title": "Generated API",
                "version": "1.0.0",
                "description": "API schema generated from natural language"
            }
        elif isinstance(schema["info"], dict):
            info = schema["info"]
            if "title" not in info:
                info["title"] = "Generated API"
            if "version" not in info:
                info["version"] = "1.0.0"
            if "description" not in info:
                info["description"] = "API schema generated from natural language"
            
        # Ensure sources is a list
        if "sources" not in schema:
            schema["sources"] = []
            
        # Ensure flows is a list
        if "flows" not in schema:
            schema["flows"] = []
            
        return schema

    def convert_to_action_service(self, schema: Dict[str, Any], collection_id: str) -> Dict[str, Any]:
        """
        Convert a generated schema to the format required by the Search Action Service.
        
        Args:
            schema: The schema to convert
            collection_id: The ID of the collection to associate with the schema
            
        Returns:
            A dictionary in the format expected by the Search Action Service
        """
        return convert_to_action_service_format(schema, collection_id)

    def clarify_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> str:
        """
        Generate clarifying questions for the given query.
        
        This is a generic implementation that should be overridden by subclasses
        to implement provider-specific clarification generation.
        
        Args:
            query: The natural language query to clarify
            system_prompt: Optional system prompt to guide clarification
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            
        Returns:
            A string containing clarifying questions
        """
        raise NotImplementedError("This method should be implemented by a subclass")
    
    def generate_with_clarification(
        self,
        initial_query: str,
        clarification_response: Optional[str] = None,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4000,
        temperature: float = 0.2,
        existing_schema: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate an action schema with a clarification step.
        
        Args:
            initial_query: The initial natural language query
            clarification_response: Optional response to clarifying questions
            system_prompt: Optional system prompt to guide generation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            existing_schema: Optional existing schema to extend
            
        Returns:
            A dictionary containing the generated schema
        """
        if clarification_response:
            # Combine the initial query and clarification for schema generation
            combined_query = f"""
            Initial query: {initial_query}
            
            Clarifications provided:
            {clarification_response}
            """
            
            # Generate schema with the combined information
            return self.generate_from_query(
                query=combined_query,
                system_prompt=system_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                existing_schema=existing_schema
            )
        else:
            # If no clarification response provided, just use the initial query
            return self.generate_from_query(
                query=initial_query,
                system_prompt=system_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                existing_schema=existing_schema
            )

    def repair_schema_if_needed(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Repair a schema if it doesn't conform to the expected format.
        
        Args:
            schema: The schema to check and potentially repair
            
        Returns:
            The original schema if valid, or a repaired version if invalid
        """
        # Check if schema is valid
        validation_errors = get_schema_validation_errors(schema)
        if len(validation_errors) == 0:
            return schema
        
        # Log validation errors
        logger.warning(f"Schema validation failed with {len(validation_errors)} errors:")
        for error in validation_errors:
            logger.warning(f"  - {error}")
        
        # Attempt to repair the schema
        logger.info("Attempting to repair schema...")
        return repair_schema(schema, self.llm_client, self.provider, self.model)


class OpenAIActionGenerator(ActionGenerator):
    """Implementation of ActionGenerator for OpenAI."""
    
    def __init__(
        self,
        client: Any,
        model: str = "gpt-4-turbo-preview",
        schema_validator: Optional[Callable[[Dict[str, Any]], bool]] = None,
    ):
        """
        Initialize the OpenAI action generator.
        
        Args:
            client: The OpenAI client
            model: The OpenAI model to use
            schema_validator: Optional schema validator function
        """
        super().__init__(llm_client=client, schema_validator=schema_validator, provider="openai", model=model)
        self.model = model
        
    def generate_from_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4000,
        temperature: float = 0.2,
        existing_schema: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate an action schema from a natural language query using OpenAI.
        
        Args:
            query: The natural language query
            system_prompt: System prompt to guide generation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            existing_schema: Optional existing schema to extend
            
        Returns:
            A dictionary containing the generated schema
        """
        if system_prompt is None:
            system_prompt = (
                "You are an expert API designer. Your task is to convert natural language descriptions "
                "into API schemas that strictly follow the agents.json format. The schema must include:\n"
                "1. agentsJson: version string\n"
                "2. info: with title, version, and description\n"
                "3. sources: array of API sources with id and path\n"
                "4. flows: array of flows, each with id, title, description, actions, and fields\n"
                "5. Each flow must include actions, links (data connections), and fields (parameters and responses)\n\n"
                "Follow the agents.json schema format exactly. Return only valid JSON."
            )
            
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create an OpenAPI schema for the following: {query}"}
        ]
        
        if existing_schema:
            messages.append({
                "role": "user", 
                "content": f"Extend or modify this existing schema: {json.dumps(existing_schema, indent=2)}"
            })
            
        try:
            response = self.llm_client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                response_format={"type": "json_object"}
            )
            
            # Track usage
            if hasattr(response, "usage"):
                self.track_usage(
                    input_tokens=response.usage.prompt_tokens,
                    output_tokens=response.usage.completion_tokens
                )
                
            # Parse the response
            content = response.choices[0].message.content
            schema = json.loads(content)
            
            # Format and validate
            schema = self.format_schema(schema)
            valid = self.validate_schema(schema)
            
            if not valid:
                logger.warning("Generated schema failed validation, attempting repair...")
                schema = self.repair_schema_if_needed(schema)
                
            return schema
            
        except Exception as e:
            logger.error(f"Error generating schema with OpenAI: {e}")
            raise

    def clarify_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> str:
        """
        Generate clarifying questions for the given query using OpenAI.
        
        Args:
            query: The natural language query to clarify
            system_prompt: Optional system prompt to guide clarification
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            
        Returns:
            A string containing clarifying questions
        """
        if system_prompt is None:
            system_prompt = (
                "You are an expert API designer helping to create schemas in the agents.json format. "
                "Ask clarifying questions to gather information about the agents.json components:\n"
                "1. info: What should be the title, version, and description of the API?\n"
                "2. sources: What API sources need to be included? What are their IDs and paths?\n"
                "3. flows: What workflows should be supported? For each flow:\n"
                "   a. What actions (API operations) are needed?\n"
                "   b. What links between actions are required for data flow?\n"
                "   c. What parameters are needed for the flow?\n"
                "   d. What should the response format be?\n\n"
                "Ask 3-5 specific questions that will help you create a complete agents.json schema."
            )
            
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"I want to create an API for: {query}\n\nPlease ask me clarifying questions."}
        ]
        
        try:
            response = self.llm_client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Track usage
            if hasattr(response, "usage"):
                self.track_usage(
                    input_tokens=response.usage.prompt_tokens,
                    output_tokens=response.usage.completion_tokens
                )
                
            # Return the clarifying questions
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Error generating clarifying questions with OpenAI: {e}")
            raise


class AnthropicActionGenerator(ActionGenerator):
    """Implementation of ActionGenerator for Anthropic."""
    
    def __init__(
        self,
        client: Any,
        model: str = "claude-3-opus-20240229",
        schema_validator: Optional[Callable[[Dict[str, Any]], bool]] = None,
    ):
        """
        Initialize the Anthropic action generator.
        
        Args:
            client: The Anthropic client
            model: The Anthropic model to use
            schema_validator: Optional schema validator function
        """
        super().__init__(llm_client=client, schema_validator=schema_validator, provider="anthropic", model=model)
        self.model = model
        
    def generate_from_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 4000,
        temperature: float = 0.2,
        existing_schema: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate an action schema from a natural language query using Anthropic.
        
        Args:
            query: The natural language query
            system_prompt: Optional system prompt to guide generation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            existing_schema: Optional existing schema to extend
            
        Returns:
            A dictionary containing the generated schema
        """
        if system_prompt is None:
            system_prompt = (
                "You are an expert API designer. Your task is to convert natural language descriptions "
                "into API schemas that strictly follow the agents.json format. The schema must include:\n"
                "1. agentsJson: version string\n"
                "2. info: with title, version, and description\n"
                "3. sources: array of API sources with id and path\n"
                "4. flows: array of flows, each with id, title, description, actions, and fields\n"
                "5. Each flow must include actions, links (data connections), and fields (parameters and responses)\n\n"
                "Follow the agents.json schema format exactly. Return only valid JSON."
            )
            
        # Create messages - Anthropic expects system as a separate parameter, not as a message role
        messages = []
        
        if existing_schema:
            messages = [
                {"role": "user", "content": f"Create an OpenAPI schema for the following: {query}"},
                {"role": "user", "content": f"Extend or modify this existing schema: {json.dumps(existing_schema, indent=2)}"}
            ]
        else:
            messages = [
                {"role": "user", "content": f"Create an OpenAPI schema for the following: {query}"}
            ]
            
        try:
            response = self.llm_client.messages.create(
                model=self.model,
                system=system_prompt,  # Pass system prompt as a separate parameter
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Track usage
            if hasattr(response, "usage"):
                self.track_usage(
                    input_tokens=response.usage.input_tokens,
                    output_tokens=response.usage.output_tokens
                )
                
            # Parse the response
            content = response.content[0].text
            
            # Extract JSON from the response
            # Anthropic might wrap the JSON in markdown code blocks
            if "```json" in content:
                json_str = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                json_str = content.split("```")[1].strip()
            else:
                json_str = content.strip()
                
            schema = json.loads(json_str)
            
            # Format and validate
            schema = self.format_schema(schema)
            valid = self.validate_schema(schema)
            
            if not valid:
                logger.warning("Generated schema failed validation, attempting repair...")
                schema = self.repair_schema_if_needed(schema)
                
            return schema
            
        except Exception as e:
            logger.error(f"Error generating schema with Anthropic: {e}")
            raise 

    def clarify_query(
        self,
        query: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 1000,
        temperature: float = 0.7
    ) -> str:
        """
        Generate clarifying questions for the given query using Anthropic.
        
        Args:
            query: The natural language query to clarify
            system_prompt: Optional system prompt to guide clarification
            max_tokens: Maximum tokens to generate
            temperature: Temperature for generation
            
        Returns:
            A string containing clarifying questions
        """
        if system_prompt is None:
            system_prompt = (
                "You are an expert API designer helping to create schemas in the agents.json format. "
                "Ask clarifying questions to gather information about the agents.json components:\n"
                "1. info: What should be the title, version, and description of the API?\n"
                "2. sources: What API sources need to be included? What are their IDs and paths?\n"
                "3. flows: What workflows should be supported? For each flow:\n"
                "   a. What actions (API operations) are needed?\n"
                "   b. What links between actions are required for data flow?\n"
                "   c. What parameters are needed for the flow?\n"
                "   d. What should the response format be?\n\n"
                "Ask 3-5 specific questions that will help you create a complete agents.json schema."
            )
            
        # Create messages - Anthropic expects system as a separate parameter
        messages = [
            {"role": "user", "content": f"I want to create an API for: {query}\n\nPlease ask me clarifying questions."}
        ]
        
        try:
            response = self.llm_client.messages.create(
                model=self.model,
                system=system_prompt,  # Pass system prompt as a separate parameter
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Track usage
            if hasattr(response, "usage"):
                self.track_usage(
                    input_tokens=response.usage.input_tokens,
                    output_tokens=response.usage.output_tokens
                )
                
            # Return the clarifying questions
            if response.content and len(response.content) > 0:
                return response.content[0].text
            return "Could you provide more details about the API you want to create?"
            
        except Exception as e:
            logger.error(f"Error generating clarifying questions with Anthropic: {e}")
            raise 