"""
Component Registry Usage Example

This example demonstrates how to use the ComponentRegistry to register,
manage, and discover components in OpenAgents JSON.

The ComponentRegistry provides a central location to register agents, tools,
and other components, making them discoverable and reusable throughout your application.
"""

import logging
from typing import Dict, Any, List, Optional

from openagents_json.core import (
    BaseComponentRegistry,
    InMemoryComponentRegistry,
    ComponentMetadata,
    component_registry,
)


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Simple component classes for the example
class Agent:
    """An agent that can execute tasks."""
    __version__ = "1.0.0"
    __author__ = "OpenAgents Team"
    __tags__ = ["agent", "core"]
    
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities
    
    def execute(self, task: str) -> str:
        return f"Agent {self.name} executed task: {task}"


class Tool:
    """A tool that can be used by agents."""
    __version__ = "1.0.0"
    __author__ = "OpenAgents Team"
    __tags__ = ["tool", "utility"]
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def use(self, input_data: Any) -> Any:
        return f"Tool {self.name} processed: {input_data}"


def register_components():
    """Register some example components with the registry."""
    # Register agents
    text_agent = Agent("TextProcessor", ["text_analysis", "summarization"])
    component_registry.register(
        "agents.text_processor",
        text_agent,
        ComponentMetadata(
            name="Text Processing Agent",
            description="An agent that processes and analyzes text content",
            tags={"agent", "text", "nlp"}
        )
    )
    
    vision_agent = Agent("ImageAnalyzer", ["object_detection", "image_classification"])
    component_registry.register(
        "agents.image_analyzer",
        vision_agent
    )  # Let metadata be auto-extracted
    
    # Register tools
    summarize_tool = Tool("Summarizer", "Summarizes text content")
    component_registry.register("tools.summarizer", summarize_tool)
    
    translator_tool = Tool("Translator", "Translates text between languages")
    component_registry.register("tools.translator", translator_tool)
    
    logger.info(f"Registered {len(component_registry.list())} components")


def demonstrate_lookup():
    """Demonstrate how to look up components."""
    # Get a component by ID
    text_agent = component_registry.get("agents.text_processor")
    
    if text_agent:
        logger.info(f"Found agent: {text_agent.name}")
        logger.info(f"Capabilities: {text_agent.capabilities}")
        
        # Get and display metadata
        metadata = component_registry.get_metadata("agents.text_processor")
        logger.info(f"Metadata: {metadata.name}, {metadata.description}, {metadata.tags}")
        
        # Execute the agent
        result = text_agent.execute("Analyze this document")
        logger.info(f"Result: {result}")
    else:
        logger.warning("Text agent not found")


def demonstrate_filtering():
    """Demonstrate how to find components based on metadata."""
    # Find all agents
    agent_ids = component_registry.find(tags=["agent"])
    logger.info(f"Found {len(agent_ids)} agents: {agent_ids}")
    
    # Find all tools
    tool_ids = component_registry.find(tags=["tool"])
    logger.info(f"Found {len(tool_ids)} tools: {tool_ids}")
    
    # Find components by author
    openagents_components = component_registry.find(author="OpenAgents Team")
    logger.info(f"OpenAgents components: {openagents_components}")


def demonstrate_events():
    """Demonstrate the event system."""
    from openagents_json.core.registry import ComponentRegistered, ComponentUnregistered
    
    # Create event listeners
    def on_component_registered(event):
        logger.info(f"EVENT: Component registered: {event.component_id}")
    
    def on_component_unregistered(event):
        logger.info(f"EVENT: Component unregistered: {event.component_id}")
    
    # Register the listeners
    component_registry.add_event_listener(ComponentRegistered, on_component_registered)
    component_registry.add_event_listener(ComponentUnregistered, on_component_unregistered)
    
    # Register and unregister a component to trigger events
    calculator_tool = Tool("Calculator", "Performs mathematical calculations")
    logger.info("Registering calculator tool (should trigger event)...")
    component_registry.register("tools.calculator", calculator_tool)
    
    logger.info("Unregistering calculator tool (should trigger event)...")
    component_registry.unregister("tools.calculator")


def main():
    """Run the example."""
    logger.info("Starting Component Registry Example")
    
    # Register example components
    register_components()
    
    # Demonstrate component lookup
    demonstrate_lookup()
    
    # Demonstrate component filtering
    demonstrate_filtering()
    
    # Demonstrate events
    demonstrate_events()
    
    logger.info("Example completed")


if __name__ == "__main__":
    main() 