"""
Enhanced decorators for OpenAgents JSON.

This module provides enhanced decorators for registering agents, capabilities, and tools
with improved metadata extraction, type preservation, and schema generation.
"""

import functools
import inspect
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import (
    Annotated,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Set,
    Type,
    TypeVar,
    Union,
    get_type_hints,
)

# Type variables for preserving types in decorators
AgentType = TypeVar("AgentType", bound=Type[Any])
CapabilityFunc = TypeVar("CapabilityFunc", bound=Callable[..., Any])
ToolFunc = TypeVar("ToolFunc", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


@dataclass
class Example:
    """Example for a capability or tool."""

    inputs: Dict[str, Any]
    outputs: Optional[Any] = None
    description: Optional[str] = None


@dataclass
class ComponentConfig:
    """Base configuration for any component."""

    name: str
    version: str = "0.1.0"
    description: str = ""
    author: str = ""
    tags: Set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    examples: List[Example] = field(default_factory=list)
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_component(
        cls, component: Any, name: str, metadata: Dict[str, Any]
    ) -> "ComponentConfig":
        """Extract metadata from a component and combine with provided metadata."""
        config = cls(name=name)

        # Extract description from docstring
        if component.__doc__:
            config.description = inspect.cleandoc(component.__doc__).split("\n\n")[0]

        # Update with provided metadata
        for key, value in metadata.items():
            if hasattr(config, key):
                setattr(config, key, value)
            else:
                config.extra[key] = value

        return config


@dataclass
class AgentConfig(ComponentConfig):
    """Configuration for an agent."""

    model: Optional[str] = None
    capabilities: Dict[str, Dict[str, Any]] = field(default_factory=dict)


@dataclass
class CapabilityConfig(ComponentConfig):
    """Configuration for a capability."""

    agent_name: Optional[str] = None
    input_schema: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolConfig(ComponentConfig):
    """Configuration for a tool."""

    input_schema: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)


def extract_schema_from_function(
    func: Callable,
) -> tuple[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    """Extract input and output schema from a function's type hints."""
    type_hints = get_type_hints(func)

    # Extract input parameters from signature
    signature = inspect.signature(func)
    input_schema = {}

    for param_name, param in signature.parameters.items():
        # Skip self, cls, and context parameters
        if param_name in ("self", "cls", "context"):
            continue

        param_info = {
            "type": str(type_hints.get(param_name, Any).__name__),
            "required": param.default == inspect.Parameter.empty,
        }

        # Add default value if present
        if param.default != inspect.Parameter.empty:
            param_info["default"] = param.default

        input_schema[param_name] = param_info

    # Extract return type
    output_type = type_hints.get("return", Any).__name__
    # Normalize type names
    if output_type == "Dict":
        output_type = "dict"
    elif output_type == "List":
        output_type = "list"

    output_schema = {"type": output_type}

    return input_schema, output_schema


def create_agent_decorator(registry):
    """Create an enhanced agent decorator using the provided registry."""

    def agent(name: str, **metadata) -> Callable[[AgentType], AgentType]:
        """
        Enhanced decorator to register an agent class or function.

        Args:
            name: Name of the agent
            **metadata: Additional metadata for the agent
                version: Version of the agent
                description: Description of the agent
                author: Author of the agent
                tags: Tags for the agent
                model: Default model for the agent
                examples: Examples for the agent

        Returns:
            Decorator function
        """

        def decorator(cls_or_func: AgentType) -> AgentType:
            # Extract metadata and create configuration
            config = AgentConfig.from_component(cls_or_func, name, metadata)

            # Register agent
            registry.register_agent(name, cls_or_func, config.__dict__)

            # For classes, store the class reference for capability registration
            if inspect.isclass(cls_or_func):
                decorator.cls = cls_or_func

            # Preserve function attributes like __name__, __doc__, etc.
            @functools.wraps(cls_or_func)
            def wrapper(*args, **kwargs):
                return cls_or_func(*args, **kwargs)

            # For classes, return the original class
            if inspect.isclass(cls_or_func):
                return cls_or_func

            # For functions, return the wrapped function with the original reference
            wrapper.__original__ = cls_or_func
            return wrapper

        decorator.cls = None
        return decorator

    return agent


def create_capability_decorator(registry):
    """Create an enhanced capability decorator using the provided registry."""

    def capability(name: str, **metadata) -> Callable[[CapabilityFunc], CapabilityFunc]:
        """
        Enhanced decorator to register an agent capability.

        Args:
            name: Name of the capability
            **metadata: Additional metadata for the capability
                version: Version of the capability
                description: Description of the capability
                examples: Examples for the capability
                input_schema: Override for automatically extracted input schema
                output_schema: Override for automatically extracted output schema

        Returns:
            Decorator function
        """

        def decorator(func: CapabilityFunc) -> CapabilityFunc:
            # Extract input and output schema from function
            input_schema, output_schema = extract_schema_from_function(func)

            # Override with provided schema if specified
            if "input_schema" in metadata:
                input_schema = metadata.pop("input_schema")
            if "output_schema" in metadata:
                output_schema = metadata.pop("output_schema")

            # Create configuration
            config = CapabilityConfig.from_component(func, name, metadata)
            config.input_schema = input_schema
            config.output_schema = output_schema

            # Find parent decorator to get agent class
            frame = inspect.currentframe()
            try:
                if frame and frame.f_back:
                    # Get the parent frame's locals
                    parent_locals = frame.f_back.f_locals
                    # Try to get the decorator object that was called
                    agent_decorator = parent_locals.get("self")
                    if agent_decorator and hasattr(agent_decorator, "cls"):
                        for agent_name, agent_info in registry.agents.items():
                            if agent_info["cls"] == agent_decorator.cls:
                                config.agent_name = agent_name
                                registry.register_capability(
                                    agent_name, name, func, config.__dict__
                                )
                                break
                    # Traditional frame-based method as fallback
                    if not config.agent_name and "cls" in parent_locals:
                        for agent_name, agent_info in registry.agents.items():
                            if agent_info["cls"] == parent_locals.get("cls"):
                                config.agent_name = agent_name
                                registry.register_capability(
                                    agent_name, name, func, config.__dict__
                                )
                                break
            finally:
                del frame  # Avoid reference cycles

            # Preserve function attributes
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    return capability


def create_tool_decorator(registry):
    """Create an enhanced tool decorator using the provided registry."""

    def tool(name: str, **metadata) -> Callable[[ToolFunc], ToolFunc]:
        """
        Enhanced decorator to register a standalone tool.

        Args:
            name: Name of the tool
            **metadata: Additional metadata for the tool
                version: Version of the tool
                description: Description of the tool
                examples: Examples for the tool
                input_schema: Override for automatically extracted input schema
                output_schema: Override for automatically extracted output schema

        Returns:
            Decorator function
        """

        def decorator(func: ToolFunc) -> ToolFunc:
            # Extract input and output schema from function
            input_schema, output_schema = extract_schema_from_function(func)

            # Override with provided schema if specified
            if "input_schema" in metadata:
                input_schema = metadata.pop("input_schema")
            if "output_schema" in metadata:
                output_schema = metadata.pop("output_schema")

            # Create configuration
            config = ToolConfig.from_component(func, name, metadata)
            config.input_schema = input_schema
            config.output_schema = output_schema

            # Register tool
            registry.register_tool(name, func, config.__dict__)

            # Preserve function attributes
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            # Store original function reference
            wrapper.__original__ = func
            return wrapper

        return decorator

    return tool
