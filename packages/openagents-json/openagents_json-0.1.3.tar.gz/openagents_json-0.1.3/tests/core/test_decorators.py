"""
Unit tests for enhanced decorators.
"""

import inspect
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock, patch

import pytest

from openagents_json.core.decorators import (
    AgentConfig,
    CapabilityConfig,
    Example,
    ToolConfig,
    extract_schema_from_function,
)


# Create mock classes
class MockAgentRegistry:
    def __init__(self):
        self.agents = {}
        self.capabilities = {}
        self.tools = {}
        self.tools_metadata = {}

    def register_agent(self, name, cls, metadata):
        self.agents[name] = {"cls": cls, "metadata": metadata, "capabilities": {}}
        self.capabilities[name] = {}

    def register_capability(self, agent_name, capability_name, func, metadata):
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not registered")
        self.capabilities[agent_name][capability_name] = func
        self.agents[agent_name]["capabilities"][capability_name] = metadata

    def register_tool(self, name, func, metadata):
        self.tools[name] = func
        self.tools_metadata[name] = metadata


class MockOpenAgentsApp:
    def __init__(self):
        from openagents_json.core.decorators import (
            create_agent_decorator,
            create_capability_decorator,
            create_tool_decorator,
        )

        self.agent_registry = MockAgentRegistry()
        # Create enhanced decorators
        self.agent = create_agent_decorator(self.agent_registry)
        self.capability = create_capability_decorator(self.agent_registry)
        self.tool = create_tool_decorator(self.agent_registry)


# Setup for tests
@pytest.fixture
def app():
    """Create a fresh MockOpenAgentsApp instance for each test."""
    return MockOpenAgentsApp()


# Tests for agent decorator
def test_agent_class_registration(app):
    """Test registering a class-based agent."""

    @app.agent("test_agent", description="Test agent", version="1.0.0")
    class TestAgent:
        """Test agent docstring."""

        def __init__(self, config=None):
            self.config = config or {}

    # Verify agent was registered
    assert "test_agent" in app.agent_registry.agents
    agent_info = app.agent_registry.agents["test_agent"]

    # Check class registration
    assert agent_info["cls"] == TestAgent

    # Check metadata extraction
    assert "description" in agent_info["metadata"]
    assert agent_info["metadata"]["description"] == "Test agent"
    assert agent_info["metadata"]["version"] == "1.0.0"


def test_agent_function_registration(app):
    """Test registering a function-based agent."""

    @app.agent("calc", description="Calculator agent")
    async def calculator(op: str, a: float, b: float) -> float:
        """Simple calculator."""
        if op == "add":
            return a + b
        return 0

    # Verify agent was registered
    assert "calc" in app.agent_registry.agents
    agent_info = app.agent_registry.agents["calc"]

    # Check function registration
    assert agent_info["cls"] == calculator

    # Check metadata extraction
    assert "description" in agent_info["metadata"]
    assert agent_info["metadata"]["description"] == "Calculator agent"


# Tests for capability decorator
def test_capability_registration(app):
    """Test registering a capability on an agent."""

    @app.agent("agent_with_capabilities")
    class TestAgent:
        """Agent with capabilities."""

        @app.capability("test_capability", description="Test capability")
        async def test_capability(self, input: str) -> str:
            """Test capability docstring."""
            return input

    # Verify capability was registered
    assert "agent_with_capabilities" in app.agent_registry.agents
    agent_info = app.agent_registry.agents["agent_with_capabilities"]

    # Check capability registration
    assert "test_capability" in agent_info["capabilities"]
    capability_info = agent_info["capabilities"]["test_capability"]

    # Check metadata extraction
    assert "description" in capability_info
    assert capability_info["description"] == "Test capability"

    # Check schema extraction
    assert "input_schema" in capability_info
    assert "input" in capability_info["input_schema"]
    assert capability_info["input_schema"]["input"]["type"] == "str"

    assert "output_schema" in capability_info
    assert capability_info["output_schema"]["type"] == "str"


def test_capability_with_examples(app):
    """Test registering a capability with examples."""

    @app.agent("agent_with_examples")
    class TestAgent:
        """Agent with examples."""

        @app.capability(
            "echo",
            examples=[
                {"inputs": {"text": "Hello"}, "outputs": "Hello"},
                {"inputs": {"text": "World"}, "outputs": "World"},
            ],
        )
        async def echo(self, text: str) -> str:
            """Echo back the input."""
            return text

    # Verify capability has examples
    agent_info = app.agent_registry.agents["agent_with_examples"]
    capability_info = agent_info["capabilities"]["echo"]

    assert "examples" in capability_info
    assert len(capability_info["examples"]) == 2
    assert capability_info["examples"][0]["inputs"]["text"] == "Hello"


# Tests for tool decorator
def test_tool_registration(app):
    """Test registering a standalone tool."""

    @app.tool("test_tool", description="Test tool")
    def test_tool(input: str, count: int = 1) -> List[str]:
        """Test tool docstring."""
        return [input] * count

    # Verify tool was registered
    assert "test_tool" in app.agent_registry.tools

    # Check tool function
    assert app.agent_registry.tools["test_tool"] == test_tool

    # Check schema extraction
    tool_metadata = app.agent_registry.tools_metadata.get("test_tool", {})

    assert "input_schema" in tool_metadata
    assert "input" in tool_metadata["input_schema"]
    assert tool_metadata["input_schema"]["input"]["type"] == "str"
    assert "count" in tool_metadata["input_schema"]
    assert tool_metadata["input_schema"]["count"]["type"] == "int"
    assert tool_metadata["input_schema"]["count"]["required"] is False

    assert "output_schema" in tool_metadata
    assert tool_metadata["output_schema"]["type"] == "list"


def test_tool_with_complex_types(app):
    """Test registering a tool with complex types."""

    @app.tool("complex_tool")
    def complex_tool(
        items: List[Dict[str, Any]], filter_key: Optional[str] = None
    ) -> Dict[str, List[Any]]:
        """Complex tool with complex types."""
        result = {}
        for item in items:
            if filter_key and filter_key not in item:
                continue
            result.setdefault(str(item.get(filter_key, "other")), []).append(item)
        return result

    # Check schema extraction for complex types
    tool_metadata = app.agent_registry.tools_metadata.get("complex_tool", {})

    assert "input_schema" in tool_metadata
    assert "items" in tool_metadata["input_schema"]
    assert "filter_key" in tool_metadata["input_schema"]
    assert tool_metadata["input_schema"]["filter_key"]["required"] is False

    assert "output_schema" in tool_metadata
    assert tool_metadata["output_schema"]["type"] == "dict"


# Tests for schema extraction function
def test_extract_schema_from_function():
    """Test the schema extraction function."""

    def test_func(
        required_str: str, optional_int: int = 42, optional_list: List[str] = None
    ) -> Dict[str, Any]:
        """Test function for schema extraction."""
        return {"result": required_str, "count": optional_int}

    input_schema, output_schema = extract_schema_from_function(test_func)

    # Check input schema
    assert "required_str" in input_schema
    assert input_schema["required_str"]["type"] == "str"
    assert input_schema["required_str"]["required"] is True

    assert "optional_int" in input_schema
    assert input_schema["optional_int"]["type"] == "int"
    assert input_schema["optional_int"]["required"] is False
    assert input_schema["optional_int"]["default"] == 42

    assert "optional_list" in input_schema
    assert input_schema["optional_list"]["required"] is False

    # Check output schema
    assert output_schema["type"] == "dict"


def test_docstring_extraction(app):
    """Test extracting metadata from docstrings."""

    @app.agent("docstring_agent")
    class DocAgent:
        """
        Agent with detailed docstring.

        This agent demonstrates docstring extraction.
        """

        @app.capability("doc_capability")
        async def doc_capability(self, input: str) -> str:
            """
            Capability with detailed docstring.

            This capability shows how docstrings are processed.

            Args:
                input: The input string

            Returns:
                The processed output
            """
            return input

    agent_info = app.agent_registry.agents["docstring_agent"]

    # Check agent description extraction
    assert "description" in agent_info["metadata"]
    assert "Agent with detailed docstring" in agent_info["metadata"]["description"]

    # Check capability description extraction
    capability_info = agent_info["capabilities"]["doc_capability"]
    assert "description" in capability_info
    assert "Capability with detailed docstring" in capability_info["description"]
