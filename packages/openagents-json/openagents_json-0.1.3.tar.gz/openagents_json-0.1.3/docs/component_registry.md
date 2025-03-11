# ComponentRegistry System

The ComponentRegistry is a central system for registering, discovering, and managing components in the OpenAgents JSON framework. Components can include agents, tools, assets, or any other reusable piece of functionality.

## Overview

The ComponentRegistry provides the following capabilities:

- Registration and management of components
- Metadata extraction and management
- Component versioning
- Component discovery
- Event notification for registry operations

## Getting Started

The ComponentRegistry is available through the `openagents_json.core` module:

```python
from openagents_json.core import (
    BaseComponentRegistry,
    InMemoryComponentRegistry,
    ComponentMetadata,
    component_registry,
)
```

The framework provides a default registry instance (`component_registry`) that you can use directly:

```python
from openagents_json.core import component_registry

# Register a component
component_registry.register("my_component", MyComponent())

# Get a registered component
my_component = component_registry.get("my_component")
```

## Registering Components

Components can be registered with or without custom metadata:

```python
# Register with auto-extracted metadata
component_registry.register("component_id", my_component)

# Register with custom metadata
component_registry.register(
    "component_id",
    my_component,
    ComponentMetadata(
        name="My Component",
        version="1.0.0",
        description="A useful component",
        tags={"category1", "category2"},
    )
)
```

When no metadata is provided, the registry will automatically extract metadata from the component's:

- Docstring (for description)
- `__version__` attribute (for version)
- `__author__` attribute (for author)
- `__tags__` attribute (for tags)

## Finding Components

The registry provides several ways to find components:

```python
# Get a specific component by ID
component = component_registry.get("component_id")

# List all registered component IDs
all_components = component_registry.list()

# Find components by metadata attributes
text_components = component_registry.find(tags=["text"])
version_1_components = component_registry.find(version="1.0.0")
```

The `find` method accepts any attribute of the `ComponentMetadata` class as a filter criterion.

## Working with Metadata

You can retrieve and inspect component metadata:

```python
# Get metadata for a component
metadata = component_registry.get_metadata("component_id")

print(f"Name: {metadata.name}")
print(f"Version: {metadata.version}")
print(f"Description: {metadata.description}")
print(f"Tags: {metadata.tags}")
```

## Event System

The registry includes an event system that notifies listeners when registry operations occur:

```python
from openagents_json.core.registry import ComponentRegistered, ComponentUnregistered

# Define event listeners
def on_component_registered(event):
    print(f"Component registered: {event.component_id}")

def on_component_unregistered(event):
    print(f"Component unregistered: {event.component_id}")

# Register event listeners
component_registry.add_event_listener(ComponentRegistered, on_component_registered)
component_registry.add_event_listener(ComponentUnregistered, on_component_unregistered)
```

## Thread Safety

All registry operations are thread-safe, allowing concurrent access from multiple threads.

## Custom Registry Implementations

You can create custom registry implementations by extending the `BaseComponentRegistry` abstract class:

```python
from openagents_json.core import BaseComponentRegistry

class CustomRegistry(BaseComponentRegistry):
    # Implement the required methods...
    pass
```

This allows for specialized registry implementations, such as persistent storage or distributed registries.

## Example Usage

Here's a complete example of using the ComponentRegistry:

```python
from openagents_json.core import component_registry, ComponentMetadata

# Define a simple component
class TextProcessor:
    """A component that processes text."""
    __version__ = "1.0.0"
    __author__ = "OpenAgents Team"
    __tags__ = ["text", "nlp"]
    
    def process(self, text):
        return f"Processed: {text}"

# Register the component
processor = TextProcessor()
component_registry.register("text_processor", processor)

# Find components by tag
text_components = component_registry.find(tags=["text"])
print(f"Found {len(text_components)} text components: {text_components}")

# Use the component
if "text_processor" in text_components:
    processor = component_registry.get("text_processor")
    result = processor.process("Hello, world!")
    print(result)
```

For more examples, see the `examples/component_registry_example.py` file in the repository. 