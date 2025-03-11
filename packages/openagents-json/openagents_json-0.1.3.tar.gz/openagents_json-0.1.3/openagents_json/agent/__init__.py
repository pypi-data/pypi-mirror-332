"""
OpenAgents JSON Agent Module.

This module provides base classes, utilities, and decorators for defining and using agents
within the OpenAgents JSON framework.
"""

# Import core components
from openagents_json.agent.base import BaseAgent, LLMAgent, ToolAgent, WorkflowAgent
from openagents_json.agent.capabilities import Capability, create_capability
from openagents_json.agent.tools import Tool, create_tool, tool_registry
from openagents_json.agent.config import AgentConfig
from openagents_json.agent.monitoring import AgentMonitor, agent_monitor
from openagents_json.agent.workflow import (
    AgentStep, 
    SequentialAgentWorkflow, 
    create_agent_workflow,
    agent_to_workflow_definition
)

# Import utility functions
from openagents_json.agent.utils import (
    AgentStateManager,
    validate_inputs,
    validate_outputs,
    serialize_agent,
    deserialize_agent
)

# Import examples
from openagents_json.agent.decorator_examples import (
    BasicAgent,
    SimpleCompletion,
    ChatAgent,
    WebSearchAgent
)

__all__ = [
    # Basic agent types
    "BaseAgent",
    "LLMAgent",
    "ToolAgent",
    "WorkflowAgent",
    
    # Agent capabilities and tools
    "Capability",
    "create_capability",
    "Tool",
    "create_tool",
    "tool_registry",
    
    # Configuration and monitoring
    "AgentConfig",
    "AgentMonitor",
    "agent_monitor",
    
    # Workflow integration
    "AgentStep",
    "SequentialAgentWorkflow",
    "create_agent_workflow",
    "agent_to_workflow_definition",
    
    # Utilities
    "AgentStateManager",
    "validate_inputs",
    "validate_outputs",
    "serialize_agent",
    "deserialize_agent",
    
    # Examples
    "BasicAgent",
    "SimpleCompletion",
    "ChatAgent",
    "WebSearchAgent",
]
