"""
Parallel execution module for AgentStable SDK.

This module provides functionality for executing multiple actions or flows in parallel.
"""

import concurrent.futures
from typing import Any, Dict, List, Optional, Union, Callable
import json
import time

from .auth import Auth, NoAuth
from .execute import execute, execute_openai, execute_anthropic
from .memory import Session, get_session


def execute_actions_parallel(
    flow_response: Dict[str, Any],
    action_ids: List[str],
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    arguments: Optional[Dict[str, Any]] = None,
    max_workers: int = 5,
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute multiple actions from a flow in parallel.
    
    Args:
        flow_response: The response from the search action service
        action_ids: List of action IDs to execute in parallel
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None)
        arguments: Arguments to use for all actions (default: None)
        max_workers: Maximum number of concurrent workers (default: 5)
        session: Session object for context management (default: None)
        
    Returns:
        Dictionary containing the results of all parallel executions
    """
    if not auth:
        auth = NoAuth()
    
    if not session:
        session = get_session()
    
    if not arguments:
        arguments = {}
        
    # Extract the schema and flow ID
    schema = flow_response.get("schema", {})
    flow_id = flow_response.get("flow_id")
    
    if not schema or not flow_id:
        raise ValueError("Invalid flow response: missing schema or flow_id")
    
    # Find the flow in the schema
    flow = None
    for f in schema.get("flows", []):
        if f.get("id") == flow_id:
            flow = f
            break
    
    if not flow:
        raise ValueError(f"Flow with ID '{flow_id}' not found in schema")
    
    # Get all actions from the flow
    all_actions = flow.get("actions", [])
    if not all_actions:
        raise ValueError(f"No actions defined in flow '{flow_id}'")
    
    # Filter actions to execute
    actions_to_execute = []
    for action in all_actions:
        action_id = action.get("id")
        if action_id in action_ids:
            actions_to_execute.append(action)
    
    if not actions_to_execute:
        raise ValueError(f"None of the specified action IDs were found in flow '{flow_id}'")
    
    # Execute actions in parallel
    results = {}
    
    # Prepare a partial flow for each action
    action_flows = []
    for action in actions_to_execute:
        # Create a single-action flow for each action
        action_flow = {
            "flow_id": flow_id,
            "schema": schema,
            "single_action": action.get("id")
        }
        action_flows.append((action.get("id"), action_flow))
    
    # Define the worker function to execute a single action
    def execute_single_action(action_data):
        action_id, action_flow = action_data
        try:
            # Enhance arguments with context for this action
            action_args = arguments.copy()
            context = session.get_all_context(flow_id)
            for key, value in context.items():
                if key not in action_args:
                    action_args[key] = value
            
            # Create a dummy tool call response for this action
            dummy_response = {
                "tool_calls": [
                    {
                        "id": f"call_{action_id}",
                        "name": flow_id,
                        "arguments": json.dumps(action_args)
                    }
                ]
            }
            
            # Execute just this action
            result = execute(
                flow_response=action_flow,
                llm_response=dummy_response,
                auth=auth,
                base_url=base_url,
                session=session
            )
            
            return action_id, result
        except Exception as e:
            return action_id, {"error": str(e)}
    
    # Execute actions in parallel using ThreadPoolExecutor
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(execute_single_action, action_data) for action_data in action_flows]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                action_id, result = future.result()
                results[action_id] = result
            except Exception as e:
                print(f"Exception while executing parallel action: {e}")
    
    execution_time = time.time() - start_time
    
    # Store the results in the session
    session.set_context("parallel_action_results", results, flow_id)
    session.set_context("parallel_execution_time", execution_time, flow_id)
    
    return {
        "flow_id": flow_id,
        "parallel_results": results,
        "execution_time": execution_time
    }


def execute_flows_parallel(
    flow_responses: List[Dict[str, Any]],
    llm_responses: List[Any],
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    provider: str = "openai",
    max_workers: int = 3,
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute multiple flows in parallel.
    
    Args:
        flow_responses: List of responses from the search action service
        llm_responses: List of responses from LLM APIs
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None)
        provider: The LLM provider, either "openai" or "anthropic" (default: "openai")
        max_workers: Maximum number of concurrent workers (default: 3)
        session: Session object for context management (default: None)
        
    Returns:
        Dictionary containing the results of all parallel flow executions
    """
    if not auth:
        auth = NoAuth()
    
    if not session:
        session = get_session()
    
    if len(flow_responses) != len(llm_responses):
        raise ValueError("The number of flow responses must match the number of LLM responses")
    
    # Define the worker function to execute a single flow
    def execute_single_flow(flow_data):
        flow_idx, (flow_response, llm_response) = flow_data
        flow_id = flow_response.get("flow_id", f"flow_{flow_idx}")
        
        try:
            # Choose the correct execution function based on provider
            if provider.lower() == "openai":
                result = execute_openai(
                    flow_response=flow_response,
                    openai_response=llm_response,
                    auth=auth,
                    base_url=base_url,
                    session=session
                )
            elif provider.lower() == "anthropic":
                result = execute_anthropic(
                    flow_response=flow_response,
                    anthropic_response=llm_response,
                    auth=auth,
                    base_url=base_url,
                    session=session
                )
            else:
                raise ValueError(f"Unsupported provider: {provider}")
            
            return flow_id, result
        except Exception as e:
            return flow_id, {"error": str(e)}
    
    # Execute flows in parallel using ThreadPoolExecutor
    results = {}
    start_time = time.time()
    
    flow_data = list(enumerate(zip(flow_responses, llm_responses)))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(execute_single_flow, data) for data in flow_data]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                flow_id, result = future.result()
                results[flow_id] = result
            except Exception as e:
                print(f"Exception while executing parallel flow: {e}")
    
    execution_time = time.time() - start_time
    
    # Store the results in the session
    session.set_context("parallel_flow_results", results, "parallel_execution")
    session.set_context("parallel_execution_time", execution_time, "parallel_execution")
    
    return {
        "parallel_results": results,
        "execution_time": execution_time
    }


def execute_tasks_parallel(
    tasks: List[Dict[str, Any]],
    auth: Optional[Auth] = None,
    base_url: Optional[str] = None,
    max_workers: int = 5,
    session: Optional[Session] = None
) -> Dict[str, Any]:
    """
    Execute a list of arbitrary tasks in parallel.
    
    Args:
        tasks: List of task definitions, each with a function and arguments
        auth: Authentication method to use (default: None)
        base_url: Base URL for API calls (default: None)
        max_workers: Maximum number of concurrent workers (default: 5)
        session: Session object for context management (default: None)
        
    Returns:
        Dictionary containing the results of all parallel task executions
    """
    if not auth:
        auth = NoAuth()
    
    if not session:
        session = get_session()
    
    # Define the worker function to execute a single task
    def execute_single_task(task_data):
        task_idx, task = task_data
        task_id = task.get("id", f"task_{task_idx}")
        func = task.get("function")
        args = task.get("args", {})
        
        try:
            if not callable(func):
                raise ValueError(f"Task {task_id} does not have a callable function")
            
            # Execute the function with the provided arguments
            result = func(**args)
            return task_id, result
        except Exception as e:
            return task_id, {"error": str(e)}
    
    # Execute tasks in parallel using ThreadPoolExecutor
    results = {}
    start_time = time.time()
    
    task_data = list(enumerate(tasks))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(execute_single_task, data) for data in task_data]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                task_id, result = future.result()
                results[task_id] = result
            except Exception as e:
                print(f"Exception while executing parallel task: {e}")
    
    execution_time = time.time() - start_time
    
    # Store the results in the session
    session.set_context("parallel_task_results", results, "parallel_execution")
    session.set_context("parallel_execution_time", execution_time, "parallel_execution")
    
    return {
        "parallel_results": results,
        "execution_time": execution_time
    } 