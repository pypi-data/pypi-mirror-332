"""
Tests for the agent registry functionality.
"""

import pytest

from openagents_json import OpenAgentsApp


def test_agent_registration():
    """Test registering an agent with the registry."""
    agents_app = OpenAgentsApp()

    @agents_app.agent("test_agent", description="A test agent")
    class TestAgent:
        def __init__(self, config=None):
            self.config = config or {}

    # Check that the agent was registered
    assert "test_agent" in agents_app.agent_registry.agents
    assert (
        agents_app.agent_registry.agents["test_agent"]["metadata"]["description"]
        == "A test agent"
    )


def test_capability_registration():
    """Test registering a capability with an agent."""
    agents_app = OpenAgentsApp()

    @agents_app.agent("test_agent", description="A test agent")
    class TestAgent:
        def __init__(self, config=None):
            self.config = config or {}

        @agents_app.capability("test_capability", description="A test capability")
        async def test_capability(self, text: str) -> str:
            return f"Processed: {text}"

    # Check that the capability was registered
    agent_info = agents_app.agent_registry.agents["test_agent"]
    assert "test_capability" in agent_info["capabilities"]
    assert (
        agent_info["capabilities"]["test_capability"]["description"]
        == "A test capability"
    )


def test_tool_registration():
    """Test registering a standalone tool."""
    agents_app = OpenAgentsApp()

    @agents_app.tool("test_tool", description="A test tool")
    def test_tool(text: str) -> str:
        return f"Tool output: {text}"

    # Check that the tool was registered
    assert "test_tool" in agents_app.agent_registry.tools


def test_multiple_agents():
    """Test registering multiple agents."""
    agents_app = OpenAgentsApp()

    @agents_app.agent("agent1", description="First agent")
    class Agent1:
        pass

    @agents_app.agent("agent2", description="Second agent")
    class Agent2:
        pass

    # Check that both agents were registered
    assert "agent1" in agents_app.agent_registry.agents
    assert "agent2" in agents_app.agent_registry.agents
    assert (
        agents_app.agent_registry.agents["agent1"]["metadata"]["description"]
        == "First agent"
    )
    assert (
        agents_app.agent_registry.agents["agent2"]["metadata"]["description"]
        == "Second agent"
    )
