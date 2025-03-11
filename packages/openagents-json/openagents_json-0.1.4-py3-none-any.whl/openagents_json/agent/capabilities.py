"""
Capability system for OpenAgents JSON.

This module provides classes and utilities for managing agent capabilities,
including capability registration, execution, and validation.
"""

import asyncio
import functools
import inspect
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Type, TypeVar, Union, get_type_hints, cast

from pydantic import BaseModel, ValidationError, create_model

from openagents_json.agent.type_registry import serialize_type, deserialize_type

logger = logging.getLogger(__name__)

CapabilityFunc = TypeVar("CapabilityFunc", bound=Callable[..., Any])


@dataclass
class CapabilityMetadata:
    """Metadata for a capability."""
    
    name: str
    description: str = ""
    version: str = "0.1.0"
    author: str = ""
    tags: Set[str] = field(default_factory=set)
    examples: List[Dict[str, Any]] = field(default_factory=list)
    input_schema: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)
    agent_types: List[str] = field(default_factory=list)
    isolated_state: bool = False
    extra: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_function(cls, func: Callable[..., Any], name: Optional[str] = None) -> "CapabilityMetadata":
        """Extract metadata from a function's docstring and annotations."""
        metadata = cls(name=name or func.__name__)
        
        # Extract description from docstring
        if func.__doc__:
            metadata.description = inspect.cleandoc(func.__doc__).split("\n\n")[0]
        
        # Extract input schema from type hints
        type_hints = get_type_hints(func)
        for param_name, param in inspect.signature(func).parameters.items():
            # Skip 'self' parameter for methods
            if param_name == "self":
                continue
                
            if param_name in type_hints:
                param_type = type_hints[param_name]
                # Use serialize_type instead of str() for safe type serialization
                type_repr = serialize_type(param_type)
                metadata.input_schema[param_name] = {
                    "type": type_repr,
                    "required": param.default == inspect.Parameter.empty
                }
                
                # Add default value if present
                if param.default != inspect.Parameter.empty:
                    metadata.input_schema[param_name]["default"] = param.default
        
        # Extract output schema from return type hint
        if "return" in type_hints:
            # Use serialize_type for return type as well
            metadata.output_schema = {"type": serialize_type(type_hints["return"])}
        
        return metadata


class Capability:
    """
    Class for defining and executing agent capabilities.
    
    Capabilities are functions that agents can execute to perform specific tasks.
    They can be registered with agents and called by name.
    """
    
    def __init__(
        self,
        func: Callable[..., Any],
        name: Optional[str] = None,
        metadata: Optional[CapabilityMetadata] = None,
        requires_agent: bool = True,
        isolated_state: bool = False,
    ) -> None:
        """
        Initialize a capability.
        
        Args:
            func: The function implementing the capability
            name: Optional name for the capability (defaults to function name)
            metadata: Optional metadata about the capability
            requires_agent: Whether the capability requires the agent instance as first arg
            isolated_state: Whether to isolate state changes during execution
        """
        self.func = func
        self.name = name or func.__name__
        self.requires_agent = requires_agent
        self.isolated_state = isolated_state
        
        # Create metadata if not provided
        if metadata is None:
            metadata = CapabilityMetadata.from_function(func, self.name)
            
        # Update metadata with isolated_state
        metadata.isolated_state = isolated_state
        self.metadata = metadata
        
        # Create a wrapper function that preserves the original function's signature
        functools.update_wrapper(self, func)
    
    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the capability with the given arguments.
        
        Args:
            *args: Positional arguments to pass to the capability
            **kwargs: Keyword arguments to pass to the capability
            
        Returns:
            Result of the capability execution
        """
        # Check if we have an agent instance as the first argument
        agent = None
        if args and hasattr(args[0], "agent_id"):
            agent = args[0]
            
        # Handle state isolation if requested
        state_snapshot = None
        if self.isolated_state and agent and hasattr(agent, "get_state_snapshot"):
            try:
                # Create state snapshot before execution
                state_snapshot = agent.get_state_snapshot()
            except Exception as e:
                logger.warning(f"Failed to create state snapshot for capability {self.name}: {e}")
        
        try:
            # Execute the capability
            if asyncio.iscoroutinefunction(self.func):
                result = await self.func(*args, **kwargs)
            else:
                result = self.func(*args, **kwargs)
                
            return result
        except Exception as e:
            # Restore state snapshot on error if requested
            if self.isolated_state and agent and state_snapshot and hasattr(agent, "restore_from_snapshot"):
                try:
                    agent.restore_from_snapshot(state_snapshot)
                    logger.info(f"Restored state snapshot after error in capability {self.name}")
                except Exception as restore_error:
                    logger.error(f"Failed to restore state snapshot: {restore_error}")
            raise e
    
    @classmethod
    def register(
        cls,
        name: Optional[str] = None,
        isolated_state: bool = False,
        **metadata: Any
    ) -> Callable[[CapabilityFunc], "Capability"]:
        """
        Decorator for registering a function as a capability.
        
        Args:
            name: Optional name for the capability (defaults to function name)
            isolated_state: Whether to isolate state changes during execution
            **metadata: Additional metadata for the capability
            
        Returns:
            Decorator function that wraps the capability
        """
        def decorator(func: CapabilityFunc) -> Capability:
            # Extract parameters from function signature
            sig = inspect.signature(func)
            
            # Check if the first parameter is 'self' to determine if this is a method
            requires_agent = False
            params = list(sig.parameters.values())
            if params and params[0].name == "self":
                requires_agent = True
            
            # Create capability metadata
            capability_metadata = CapabilityMetadata(
                name=name or func.__name__,
                **metadata
            )
            
            # Create and return the capability
            capability = cls(
                func=func,
                name=name or func.__name__,
                metadata=capability_metadata,
                requires_agent=requires_agent,
                isolated_state=isolated_state,
            )
            
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                return capability(*args, **kwargs)
                
            # Attach the capability to the wrapper for introspection
            wrapper.capability = capability
            
            return wrapper
            
        return decorator


def create_capability(
    func: Callable[..., Any],
    name: Optional[str] = None,
    description: str = "",
    isolated_state: bool = False,
    **metadata: Any
) -> Capability:
    """
    Create a capability from a function.
    
    Args:
        func: Function implementing the capability
        name: Optional name for the capability (defaults to function name)
        description: Description of the capability
        isolated_state: Whether to isolate state changes during execution
        **metadata: Additional metadata for the capability
        
    Returns:
        Capability instance
    """
    # Create capability metadata
    capability_metadata = CapabilityMetadata(
        name=name or func.__name__,
        description=description,
        **metadata
    )
    
    # Check if the first parameter is 'self' to determine if this is a method
    sig = inspect.signature(func)
    requires_agent = False
    params = list(sig.parameters.values())
    if params and params[0].name == "self":
        requires_agent = True
    
    # Create and return the capability
    return Capability(
        func=func,
        name=name or func.__name__,
        metadata=capability_metadata,
        requires_agent=requires_agent,
        isolated_state=isolated_state,
    )


@Capability.register(name="get_info")
def get_agent_info(self: Any) -> Dict[str, Any]:
    """
    Get information about the agent.
    
    Returns:
        Dictionary with agent information
    """
    return {
        "name": self.name,
        "id": self.agent_id,
        "type": self.__class__.__name__,
        "capabilities": list(self.capabilities.keys()),
    }


@Capability.register(name="get_state")
def get_agent_state(self: Any) -> Dict[str, Any]:
    """
    Get the current state of the agent.
    
    Returns:
        Dictionary with agent state
    """
    if hasattr(self, "get_state_snapshot"):
        return self.get_state_snapshot()
    elif hasattr(self, "state"):
        return {"state": self.state}
    else:
        return {} 