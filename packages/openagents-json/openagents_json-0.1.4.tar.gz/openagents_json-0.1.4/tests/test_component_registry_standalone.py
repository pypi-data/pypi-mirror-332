"""
Standalone tests for the ComponentRegistry implementation.
"""

import importlib.util
import os
import sys
from typing import Any, Dict, List, Optional, Set

import pytest

# Directly import the registry module without going through the core package
spec = importlib.util.spec_from_file_location(
    "registry",
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "openagents_json/core/registry.py"
    ),
)
registry_module = importlib.util.module_from_spec(spec)
sys.modules["registry"] = registry_module
spec.loader.exec_module(registry_module)

# Import the classes directly from the module
BaseComponentRegistry = registry_module.BaseComponentRegistry
InMemoryComponentRegistry = registry_module.InMemoryComponentRegistry
ComponentMetadata = registry_module.ComponentMetadata
ComponentRegistered = registry_module.ComponentRegistered
ComponentUnregistered = registry_module.ComponentUnregistered
ComponentLookup = registry_module.ComponentLookup


class DummyComponent:
    """A dummy component for testing the registry."""

    __version__ = "1.0.0"
    __author__ = "Test Author"
    __tags__ = ["test", "dummy"]

    def __init__(self, name: str, config: Optional[Dict[str, Any]] = None):
        self.name = name
        self.config = config or {}

    def execute(self) -> str:
        return f"Executed {self.name}"


class TestComponentRegistry:
    """Test suite for the ComponentRegistry implementation."""

    def test_register_and_get(self):
        """Test that components can be registered and retrieved."""
        registry = InMemoryComponentRegistry()
        component = DummyComponent("test_component")

        registry.register("test", component)

        retrieved = registry.get("test")
        assert retrieved is component
        assert retrieved.name == "test_component"

    def test_metadata_extraction(self):
        """Test that metadata is correctly extracted from components."""
        registry = InMemoryComponentRegistry()
        component = DummyComponent("test_component")

        registry.register("test", component)

        metadata = registry.get_metadata("test")
        assert metadata is not None
        assert metadata.name == "test"
        assert metadata.version == "1.0.0"
        assert metadata.author == "Test Author"
        assert metadata.tags == {"test", "dummy"}
        assert "dummy component for testing" in metadata.description.lower()

    def test_custom_metadata(self):
        """Test that custom metadata can be provided."""
        registry = InMemoryComponentRegistry()
        component = DummyComponent("test_component")
        custom_metadata = ComponentMetadata(
            name="custom_name",
            version="2.0.0",
            description="Custom description",
            author="Custom Author",
            tags={"custom", "tags"},
        )

        registry.register("test", component, metadata=custom_metadata)

        metadata = registry.get_metadata("test")
        assert metadata is not None
        assert metadata.name == "custom_name"
        assert metadata.version == "2.0.0"
        assert metadata.description == "Custom description"
        assert metadata.author == "Custom Author"
        assert metadata.tags == {"custom", "tags"}

    def test_unregister(self):
        """Test that components can be unregistered."""
        registry = InMemoryComponentRegistry()
        component = DummyComponent("test_component")

        registry.register("test", component)
        assert registry.get("test") is component

        success = registry.unregister("test")
        assert success is True
        assert registry.get("test") is None
        assert registry.get_metadata("test") is None

    def test_list(self):
        """Test that all registered components can be listed."""
        registry = InMemoryComponentRegistry()

        # Register multiple components
        registry.register("comp1", DummyComponent("Component 1"))
        registry.register("comp2", DummyComponent("Component 2"))
        registry.register("comp3", DummyComponent("Component 3"))

        component_ids = registry.list()
        assert len(component_ids) == 3
        assert set(component_ids) == {"comp1", "comp2", "comp3"}

    def test_find(self):
        """Test that components can be found by metadata attributes."""
        registry = InMemoryComponentRegistry()

        # Register components with different tags
        comp1 = DummyComponent("Component 1")
        comp2 = DummyComponent("Component 2")
        comp2.__tags__ = ["test", "special"]

        registry.register("comp1", comp1)
        registry.register("comp2", comp2)

        # Find by tag
        results = registry.find(tags=["special"])
        assert len(results) == 1
        assert results[0] == "comp2"

        # Find by author
        results = registry.find(author="Test Author")
        assert len(results) == 2
        assert set(results) == {"comp1", "comp2"}

        # Find by version
        results = registry.find(version="1.0.0")
        assert len(results) == 2
        assert set(results) == {"comp1", "comp2"}

    def test_events(self):
        """Test that registry events are fired correctly."""
        registry = InMemoryComponentRegistry()
        component = DummyComponent("test_component")

        # Event tracking
        registered_events = []
        unregistered_events = []
        lookup_events = []

        # Add event listeners
        registry.add_event_listener(
            ComponentRegistered, lambda e: registered_events.append(e)
        )
        registry.add_event_listener(
            ComponentUnregistered, lambda e: unregistered_events.append(e)
        )
        registry.add_event_listener(ComponentLookup, lambda e: lookup_events.append(e))

        # Test registration event
        registry.register("test", component)
        assert len(registered_events) == 1
        assert registered_events[0].component_id == "test"
        assert registered_events[0].component is component

        # Test lookup event
        registry.get("test")
        assert len(lookup_events) == 1
        assert lookup_events[0].component_id == "test"
        assert lookup_events[0].component is component

        # Test unregistration event
        registry.unregister("test")
        assert len(unregistered_events) == 1
        assert unregistered_events[0].component_id == "test"
        assert unregistered_events[0].component is component
