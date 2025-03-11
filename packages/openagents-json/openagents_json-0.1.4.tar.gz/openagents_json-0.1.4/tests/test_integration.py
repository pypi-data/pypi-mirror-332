"""
Integration tests for OpenAgents JSON.

This module performs end-to-end tests to verify that all components work together correctly.
"""

import unittest
import asyncio
from typing import List, Dict, Any

from openagents_json import OpenAgentsApp
from openagents_json.agent.type_registry import serialize_type, deserialize_type


class IntegrationTests(unittest.TestCase):
    """Integration tests for OpenAgents JSON."""
    
    def setUp(self):
        """Set up the test environment."""
        self.app = OpenAgentsApp()
        
        # Register a test agent with capabilities
        @self.app.agent("integration_agent", description="Test agent for integration tests")
        class IntegrationAgent:
            def __init__(self, config=None):
                self.config = config or {}
                self.calls = []
                
            @self.app.capability(
                agent_name="integration_agent",
                name="process_data",
                description="Process a list of data items"
            )
            async def process_data(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
                """Process a list of data items and return summary."""
                self.calls.append(("process_data", data))
                
                # Simple processing
                total_items = len(data)
                total_values = sum(item.get("value", 0) for item in data)
                
                return {
                    "total_items": total_items,
                    "total_values": total_values,
                    "average": total_values / total_items if total_items else 0
                }
        
        self.IntegrationAgent = IntegrationAgent
        
        # Register a standalone tool
        @self.app.tool("multiply", description="Multiply two numbers")
        async def multiply(a: float, b: float) -> float:
            """Multiply two numbers and return the result."""
            return a * b
    
    def test_agent_registration(self):
        """Test that agents are registered correctly."""
        # Check if the agent is registered
        self.assertIn("integration_agent", self.app.registry.agents)
        
        # Check if the agent has the capability
        agent_info = self.app.registry.agents["integration_agent"]
        self.assertIn("process_data", agent_info["capabilities"])
    
    def test_capability_registration(self):
        """Test that capabilities are registered correctly."""
        # Check if the capability is registered
        self.assertIn("process_data", self.app.registry.capabilities)
        
        # Check capability metadata
        capability_info = self.app.registry.capabilities["process_data"]
        self.assertEqual(capability_info["agent_name"], "integration_agent")
        self.assertEqual(capability_info["description"], "Process a list of data items")
        
        # Check input schema (verify type serialization works)
        self.assertIn("data", capability_info["input_schema"])
        self.assertIn("type", capability_info["input_schema"]["data"])
        
        # The type should be List[Dict[str, Any]] or equivalent
        type_str = capability_info["input_schema"]["data"]["type"]
        deserialized_type = deserialize_type(type_str)
        
        # Verify the deserialized type is correct (this is a bit complex with generics)
        self.assertTrue(hasattr(deserialized_type, "__origin__"))
        self.assertEqual(deserialized_type.__origin__, list)
    
    def test_tool_registration(self):
        """Test that tools are registered correctly."""
        # Check if the tool is registered
        self.assertIn("multiply", self.app.registry.tools)
        
        # Check tool metadata
        tool_info = self.app.registry.tools["multiply"]
        self.assertEqual(tool_info["name"], "multiply")
        self.assertEqual(tool_info["description"], "Multiply two numbers")
        
        # Check input schema
        self.assertIn("a", tool_info["input_schema"])
        self.assertIn("b", tool_info["input_schema"])
        
        # Check types
        self.assertEqual(deserialize_type(tool_info["input_schema"]["a"]["type"]), float)
        self.assertEqual(deserialize_type(tool_info["input_schema"]["b"]["type"]), float)
    
    async def async_test_capability_execution(self):
        """Test capability execution."""
        # Create an instance of the agent
        agent = self.IntegrationAgent()
        
        # Test data
        test_data = [
            {"id": 1, "value": 10},
            {"id": 2, "value": 20},
            {"id": 3, "value": 30}
        ]
        
        # Execute the capability
        result = await self.app.execute_capability(
            "integration_agent",
            "process_data",
            {"data": test_data}
        )
        
        # Verify the result
        self.assertEqual(result["total_items"], 3)
        self.assertEqual(result["total_values"], 60)
        self.assertEqual(result["average"], 20)
    
    async def async_test_tool_execution(self):
        """Test tool execution."""
        # Execute the tool
        result = await self.app.execute_tool("multiply", {"a": 5, "b": 7})
        
        # Verify the result
        self.assertEqual(result, 35)
    
    def test_capability_execution(self):
        """Run async test for capability execution."""
        asyncio.run(self.async_test_capability_execution())
        
    def test_tool_execution(self):
        """Run async test for tool execution."""
        asyncio.run(self.async_test_tool_execution())


if __name__ == "__main__":
    unittest.main() 