"""
Tool system for OpenAgents JSON.

This module provides classes and utilities for defining and using tools with agents,
including tool registration, execution, and validation.
"""

import asyncio
import functools
import inspect
import logging
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Type, TypeVar, Union, get_type_hints, cast

from pydantic import BaseModel, ValidationError, create_model

logger = logging.getLogger(__name__)

ToolFunc = TypeVar("ToolFunc", bound=Callable[..., Any])


@dataclass
class ToolMetadata:
    """Metadata for a tool."""
    
    name: str
    description: str = ""
    version: str = "0.1.0"
    author: str = ""
    tags: Set[str] = field(default_factory=set)
    examples: List[Dict[str, Any]] = field(default_factory=list)
    input_schema: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)
    category: str = "general"
    extra: Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_function(cls, func: Callable[..., Any], name: Optional[str] = None) -> "ToolMetadata":
        """Extract metadata from a function's docstring and annotations."""
        metadata = cls(name=name or func.__name__)
        
        # Extract description from docstring
        if func.__doc__:
            metadata.description = inspect.cleandoc(func.__doc__).split("\n\n")[0]
        
        # Extract input schema from type hints
        type_hints = get_type_hints(func)
        for param_name, param in inspect.signature(func).parameters.items():
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


class Tool:
    """
    Class for defining and executing tools.
    
    Tools are standalone functions that can be called by agents to perform
    specific tasks, such as making API calls, processing data, or interacting
    with external systems.
    """
    
    def __init__(
        self,
        func: Callable[..., Any],
        name: Optional[str] = None,
        metadata: Optional[ToolMetadata] = None,
    ) -> None:
        """
        Initialize a tool.
        
        Args:
            func: The function implementing the tool
            name: Optional name for the tool (defaults to function name)
            metadata: Optional metadata about the tool
        """
        self.func = func
        self.name = name or func.__name__
        self.metadata = metadata or ToolMetadata.from_function(func, self.name)
        
        # Create input validation model
        input_fields: Dict[str, Any] = {}
        for param_name, param_info in self.metadata.input_schema.items():
            field_type = eval(param_info["type"]) if isinstance(param_info["type"], str) else param_info["type"]
            field_default = param_info.get("default", ... if param_info.get("required", True) else None)
            input_fields[param_name] = (field_type, field_default)
        
        self.input_model = create_model(f"{self.name}_inputs", **input_fields) if input_fields else None
    
    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the tool.
        
        This method handles validation of inputs and outputs, as well as
        error handling during tool execution.
        
        Args:
            *args: Positional arguments for the tool
            **kwargs: Keyword arguments for the tool
            
        Returns:
            The result of the tool execution
            
        Raises:
            ValueError: If input validation fails
            Exception: If tool execution fails
        """
        # Validate inputs if we have a model
        if self.input_model:
            try:
                # Convert kwargs to a dict for validation
                input_dict: Dict[str, Any] = {}
                for param_name in self.metadata.input_schema:
                    # Get the value from kwargs or args
                    if param_name in kwargs:
                        input_dict[param_name] = kwargs[param_name]
                
                # Validate inputs
                validated_inputs = self.input_model(**input_dict)
                
                # Update kwargs with validated inputs
                for field_name, field_value in validated_inputs.model_dump().items():
                    kwargs[field_name] = field_value
                    
            except ValidationError as e:
                raise ValueError(f"Input validation failed for tool {self.name}: {str(e)}")
        
        # Execute the tool
        try:
            result = self.func(*args, **kwargs)
            
            # Handle coroutine functions
            if asyncio.iscoroutine(result):
                result = await result
                
            return result
            
        except Exception as e:
            logger.error(f"Error executing tool {self.name}: {str(e)}")
            raise
    
    @classmethod
    def register(
        cls,
        name: Optional[str] = None,
        **metadata: Any
    ) -> Callable[[ToolFunc], "Tool"]:
        """
        Decorator to register a function as a tool.
        
        Args:
            name: Optional name for the tool (defaults to function name)
            **metadata: Additional metadata for the tool
            
        Returns:
            Decorator function that wraps the tool function
        """
        def decorator(func: ToolFunc) -> Tool:
            # Create metadata from function and provided values
            tool_name = name or func.__name__
            tool_metadata = ToolMetadata.from_function(func, tool_name)
            
            # Update with provided metadata
            for key, value in metadata.items():
                if hasattr(tool_metadata, key):
                    setattr(tool_metadata, key, value)
                else:
                    tool_metadata.extra[key] = value
            
            # Create tool instance
            tool = cls(
                func=func,
                name=tool_name,
                metadata=tool_metadata
            )
            
            # Make the tool callable like the original function
            @functools.wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                return tool(*args, **kwargs)
            
            # Attach tool instance to wrapper
            setattr(wrapper, 'tool', tool)
            return cast(Tool, wrapper)
            
        return decorator


# Helper function to create tool from function
def create_tool(
    func: Callable[..., Any],
    name: Optional[str] = None,
    description: str = "",
    **metadata: Any
) -> Tool:
    """
    Create a tool from a function.
    
    Args:
        func: The function implementing the tool
        name: Optional name for the tool (defaults to function name)
        description: Optional description of the tool
        **metadata: Additional metadata for the tool
        
    Returns:
        Tool instance
    """
    tool_name = name or func.__name__
    
    # Create or update metadata
    if description:
        metadata["description"] = description
    
    # Create tool instance
    return Tool.register(tool_name, **metadata)(func)


class ToolRegistry:
    """Registry for managing and accessing tools."""
    
    def __init__(self) -> None:
        """Initialize the tool registry."""
        self.tools: Dict[str, Tool] = {}
    
    def register_tool(self, tool: Union[Tool, Callable[..., Any]], name: Optional[str] = None, **metadata: Any) -> Tool:
        """
        Register a tool with the registry.
        
        Args:
            tool: The tool or function to register
            name: Optional name for the tool (defaults to function/tool name)
            **metadata: Additional metadata for the tool
            
        Returns:
            The registered tool
            
        Raises:
            ValueError: If a tool with the same name is already registered
        """
        # If the tool is a function, create a Tool instance
        if not isinstance(tool, Tool):
            tool = create_tool(tool, name, **metadata)
        
        tool_name = name or tool.name
        
        # Check if tool is already registered
        if tool_name in self.tools:
            raise ValueError(f"Tool '{tool_name}' is already registered")
        
        self.tools[tool_name] = tool
        return tool
    
    def get_tool(self, name: str) -> Optional[Tool]:
        """
        Get a tool by name.
        
        Args:
            name: The name of the tool to get
            
        Returns:
            The tool if found, None otherwise
        """
        return self.tools.get(name)
    
    def list_tools(self) -> List[Dict[str, Any]]:
        """
        List all registered tools.
        
        Returns:
            List of dictionaries with tool information
        """
        return [
            {
                "name": tool.name,
                "description": tool.metadata.description,
                "category": tool.metadata.category,
                "tags": list(tool.metadata.tags)
            }
            for tool in self.tools.values()
        ]
    
    def get_tools_by_category(self, category: str) -> List[Tool]:
        """
        Get all tools in a specific category.
        
        Args:
            category: The category to filter by
            
        Returns:
            List of tools in the category
        """
        return [tool for tool in self.tools.values() if tool.metadata.category == category]
    
    def get_tools_by_tag(self, tag: str) -> List[Tool]:
        """
        Get all tools with a specific tag.
        
        Args:
            tag: The tag to filter by
            
        Returns:
            List of tools with the tag
        """
        return [tool for tool in self.tools.values() if tag in tool.metadata.tags]


# Create a global tool registry
tool_registry = ToolRegistry()


# Common utility tools
@Tool.register(name="echo", category="utility", tags={"debug", "utility"})
async def echo(message: str) -> str:
    """
    Echo the message back.
    
    Args:
        message: The message to echo
        
    Returns:
        The same message
    """
    return message


@Tool.register(name="fetch_json", category="http", tags={"http", "json", "api"})
async def fetch_json(url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Fetch JSON data from a URL.
    
    Args:
        url: The URL to fetch from
        method: HTTP method to use (GET, POST, etc.)
        headers: Optional HTTP headers
        
    Returns:
        The parsed JSON response
    """
    # This would be implemented with aiohttp or similar
    logger.info(f"Fetching JSON from {url} using {method}")
    return {"result": f"JSON data from {url} (placeholder)"}


@Tool.register(name="math_evaluate", category="math", tags={"math", "calculation"})
def math_evaluate(expression: str) -> float:
    """
    Evaluate a mathematical expression.
    
    Args:
        expression: The expression to evaluate
        
    Returns:
        The result of the evaluation
        
    Raises:
        ValueError: If the expression is invalid
    """
    # This would be implemented with a safe math evaluation library
    # or something like sympy for more advanced calculations
    logger.info(f"Evaluating math expression: {expression}")
    
    # Very basic implementation for example purposes only
    # In a real implementation, you would use a proper math parser
    try:
        # This is NOT safe and is just for demonstration
        # In a real implementation, use a proper math parser
        result = eval(expression)  # nosec
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid math expression: {str(e)}") 