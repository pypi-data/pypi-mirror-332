"""
Parallel execution module for AgentStable SDK.

This module provides functionality for executing actions, flows, and tasks in parallel.
"""

import asyncio
from typing import List, Dict, Any, Callable, Union, Optional


async def _execute_async(func, *args, **kwargs):
    """Execute a function asynchronously, handling both async and sync functions."""
    if asyncio.iscoroutinefunction(func):
        return await func(*args, **kwargs)
    else:
        return func(*args, **kwargs)


async def _execute_items_parallel(items, executor_func, *args, **kwargs):
    """Generic function to execute multiple items in parallel."""
    tasks = []
    for item in items:
        tasks.append(_execute_async(executor_func, item, *args, **kwargs))
    
    return await asyncio.gather(*tasks, return_exceptions=True)


def execute_actions_parallel(actions: List[Dict[str, Any]], 
                           executor_func: Callable, 
                           *args, **kwargs) -> List[Any]:
    """
    Execute a list of actions in parallel.
    
    Args:
        actions: List of action objects to execute
        executor_func: Function to execute for each action
        *args, **kwargs: Additional arguments to pass to the executor function
        
    Returns:
        List of results from executing each action
    """
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(_execute_items_parallel(actions, executor_func, *args, **kwargs))
    return results


def execute_flows_parallel(flows: List[Dict[str, Any]], 
                         executor_func: Callable, 
                         *args, **kwargs) -> List[Any]:
    """
    Execute a list of flows in parallel.
    
    Args:
        flows: List of flow objects to execute
        executor_func: Function to execute for each flow
        *args, **kwargs: Additional arguments to pass to the executor function
        
    Returns:
        List of results from executing each flow
    """
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(_execute_items_parallel(flows, executor_func, *args, **kwargs))
    return results


def execute_tasks_parallel(tasks: List[Callable], 
                         *args, **kwargs) -> List[Any]:
    """
    Execute a list of arbitrary tasks/functions in parallel.
    
    Args:
        tasks: List of functions to execute
        *args, **kwargs: Additional arguments to pass to all functions
        
    Returns:
        List of results from executing each task
    """
    async def run_tasks():
        tasks_coro = []
        for task_func in tasks:
            tasks_coro.append(_execute_async(task_func, *args, **kwargs))
        return await asyncio.gather(*tasks_coro, return_exceptions=True)
    
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(run_tasks())
    return results 