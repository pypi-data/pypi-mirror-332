"""
Streaming module for AgentStable SDK.

This module provides functions to stream responses from different LLM providers.
"""

from typing import Any, Dict, List, Optional, Union, Callable, Generator, Iterator
import json

from anthropic import Anthropic
from openai import OpenAI
from .usage import get_usage_tracker
from .memory import get_session


def stream_anthropic(
    client: Anthropic,
    messages: List[Dict[str, Any]],
    tools: Optional[List[Dict[str, Any]]] = None,
    model: str = "claude-3-sonnet-20240229",
    max_tokens: int = 4096,
    temperature: float = 0.7,
    callback: Optional[Callable[[str, str], None]] = None,
    session_id: Optional[str] = None
) -> Generator[Dict[str, Any], None, Dict[str, Any]]:
    """
    Stream a response from Anthropic.
    
    This function streams the response from Anthropic's API and captures token usage data 
    directly from the streaming response without making additional API calls.
    
    Token usage is tracked in two possible ways:
    1. Directly from the message_delta chunk's usage information (preferred method)
    2. By retrieving the complete message using the message ID after streaming is complete
    
    Args:
        client: The Anthropic client
        messages: List of messages for the conversation
        tools: Optional list of tools to provide to the model
        model: The model to use
        max_tokens: Maximum tokens to generate
        temperature: Temperature for response generation
        callback: Optional callback function that receives (content_type, content) for each chunk
        session_id: Optional session ID for token usage tracking
        
    Returns:
        A generator that yields chunks of the response and finally the complete response
    """
    # Store complete message parts
    full_response = {"content": []}
    current_text = ""
    current_block_type = None
    # For JSON collection
    json_parts = []
    assembled_json = ""
    
    # Get a session for tracking token usage
    session = get_session()
    usage_tracker = get_usage_tracker(session)
    
    print("[DEBUG STREAM] Starting Anthropic stream with model:", model)
    
    # Handle potentially None tools parameter
    kwargs = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    if tools:
        kwargs["tools"] = tools
        print(f"[DEBUG STREAM] Using tools: {len(tools)} tools")
    else:
        print("[DEBUG STREAM] No tools provided")
    
    # Start the streaming response
    try:
        print("[DEBUG STREAM] Creating stream...")
        with client.messages.stream(**kwargs) as stream:
            print("[DEBUG STREAM] Stream created, entering loop...")
            
            for chunk in stream:
                # Debug log the chunk type and structure
                chunk_type = getattr(chunk, "type", None)
                print(f"[DEBUG STREAM] Got chunk type: {chunk_type}")
                
                # Handle content block start (new blocks of content)
                if chunk_type == "content_block_start":
                    if hasattr(chunk, "content_block") and hasattr(chunk.content_block, "type"):
                        current_block_type = chunk.content_block.type
                        print(f"[DEBUG STREAM] Content block start: {current_block_type}")
                        
                        # Reset text for new text blocks
                        if current_block_type == "text":
                            current_text = ""
                        # Reset JSON parts for tool_use blocks
                        elif current_block_type == "tool_use":
                            json_parts = []
                            assembled_json = ""
                
                # Handle content block delta (text content)
                elif chunk_type == "content_block_delta":
                    delta_type = getattr(chunk.delta, "type", None)
                    print(f"[DEBUG STREAM] Delta type: {delta_type}")
                    
                    if delta_type == "text_delta" and hasattr(chunk.delta, "text"):
                        # Get the text content
                        text = chunk.delta.text
                        print(f"[DEBUG STREAM] Text delta: '{text}'")
                        
                        # Update the current text buffer
                        current_text += text
                        
                        # Update the response structure
                        text_block_exists = False
                        for block in full_response.get('content', []):
                            if block.get('type') == 'text':
                                block['text'] = current_text
                                text_block_exists = True
                                break
                        
                        if not text_block_exists:
                            full_response.setdefault('content', []).append({"type": "text", "text": current_text})
                        
                        # Call the callback with the text
                        if callback:
                            callback("text", text)
                        
                        # Yield the text to the caller
                        yield {"type": "text", "content": text}
                    
                    # Collect JSON for tool calls
                    elif delta_type == "input_json_delta" and hasattr(chunk.delta, "partial_json"):
                        partial_json = chunk.delta.partial_json
                        print(f"[DEBUG STREAM] JSON partial: {partial_json}")
                        
                        # Collect JSON parts
                        if partial_json and partial_json.strip():
                            json_parts.append(partial_json)
                            assembled_json += partial_json
                            print(f"[DEBUG STREAM] JSON parts collected: {len(json_parts)}")
                            print(f"[DEBUG STREAM] Assembled JSON so far: {assembled_json}")
                
                # Handle direct input_json chunks
                elif chunk_type == "input_json":
                    content = getattr(chunk, "content", "")
                    if content and content.strip():
                        print(f"[DEBUG STREAM] Direct JSON content: '{content}'")
                        json_parts.append(content)
                        assembled_json += content
                        
                        # Call the callback with the JSON content if available
                        if callback:
                            callback("input_json", content)
                        
                        # Yield the JSON content
                        yield {"type": "input_json", "content": content}
                
                # Handle text content directly
                elif chunk_type == "text" and hasattr(chunk, "text"):
                    text = chunk.text
                    print(f"[DEBUG STREAM] Direct text: '{text}'")
                    
                    # Update the current text buffer
                    current_text += text
                    
                    # Update the response structure
                    text_block_exists = False
                    for block in full_response.get('content', []):
                        if block.get('type') == 'text':
                            block['text'] = current_text
                            text_block_exists = True
                            break
                    
                    if not text_block_exists:
                        full_response.setdefault('content', []).append({"type": "text", "text": current_text})
                    
                    # Call the callback with the text
                    if callback:
                        callback("text", text)
                    
                    # Yield the text to the caller
                    yield {"type": "text", "content": text}
                
                # Handle complete tool use
                elif chunk_type == "tool_use":
                    tool_name = getattr(chunk, "name", "unknown")
                    tool_input = getattr(chunk, "input", {})
                    tool_id = getattr(chunk, "id", f"tool_{hash(str(tool_name))}")
                    
                    print(f"[DEBUG STREAM] TOOL USE: {tool_name}")
                    print(f"[DEBUG STREAM] TOOL INPUT: {tool_input}")
                    
                    # Create tool data
                    tool_data = {
                        "type": "tool_use",
                        "id": tool_id,
                        "name": tool_name,
                        "input": tool_input
                    }
                    
                    # Add to response
                    full_response.setdefault('content', []).append(tool_data)
                    
                    # Call callback
                    if callback:
                        callback_data = json.dumps({
                            "id": tool_id,
                            "name": tool_name,
                            "input": tool_input
                        })
                        callback("tool_use", callback_data)
                    
                    # Yield to caller
                    yield tool_data
                
                # Handle content block stop
                elif chunk_type == "content_block_stop":
                    if current_block_type == "text" and current_text:
                        print(f"[DEBUG STREAM] Content block stop for text: '{current_text[:50]}...'")
                        
                        # Ensure the text is in the response
                        text_block_exists = False
                        for block in full_response.get('content', []):
                            if block.get('type') == 'text':
                                block['text'] = current_text
                                text_block_exists = True
                                break
                        
                        if not text_block_exists:
                            full_response.setdefault('content', []).append({"type": "text", "text": current_text})
                    
                    # Handle tool_use block stop - try to assemble JSON tool use if available
                    elif current_block_type == "tool_use" and json_parts:
                        try:
                            # Join all parts and try to parse as JSON
                            json_str = "".join(json_parts).strip()
                            if not json_str:
                                continue
                                
                            # Clean up any stray characters that might interfere with JSON parsing
                            json_str = json_str.replace('\n', '').strip()
                            
                            print(f"[DEBUG STREAM] Attempting to parse tool JSON: {json_str}")
                            
                            # Try to parse as a complete JSON object
                            tool_input = json.loads(json_str)
                            
                            # Determine the tool name - assume it's the first tool if tools are provided
                            tool_name = tools[0]["name"] if tools and len(tools) > 0 else "unknown_tool"
                            
                            # Create the tool use object
                            tool_use = {
                                "type": "tool_use",
                                "id": f"tool_{hash(str(tool_input))}",
                                "name": tool_name,
                                "input": tool_input
                            }
                            
                            # Add to the response
                            print(f"[DEBUG STREAM] Adding assembled tool use to response: {tool_name}")
                            full_response.setdefault('content', []).append(tool_use)
                            
                            # Call the callback
                            if callback:
                                callback_data = json.dumps({
                                    "name": tool_name,
                                    "input": tool_input
                                })
                                callback("tool_use", callback_data)
                            
                            # Yield the tool use
                            yield tool_use
                        except json.JSONDecodeError as e:
                            print(f"[DEBUG STREAM] Failed to parse tool JSON: {e}")
                    
                    current_block_type = None
                
                # Handle message completion
                elif chunk_type == "message_delta" and hasattr(chunk, "delta") and hasattr(chunk.delta, "stop_reason"):
                    stop_reason = chunk.delta.stop_reason
                    print(f"[DEBUG STREAM] Message complete with stop_reason: {stop_reason}")
                    full_response["stop_reason"] = stop_reason
                    
                    # Handle usage information for token tracking
                    print("[DEBUG STREAM] Checking for usage information in message_delta chunk")
                    
                    # Dump the entire chunk structure for debugging
                    try:
                        import inspect
                        chunk_attrs = {attr: getattr(chunk, attr) for attr in dir(chunk) if not attr.startswith('_') and not inspect.ismethod(getattr(chunk, attr))}
                        print(f"[DEBUG STREAM] message_delta chunk structure: {chunk_attrs}")
                        
                        # Method 1: Check if usage is available directly on the chunk
                        if hasattr(chunk, "usage"):
                            print(f"[DEBUG STREAM] Found usage on chunk directly: {chunk.usage}")
                            output_tokens = getattr(chunk.usage, "output_tokens", 0)
                            input_tokens = 0  # We don't have this from streaming, will be estimated
                            
                            usage_data = {
                                "input_tokens": input_tokens,
                                "output_tokens": output_tokens,
                                "total_tokens": input_tokens + output_tokens,
                                "output_tokens_only": True  # Flag to indicate we only have output tokens
                            }
                            
                            print(f"[DEBUG STREAM] Got output token usage from streaming: {usage_data}")
                            full_response["usage"] = usage_data
                            
                            # We'll finalize this record once we estimate input tokens
                            # (Don't add to usage tracker yet)
                        
                        # Method 2: Check for usage field in the model_fields_set
                        elif hasattr(chunk, "model_fields_set") and "usage" in getattr(chunk, "model_fields_set", set()):
                            if hasattr(chunk, "usage"):
                                print(f"[DEBUG STREAM] Found usage in model_fields_set: {chunk.usage}")
                                output_tokens = getattr(chunk.usage, "output_tokens", 0)
                                input_tokens = 0  # We don't have this from streaming, will be estimated
                                
                                usage_data = {
                                    "input_tokens": input_tokens,
                                    "output_tokens": output_tokens,
                                    "total_tokens": input_tokens + output_tokens,
                                    "output_tokens_only": True  # Flag to indicate we only have output tokens
                                }
                                
                                print(f"[DEBUG STREAM] Got output token usage from streaming: {usage_data}")
                                full_response["usage"] = usage_data
                                
                                # We'll finalize this record once we estimate input tokens
                                # (Don't add to usage tracker yet)
                    except Exception as e:
                        print(f"[DEBUG STREAM] Error extracting usage information: {e}")
                
                # Handle final message
                elif chunk_type == "message_stop":
                    print("[DEBUG STREAM] Message stop received")
                    
                    # Get message ID if available - try different ways to access it
                    message_id = None
                    
                    # Method 1: Try to access message_id from stream directly
                    if hasattr(stream, "message_id"):
                        message_id = stream.message_id
                        print(f"[DEBUG STREAM] Found message_id from stream object: {message_id}")
                    
                    # Method 2: Try to access from the message object if available
                    elif hasattr(stream, "message") and hasattr(stream.message, "id"):
                        message_id = stream.message.id
                        print(f"[DEBUG STREAM] Found message_id from stream.message: {message_id}")
                    
                    # Method 3: Try to access from the last chunk if it has message info
                    elif hasattr(chunk, "message") and hasattr(chunk.message, "id"):
                        message_id = chunk.message.id
                        print(f"[DEBUG STREAM] Found message_id from chunk.message: {message_id}")
                        
                    # Method 4: Try to check if the chunk itself has an id
                    elif hasattr(chunk, "id"):
                        message_id = chunk.id
                        print(f"[DEBUG STREAM] Found message_id from chunk.id: {message_id}")
                        
                    if message_id:
                        # Store the message ID but don't try to retrieve it
                        # The Anthropic API doesn't support message retrieval in the current version
                        print(f"[DEBUG STREAM] Captured message ID: {message_id}")
                        full_response["message_id"] = message_id
            
            print("[DEBUG STREAM] Streaming complete")
            
            # One last check - if we have JSON parts but no tool use in the response, add it
            if json_parts and not any(block.get('type') == 'tool_use' for block in full_response.get('content', [])):
                try:
                    # Join all parts and try to parse as JSON
                    clean_json = assembled_json.replace('\n', '').strip()
                    
                    # Try to parse as a complete JSON object
                    tool_input = json.loads(clean_json)
                    
                    # Determine the tool name - assume it's the first tool if tools are provided
                    tool_name = tools[0]["name"] if tools and len(tools) > 0 else "unknown_tool"
                    
                    # Create the tool use object
                    tool_use = {
                        "type": "tool_use",
                        "id": f"final_tool_{hash(str(tool_input))}",
                        "name": tool_name,
                        "input": tool_input
                    }
                    
                    # Add to the response
                    print(f"[DEBUG STREAM] Adding final assembled tool use to response: {tool_name}")
                    full_response.setdefault('content', []).append(tool_use)
                    
                    # Call the callback
                    if callback:
                        callback_data = json.dumps({
                            "name": tool_name,
                            "input": tool_input
                        })
                        callback("tool_use", callback_data)
                except Exception as e:
                    print(f"[DEBUG STREAM] Error creating final tool use: {e}")
            
    except Exception as e:
        print(f"[DEBUG STREAM] Exception during streaming: {e}")
        import traceback
        traceback.print_exc()
    
    # Final check of the response
    print(f"[DEBUG STREAM] Final response keys: {list(full_response.keys())}")
    print(f"[DEBUG STREAM] Content blocks: {len(full_response.get('content', []))}")
    print(f"[DEBUG STREAM] JSON parts collected: {len(json_parts)}")
    
    # If we have text but it's not in the response, add it
    if current_text and not any(block.get('type') == 'text' for block in full_response.get('content', [])):
        print(f"[DEBUG STREAM] Adding missing text block: {current_text[:50]}...")
        full_response.setdefault('content', []).append({"type": "text", "text": current_text})
    
    # Finalize token usage tracking
    # If we already have partial usage (just output tokens), estimate input tokens
    if "usage" in full_response and full_response["usage"].get("output_tokens_only", False):
        try:
            # Estimate input tokens based on input messages (similar to how Anthropic counts them)
            input_text_length = 0
            for msg in messages:
                if isinstance(msg, dict) and "content" in msg:
                    if isinstance(msg["content"], str):
                        input_text_length += len(msg["content"])
                    elif isinstance(msg["content"], list):
                        for item in msg["content"]:
                            if isinstance(item, dict) and "text" in item:
                                input_text_length += len(item["text"])
            
            # Typical Anthropic token ratio is around 4 characters per token
            estimated_input_tokens = input_text_length // 4
            
            # Update usage data with estimated input tokens
            output_tokens = full_response["usage"]["output_tokens"]
            full_response["usage"]["input_tokens"] = estimated_input_tokens
            full_response["usage"]["total_tokens"] = estimated_input_tokens + output_tokens
            del full_response["usage"]["output_tokens_only"]  # Remove the flag
            
            print(f"[DEBUG STREAM] Updated token usage with estimated input tokens: {full_response['usage']}")
            
            # Add to usage tracker
            usage_tracker.add_record(
                provider="anthropic",
                model=model,
                input_tokens=estimated_input_tokens,
                output_tokens=output_tokens,
                session_id=session_id,
                metadata={"response_type": "streaming_with_estimated_input"}
            )
            
            # Call callback with usage
            if callback:
                callback("usage", json.dumps(full_response["usage"]))
            
            # Yield usage data
            yield {"type": "usage", "content": full_response["usage"]}
        except Exception as e:
            print(f"[DEBUG STREAM] Error estimating input tokens: {e}")
    
    # If we don't have any usage information from streaming, estimate both input and output tokens
    elif "usage" not in full_response:
        try:
            # Estimate input tokens
            input_text_length = 0
            for msg in messages:
                if isinstance(msg, dict) and "content" in msg:
                    if isinstance(msg["content"], str):
                        input_text_length += len(msg["content"])
                    elif isinstance(msg["content"], list):
                        for item in msg["content"]:
                            if isinstance(item, dict) and "text" in item:
                                input_text_length += len(item["text"])
            
            # Estimate output tokens from the generated text
            output_text_length = 0
            for block in full_response.get("content", []):
                if block.get("type") == "text" and "text" in block:
                    output_text_length += len(block["text"])
            
            # Typical Anthropic token ratio is around 4 characters per token
            estimated_input_tokens = input_text_length // 4
            estimated_output_tokens = output_text_length // 4
            
            estimated_usage = {
                "input_tokens": estimated_input_tokens,
                "output_tokens": estimated_output_tokens,
                "total_tokens": estimated_input_tokens + estimated_output_tokens,
                "is_estimated": True
            }
            
            full_response["usage"] = estimated_usage
            
            print(f"[DEBUG STREAM] Using fully estimated token usage: {estimated_usage}")
            
            # Add estimated usage to tracker
            usage_tracker.add_record(
                provider="anthropic",
                model=model,
                input_tokens=estimated_input_tokens,
                output_tokens=estimated_output_tokens,
                session_id=session_id,
                metadata={"response_type": "streaming_fully_estimated"}
            )
            
            # Call callback with usage
            if callback:
                callback("usage", json.dumps(estimated_usage))
            
            # Yield usage data
            yield {"type": "usage", "content": estimated_usage}
        except Exception as estimating_error:
            print(f"[DEBUG STREAM] Error fully estimating token usage: {estimating_error}")
    
    return full_response


def stream_openai(
    client: OpenAI,
    messages: List[Dict[str, Any]],
    tools: Optional[List[Dict[str, Any]]] = None,
    model: str = "gpt-4",
    max_tokens: int = 4096,
    temperature: float = 0.7,
    callback: Optional[Callable[[str, str], None]] = None,
    session_id: Optional[str] = None
) -> Generator[Dict[str, Any], None, Dict[str, Any]]:
    """
    Stream a response from OpenAI.
    
    Args:
        client: The OpenAI client
        messages: List of messages for the conversation
        tools: Optional list of tools to provide to the model
        model: The model to use
        max_tokens: Maximum tokens to generate
        temperature: Temperature for response generation
        callback: Optional callback function that receives (content_type, content) for each chunk
        session_id: Optional session ID for token usage tracking
        
    Returns:
        A generator that yields chunks of the response and finally the complete response
    """
    # Store the complete response
    full_response = {"content": []}
    current_text = ""
    tool_calls = []
    
    # Get a session for tracking token usage
    session = get_session()
    usage_tracker = get_usage_tracker(session)
    
    # Handle potentially None tools parameter
    kwargs = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": True
    }
    
    if tools:
        kwargs["tools"] = tools
        
    try:
        stream = client.chat.completions.create(**kwargs)
        
        complete_response = None
        response_id = None
        
        for chunk in stream:
            if not response_id and hasattr(chunk, "id"):
                response_id = chunk.id
                
            # Check if we have a delta
            if not hasattr(chunk.choices[0], "delta"):
                continue
                
            delta = chunk.choices[0].delta
            
            # Handle text content
            if hasattr(delta, "content") and delta.content:
                content = delta.content
                current_text += content
                
                # If we don't have a text block yet, add one
                if not full_response["content"] or full_response["content"][-1].get("type") != "text":
                    full_response["content"].append({"type": "text", "text": current_text})
                else:
                    # Update the existing text block
                    full_response["content"][-1]["text"] = current_text
                    
                # Call the callback if provided
                if callback:
                    callback("text", content)
                    
                yield {"type": "text", "content": content}
                
            # Handle tool calls
            if hasattr(delta, "tool_calls") and delta.tool_calls:
                for tool_call_delta in delta.tool_calls:
                    # Get the tool call index
                    index = tool_call_delta.index
                    
                    # Ensure we have enough tool calls
                    while len(tool_calls) <= index:
                        tool_calls.append({"id": "", "type": "function", "function": {"name": "", "arguments": ""}})
                        
                    # Update the tool call
                    if hasattr(tool_call_delta, "id") and tool_call_delta.id:
                        tool_calls[index]["id"] = tool_call_delta.id
                        
                    if hasattr(tool_call_delta, "function"):
                        if hasattr(tool_call_delta.function, "name") and tool_call_delta.function.name:
                            tool_calls[index]["function"]["name"] = tool_call_delta.function.name
                            
                        if hasattr(tool_call_delta.function, "arguments") and tool_call_delta.function.arguments:
                            tool_calls[index]["function"]["arguments"] += tool_call_delta.function.arguments
                            
                    # Update the full response with the tool calls
                    # First, remove any existing tool calls
                    full_response["content"] = [item for item in full_response["content"] if item.get("type") != "tool_calls"]
                    
                    # Add the updated tool calls
                    full_response["content"].append({"type": "tool_calls", "tool_calls": tool_calls})
                    
                    # Try to parse the arguments if they seem complete
                    for i, tool_call in enumerate(tool_calls):
                        if tool_call["function"]["arguments"]:
                            try:
                                args = json.loads(tool_call["function"]["arguments"])
                                
                                # Call the callback if provided
                                if callback:
                                    callback("tool_call", json.dumps({
                                        "name": tool_call["function"]["name"],
                                        "arguments": args
                                    }))
                                    
                                yield {
                                    "type": "tool_call", 
                                    "content": {
                                        "name": tool_call["function"]["name"],
                                        "arguments": args
                                    }
                                }
                            except json.JSONDecodeError:
                                # Arguments are not complete JSON yet
                                pass
            
            # Check if this is the last chunk
            if chunk.choices[0].finish_reason:
                finish_reason = chunk.choices[0].finish_reason
                full_response["finish_reason"] = finish_reason
                complete_response = chunk
                
        # Try to get usage information
        if response_id:
            try:
                complete_response = client.chat.completions.retrieve(response_id)
                if hasattr(complete_response, "usage"):
                    usage = complete_response.usage
                    usage_data = {
                        "prompt_tokens": usage.prompt_tokens,
                        "completion_tokens": usage.completion_tokens,
                        "total_tokens": usage.total_tokens
                    }
                    full_response["usage"] = usage_data
                    
                    # Add to usage tracker
                    usage_tracker.add_record(
                        provider="openai",
                        model=model,
                        input_tokens=usage_data["prompt_tokens"],
                        output_tokens=usage_data["completion_tokens"],
                        session_id=session_id,
                        metadata={"response_type": "streaming"}
                    )
                    
                    # Call callback with usage
                    if callback:
                        callback("usage", json.dumps(usage_data))
                        
                    yield {"type": "usage", "content": usage_data}
            except Exception as e:
                print(f"Error retrieving complete response: {e}")
                
    except Exception as e:
        print(f"Error during streaming: {e}")
        # Add error to the response
        full_response["error"] = str(e)
    
    return full_response 