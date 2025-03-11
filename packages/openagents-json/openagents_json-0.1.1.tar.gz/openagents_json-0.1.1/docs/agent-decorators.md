# Agent and Tool Decorators

OpenAgents JSON provides intuitive decorators for registering agents, capabilities, and tools. This guide explains how to use these decorators to build AI components with rich metadata.

## Overview

The decorator system allows you to:

- Register agents, capabilities, and tools with minimal code
- Extract metadata automatically from docstrings and type annotations
- Provide examples and schema information for components
- Generate documentation automatically

## Basic Usage

### Creating an Agent

```python
from openagents_json import OpenAgentsApp

agents_app = OpenAgentsApp()

# Class-based agent
@agents_app.agent("text_processor")
class TextProcessor:
    """
    An agent that processes text in various ways.
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        
    @agents_app.capability("echo")
    async def echo(self, text: str) -> str:
        """Echo back the text."""
        return text

# Function-based agent
@agents_app.agent("calculator")
async def calculate(operation: str, a: float, b: float) -> float:
    """Perform a mathematical calculation."""
    if operation == "add":
        return a + b
    # Additional operations...
    return 0
```

### Creating a Tool

```python
# Standalone tool
@agents_app.tool("uppercase")
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()
```

## Advanced Usage

### Agent Configuration

```python
@agents_app.agent(
    "text_processor",
    version="1.0.0",
    description="Processes text in various ways",
    tags={"text", "processing"},
    model="gpt-4"
)
class TextProcessor:
    # Agent implementation...
```

### Capability with Examples

```python
@agents_app.capability(
    "echo",
    description="Echo back the text",
    examples=[
        {"inputs": {"text": "Hello, World!"}, "outputs": "Hello, World!"}
    ]
)
async def echo(self, text: str) -> str:
    """Echo back the text."""
    return text
```

### Tool with Complex Types

```python
@agents_app.tool(
    "filter_items",
    description="Filter items based on criteria"
)
def filter_items(
    items: List[Dict[str, Union[str, int, float]]],
    field: str,
    min_value: Optional[float] = None,
    max_value: Optional[float] = None,
    contains: Optional[str] = None
) -> List[Dict[str, Union[str, int, float]]]:
    """Filter a list of items based on criteria."""
    # Implementation...
```

## Metadata Extraction

The decorators automatically extract metadata from:

1. **Docstrings** - For descriptions and documentation
2. **Type Annotations** - For input/output schemas
3. **Default Values** - For parameter requirements
4. **Decorator Arguments** - For explicit metadata

Example of extracted metadata:

```python
# From this function:
@app.tool("example_tool")
def example_tool(text: str, count: int = 1) -> List[str]:
    """An example tool."""
    return [text] * count

# The following metadata is extracted:
{
    "name": "example_tool",
    "description": "An example tool.",
    "input_schema": {
        "text": {
            "type": "str",
            "required": true
        },
        "count": {
            "type": "int",
            "required": false,
            "default": 1
        }
    },
    "output_schema": {
        "type": "list"
    }
}
```

## Decorator Options

### Agent Decorator

```python
@agents_app.agent(
    name,                   # Required: Name of the agent
    version="0.1.0",        # Optional: Version of the agent
    description="",         # Optional: Description of the agent
    author="",              # Optional: Author of the agent
    tags=set(),             # Optional: Set of tags for the agent
    model=None,             # Optional: Default model for the agent
    examples=[],            # Optional: Examples for the agent
    **extra                 # Additional metadata
)
```

### Capability Decorator

```python
@agents_app.capability(
    name,                   # Required: Name of the capability
    version="0.1.0",        # Optional: Version of the capability
    description="",         # Optional: Description of the capability
    examples=[],            # Optional: Examples for the capability
    input_schema={},        # Optional: Override for input schema
    output_schema={},       # Optional: Override for output schema
    **extra                 # Additional metadata
)
```

### Tool Decorator

```python
@agents_app.tool(
    name,                   # Required: Name of the tool
    version="0.1.0",        # Optional: Version of the tool
    description="",         # Optional: Description of the tool
    examples=[],            # Optional: Examples for the tool
    input_schema={},        # Optional: Override for input schema
    output_schema={},       # Optional: Override for output schema
    **extra                 # Additional metadata
)
```

## Examples

### Providing Examples

Examples help document and test your components:

```python
@agents_app.tool(
    "uppercase",
    examples=[
        {"inputs": {"text": "hello"}, "outputs": "HELLO"},
        {"inputs": {"text": "Example Text"}, "outputs": "EXAMPLE TEXT"}
    ]
)
def uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()
```

### Overriding Schema

You can override the automatically extracted schema:

```python
@agents_app.capability(
    "custom_schema",
    input_schema={
        "text": {
            "type": "string",
            "format": "email",
            "description": "Email address to process"
        }
    },
    output_schema={
        "type": "object",
        "properties": {
            "valid": {"type": "boolean"},
            "domain": {"type": "string"}
        }
    }
)
async def validate_email(self, text: str) -> Dict[str, Any]:
    """Validate an email address."""
    # Implementation...
```

## Best Practices

1. **Use Descriptive Docstrings**: The first paragraph is used as the component description.

2. **Add Type Annotations**: These are used for schema generation, so be specific.

3. **Provide Examples**: These help users understand how to use your components.

4. **Use Consistent Naming**: Use consistent naming conventions for your agents and tools.

5. **Document Parameters**: Use proper docstring format to document parameters:

   ```python
   async def my_function(param1: str, param2: int = 0) -> str:
       """
       Function description.
       
       Args:
           param1: Description of param1
           param2: Description of param2, defaults to 0
           
       Returns:
           Description of the return value
       """
   ```

## Common Patterns

### Class-based vs Function-based Agents

- **Class-based Agents**: Use when you need to maintain state or have multiple capabilities
- **Function-based Agents**: Use for simple agents with single functionality

### Configuration Options

Support both decorator arguments and constructor configuration:

```python
@agents_app.agent("text_processor", model="gpt-4")
class TextProcessor:
    def __init__(self, config=None):
        self.config = config or {}
        self.model = self.config.get("model") or "gpt-4"
```

This allows flexible configuration at both registration and instantiation time. 