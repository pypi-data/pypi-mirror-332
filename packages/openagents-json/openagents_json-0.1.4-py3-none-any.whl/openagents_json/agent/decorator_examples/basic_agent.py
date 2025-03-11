"""
Basic Agent Example for OpenAgents JSON.

This module demonstrates how to create a simple agent with capabilities
using the decorator pattern.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional

from openagents_json.agent.base import BaseAgent
from openagents_json.agent.capabilities import Capability

logger = logging.getLogger(__name__)


class BasicAgent(BaseAgent):
    """
    A simple example agent that demonstrates basic capability usage.
    
    This agent implements a few basic capabilities like echoing messages,
    doing simple math, and storing/retrieving information.
    """
    
    def __init__(self, name: str, **kwargs):
        """
        Initialize the basic agent.
        
        Args:
            name: Name of the agent
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, **kwargs)
        
        # Register capabilities
        self.add_capability("echo", self.echo_message)
        self.add_capability("add", self.add_numbers)
        self.add_capability("store", self.store_data)
        self.add_capability("retrieve", self.retrieve_data)
    
    async def initialize(self) -> bool:
        """
        Initialize the agent.
        
        Returns:
            True if initialization was successful
        """
        logger.info(f"Initializing BasicAgent: {self.name}")
        return await super().initialize()
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with the given inputs.
        
        Args:
            inputs: Dictionary with the following possible keys:
                - action: The capability to execute
                - parameters: Parameters for the capability
                
        Returns:
            Dictionary with the results of the executed capability
        """
        if not self._initialized:
            await self.initialize()
        
        action = inputs.get("action", "echo")
        parameters = inputs.get("parameters", {})
        
        if action not in self.capabilities:
            return {
                "error": f"Unknown action: {action}",
                "available_actions": list(self.capabilities.keys())
            }
        
        try:
            result = await self.call_capability(action, **parameters)
            return {"result": result, "action": action}
        except Exception as e:
            logger.error(f"Error executing capability {action}: {str(e)}")
            return {"error": str(e), "action": action}
    
    @Capability.register(name="echo", description="Echo a message back")
    async def echo_message(self, message: str) -> str:
        """
        Echo a message back.
        
        Args:
            message: The message to echo
            
        Returns:
            The same message
        """
        logger.info(f"Echoing message: {message}")
        return message
    
    @Capability.register(name="add", description="Add two numbers")
    async def add_numbers(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of the two numbers
        """
        logger.info(f"Adding numbers: {a} + {b}")
        return a + b
    
    @Capability.register(name="store", description="Store data in the agent's memory")
    async def store_data(self, key: str, value: Any) -> bool:
        """
        Store data in the agent's memory.
        
        Args:
            key: The key to store the data under
            value: The data to store
            
        Returns:
            True if the data was stored successfully
        """
        logger.info(f"Storing data: {key} = {value}")
        
        # Store in the agent's memory
        if not hasattr(self.state, "memory"):
            self.state.memory = {}
        
        self.state.memory[key] = value
        self.update_state()
        
        return True
    
    @Capability.register(name="retrieve", description="Retrieve data from the agent's memory")
    async def retrieve_data(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Retrieve data from the agent's memory.
        
        Args:
            key: The key to retrieve
            default: Default value if the key doesn't exist
            
        Returns:
            The retrieved data or the default value
        """
        logger.info(f"Retrieving data: {key}")
        
        if not hasattr(self.state, "memory"):
            return default
        
        return self.state.memory.get(key, default)


# Example usage
async def example():
    """Example of using the BasicAgent."""
    agent = BasicAgent("example_basic_agent")
    
    # Initialize the agent
    await agent.initialize()
    
    # Execute capabilities
    echo_result = await agent.execute({
        "action": "echo",
        "parameters": {"message": "Hello, world!"}
    })
    print(f"Echo result: {echo_result}")
    
    add_result = await agent.execute({
        "action": "add",
        "parameters": {"a": 2, "b": 3}
    })
    print(f"Add result: {add_result}")
    
    store_result = await agent.execute({
        "action": "store",
        "parameters": {"key": "favorite_color", "value": "blue"}
    })
    print(f"Store result: {store_result}")
    
    retrieve_result = await agent.execute({
        "action": "retrieve",
        "parameters": {"key": "favorite_color"}
    })
    print(f"Retrieve result: {retrieve_result}")


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Run the example
    asyncio.run(example()) 