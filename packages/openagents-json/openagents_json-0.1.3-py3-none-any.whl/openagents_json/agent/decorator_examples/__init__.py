"""
Decorator Examples for OpenAgents JSON.

This module provides example implementations of agents, capabilities, and tools
using the OpenAgents JSON decorators.
"""

# Import examples
from openagents_json.agent.decorator_examples.basic_agent import BasicAgent
from openagents_json.agent.decorator_examples.llm_agent import SimpleCompletion, ChatAgent
from openagents_json.agent.decorator_examples.tool_agent import WebSearchAgent

__all__ = [
    "BasicAgent",
    "SimpleCompletion",
    "ChatAgent",
    "WebSearchAgent",
] 