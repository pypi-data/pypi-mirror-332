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
                metadata.input_schema[param_name] = {
                    "type": str(param_type),
                    "required": param.default == inspect.Parameter.empty
                }
                
                # Add default value if present
                if param.default != inspect.Parameter.empty:
                    metadata.input_schema[param_name]["default"] = param.default
        
        # Extract output schema from return type hint
        if "return" in type_hints:
            metadata.output_schema = {"type": str(type_hints["return"])}
        
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
    ) -> None:
        """
        Initialize a capability.
        
        Args:
            func: The function implementing the capability
            name: Optional name for the capability (defaults to function name)
            metadata: Optional metadata about the capability
            requires_agent: Whether the capability requires the agent instance as first arg
        """
        self.func = func
        self.name = name or func.__name__
        self.requires_agent = requires_agent
        self.metadata = metadata or CapabilityMetadata.from_function(func, self.name)
        
        # Create input validation model
        input_fields: Dict[str, Any] = {}
        for param_name, param_info in self.metadata.input_schema.items():
            # Skip 'self' parameter
            if param_name == "self":
                continue
                
            field_type = eval(param_info["type"]) if isinstance(param_info["type"], str) else param_info["type"]
            field_default = param_info.get("default", ... if param_info.get("required", True) else None)
            input_fields[param_name] = (field_type, field_default)
        
        self.input_model = create_model(f"{self.name}_inputs", **input_fields) if input_fields else None
    
    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the capability.
        
        This method handles validation of inputs and outputs, as well as
        error handling during capability execution.
        
        Args:
            *args: Positional arguments for the capability
            **kwargs: Keyword arguments for the capability
            
        Returns:
            The result of the capability execution
            
        Raises:
            ValueError: If input validation fails
            Exception: If capability execution fails
        """
        # Validate inputs if we have a model
        if self.input_model:
            try:
                # Convert kwargs to a dict for validation
                input_dict: Dict[str, Any] = {}
                for param_name in self.metadata.input_schema:
                    if param_name == "self":
                        continue
                        
                    # Get the value from kwargs or args
                    if param_name in kwargs:
                        input_dict[param_name] = kwargs[param_name]
                
                # Validate inputs
                validated_inputs = self.input_model(**input_dict)
                
                # Update kwargs with validated inputs
                for field_name, field_value in validated_inputs.model_dump().items():
                    kwargs[field_name] = field_value
                    
            except ValidationError as e:
                raise ValueError(f"Input validation failed for capability {self.name}: {str(e)}")
        
        # Execute the capability
        try:
            result = self.func(*args, **kwargs)
            
            # Handle coroutine functions
            if asyncio.iscoroutine(result):
                result = await result
                
            return result
            
        except Exception as e:
            logger.error(f"Error executing capability {self.name}: {str(e)}")
            raise
    
    @classmethod
    def register(
        cls,
        name: Optional[str] = None,
        **metadata: Any
    ) -> Callable[[CapabilityFunc], "Capability"]:
        """
        Decorator to register a function as a capability.
        
        Args:
            name: Optional name for the capability (defaults to function name)
            **metadata: Additional metadata for the capability
            
        Returns:
            Decorator function that wraps the capability function
        """
        def decorator(func: CapabilityFunc) -> Capability:
            # Extract parameters from function signature
            sig = inspect.signature(func)
            parameters = list(sig.parameters.values())
            
            # Check if first parameter is 'self', indicating a method
            requires_agent = len(parameters) > 0 and parameters[0].name == "self"
            
            # Create metadata from function and provided values
            capability_name = name or func.__name__
            capability_metadata = CapabilityMetadata.from_function(func, capability_name)
            
            # Update with provided metadata
            for key, value in metadata.items():
                if hasattr(capability_metadata, key):
                    setattr(capability_metadata, key, value)
                else:
                    capability_metadata.extra[key] = value
            
            # Create capability instance
            capability = cls(
                func=func,
                name=capability_name,
                metadata=capability_metadata,
                requires_agent=requires_agent
            )
            
            # Make the capability callable like the original function
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                return capability(*args, **kwargs)
            
            # Attach capability instance to wrapper
            setattr(wrapper, 'capability', capability)
            return cast(Capability, wrapper)
            
        return decorator


# Helper function to create capability from function
def create_capability(
    func: Callable[..., Any],
    name: Optional[str] = None,
    description: str = "",
    **metadata: Any
) -> Capability:
    """
    Create a capability from a function.
    
    Args:
        func: The function implementing the capability
        name: Optional name for the capability (defaults to function name)
        description: Optional description of the capability
        **metadata: Additional metadata for the capability
        
    Returns:
        Capability instance
    """
    capability_name = name or func.__name__
    
    # Create or update metadata
    if description:
        metadata["description"] = description
    
    # Create capability instance
    return Capability.register(capability_name, **metadata)(func)


# Default capabilities that can be used by any agent
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
        "capabilities": list(self.capabilities.keys())
    }


@Capability.register(name="get_state")
def get_agent_state(self: Any) -> Dict[str, Any]:
    """
    Get the current agent state.
    
    Returns:
        Dictionary with agent state
    """
    return {
        "agent_id": self.state.agent_id,
        "session_id": self.state.session_id,
        "created_at": self.state.created_at.isoformat(),
        "updated_at": self.state.updated_at.isoformat(),
        "context": self.state.context,
        "memory": self.state.memory
    } 