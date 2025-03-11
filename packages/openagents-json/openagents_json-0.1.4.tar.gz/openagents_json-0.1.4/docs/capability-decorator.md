# Capability Decorator

The OpenAgents JSON library uses decorators to register agent capabilities. This guide focuses on the updated capability decorator that now requires keyword-only parameters for improved clarity and robustness.

## Overview

The capability decorator associates a function with a specific agent and gives it a name and metadata. The updated syntax requires the `agent_name` parameter to be specified as a keyword argument to make the relationship between agents and capabilities more explicit.

## Basic Usage

```python
from openagents_json import OpenAgentsApp

agents_app = OpenAgentsApp()

@agents_app.agent("text_processor")
class TextProcessor:
    def __init__(self):
        pass
        
    @agents_app.capability(
        agent_name="text_processor",  # Required keyword argument
        name="echo",                  # Optional, defaults to function name if not provided
        description="Echo back the input text"
    )
    async def echo(self, text: str) -> str:
        """Echo back the input text."""
        return text
```

## Required Parameters

- **agent_name** (str, keyword-only): The name of the agent this capability belongs to

## Optional Parameters

- **name** (str, optional): Name for the capability (defaults to the function name if not provided)
- **description** (str, optional): Description of what the capability does
- **version** (str, optional): Version of the capability
- **examples** (list, optional): Examples showing how to use the capability
- **input_schema** (dict, optional): Override for automatically extracted input schema
- **output_schema** (dict, optional): Override for automatically extracted output schema

## Parameter Validation

The decorator now includes validation to ensure that `agent_name` is:

1. Provided as a keyword argument
2. Not empty

If these conditions are not met, the decorator will raise appropriate errors:

- `TypeError`: If `agent_name` is not provided as a keyword argument
- `ValueError`: If `agent_name` is empty

## Examples

### Basic Example

```python
@agents_app.capability(
    agent_name="calculator",
    name="add",
    description="Add two numbers"
)
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b
```

### Using Default Function Name

```python
@agents_app.capability(
    agent_name="calculator",
    description="Multiply two numbers"
)
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b
```

### With Additional Metadata

```python
@agents_app.capability(
    agent_name="text_processor",
    name="summarize",
    description="Summarize text",
    version="1.0.0",
    examples=[
        {
            "inputs": {"text": "This is a long text that needs summarization..."},
            "outputs": "Short summary"
        }
    ]
)
async def summarize_text(self, text: str) -> str:
    """Summarize the provided text."""
    # Implementation...
    return summary
```

## Automatic Schema Generation

The capability decorator automatically extracts input and output schemas from function type hints. For example, with this function:

```python
@agents_app.capability(agent_name="data_processor")
async def process_data(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Process data and return statistics."""
    # Implementation...
    return stats
```

The system will automatically:

1. Extract that `data` is a `List[Dict[str, Any]]` type
2. Record that the return type is `Dict[str, int]`
3. Use the new type registry to safely serialize and deserialize these types

## Migration Guide

If you're updating from a previous version, you'll need to modify your capability decorators:

### Before

```python
@agents_app.capability("echo", description="Echo back the text")
async def echo(self, text: str) -> str:
    return text
```

### After

```python
@agents_app.capability(
    agent_name="your_agent_name",  # Required
    name="echo",
    description="Echo back the text"
)
async def echo(self, text: str) -> str:
    return text
```

## Benefits

- **Clarity**: Makes the relationship between agents and capabilities explicit
- **Safety**: Prevents accidentally associating capabilities with the wrong agent
- **Documentation**: Self-documents the code by clearly showing which agent a capability belongs to
- **Validation**: Catches errors early with parameter validation 