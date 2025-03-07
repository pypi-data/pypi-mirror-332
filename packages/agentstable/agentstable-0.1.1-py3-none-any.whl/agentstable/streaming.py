"""
Streaming module for AgentStable SDK.

This module provides functions to stream responses from different LLM providers.
"""

from typing import Any, Dict, List, Optional, Union, Callable, Generator, Iterator
import json

from anthropic import Anthropic
from openai import OpenAI


def stream_anthropic(
    client: Anthropic,
    messages: List[Dict[str, Any]],
    tools: Optional[List[Dict[str, Any]]] = None,
    model: str = "claude-3-sonnet-20240229",
    max_tokens: int = 4096,
    temperature: float = 0.7,
    callback: Optional[Callable[[str, str], None]] = None
) -> Generator[Dict[str, Any], None, Dict[str, Any]]:
    """
    Stream a response from Anthropic.
    
    Args:
        client: The Anthropic client
        messages: List of messages for the conversation
        tools: Optional list of tools to provide to the model
        model: The model to use
        max_tokens: Maximum tokens to generate
        temperature: Temperature for response generation
        callback: Optional callback function that receives (content_type, content) for each chunk
        
    Returns:
        A generator that yields chunks of the response and finally the complete response
    """
    # Store complete message parts
    full_response = {"content": []}
    current_text = ""
    
    # Start the streaming response
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=messages,
        tools=tools
    ) as stream:
        for chunk in stream:
            if chunk.type == "content_block_delta":
                if chunk.delta.type == "text":
                    # For text content
                    if current_text == "" and chunk.delta.text != "":
                        # Start of a new text block
                        current_text = chunk.delta.text
                        full_response["content"].append({"type": "text", "text": current_text})
                    else:
                        # Continuing a text block
                        current_text += chunk.delta.text
                        # Update the last block
                        if full_response["content"] and full_response["content"][-1]["type"] == "text":
                            full_response["content"][-1]["text"] = current_text
                    
                    if callback:
                        callback("text", chunk.delta.text)
                    
                    yield {"type": "text", "content": chunk.delta.text}
                    
            elif chunk.type == "tool_use":
                # Tool use is complete in one chunk
                tool_data = {
                    "type": "tool_use",
                    "id": chunk.id,
                    "name": chunk.name,
                    "input": chunk.input
                }
                
                full_response["content"].append({
                    "type": "tool_use",
                    "id": chunk.id,
                    "name": chunk.name,
                    "input": chunk.input
                })
                
                if callback:
                    callback("tool_use", json.dumps({
                        "name": chunk.name,
                        "input": chunk.input
                    }))
                
                yield tool_data
            
            elif chunk.type == "message_delta" and hasattr(chunk.delta, "stop_reason"):
                # End of the message
                full_response["stop_reason"] = chunk.delta.stop_reason
    
    # Return the complete response for further processing
    return full_response


def stream_openai(
    client: OpenAI,
    messages: List[Dict[str, Any]],
    tools: Optional[List[Dict[str, Any]]] = None,
    model: str = "gpt-4o",
    temperature: float = 0.7,
    callback: Optional[Callable[[str, str], None]] = None
) -> Generator[Dict[str, Any], None, Dict[str, Any]]:
    """
    Stream a response from OpenAI.
    
    Args:
        client: The OpenAI client
        messages: List of messages for the conversation
        tools: Optional list of tools to provide to the model
        model: The model to use
        temperature: Temperature for response generation
        callback: Optional callback function that receives (content_type, content) for each chunk
        
    Returns:
        A generator that yields chunks of the response and finally the complete response
    """
    # Store complete message parts
    full_response = {"choices": [{"message": {"content": "", "tool_calls": []}}]}
    current_text = ""
    current_tool_calls = {}
    
    # Create parameters for the API call
    params = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": True
    }
    
    if tools:
        params["tools"] = tools
        params["tool_choice"] = "auto"
    
    # Start the streaming response
    stream = client.chat.completions.create(**params)
    
    for chunk in stream:
        delta = chunk.choices[0].delta
        
        # Handle text content
        if delta.content is not None:
            current_text += delta.content
            full_response["choices"][0]["message"]["content"] = current_text
            
            if callback:
                callback("text", delta.content)
                
            yield {"type": "text", "content": delta.content}
        
        # Handle tool calls
        if delta.tool_calls:
            for tool_delta in delta.tool_calls:
                tool_id = tool_delta.index
                
                # Initialize tool if it's new
                if tool_id not in current_tool_calls:
                    current_tool_calls[tool_id] = {
                        "id": f"tool_{tool_id}",
                        "type": "function",
                        "function": {"name": "", "arguments": ""}
                    }
                
                # Update function name if provided
                if hasattr(tool_delta, "function") and hasattr(tool_delta.function, "name"):
                    current_tool_calls[tool_id]["function"]["name"] += tool_delta.function.name
                
                # Update function arguments if provided
                if hasattr(tool_delta, "function") and hasattr(tool_delta.function, "arguments"):
                    current_tool_calls[tool_id]["function"]["arguments"] += tool_delta.function.arguments
                
                # If this is the final chunk, add the tool call to the response
                if tool_delta.function.arguments:
                    if callback:
                        callback("tool_use", json.dumps({
                            "name": current_tool_calls[tool_id]["function"]["name"],
                            "arguments": current_tool_calls[tool_id]["function"]["arguments"]
                        }))
                    
                    yield {
                        "type": "tool_use",
                        "id": current_tool_calls[tool_id]["id"],
                        "name": current_tool_calls[tool_id]["function"]["name"],
                        "arguments": current_tool_calls[tool_id]["function"]["arguments"]
                    }
    
    # Update the full response with the completed tool calls
    full_response["choices"][0]["message"]["tool_calls"] = list(current_tool_calls.values())
    
    # Return the complete response for further processing
    return full_response 