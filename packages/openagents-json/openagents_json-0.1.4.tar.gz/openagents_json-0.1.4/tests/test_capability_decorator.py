"""
Tests for the capability decorator.

This module tests the proper usage and validation of the capability decorator,
especially with the new keyword-only parameters requirement.
"""

import unittest
from unittest.mock import MagicMock, patch

from openagents_json import OpenAgentsApp


class CapabilityDecoratorTests(unittest.TestCase):
    """Test cases for the capability decorator."""

    def setUp(self):
        """Set up the test environment."""
        self.app = OpenAgentsApp()
        
        # Register a test agent
        @self.app.agent("test_agent")
        class TestAgent:
            def __init__(self):
                pass
        
        self.test_agent = TestAgent

    def test_capability_with_keyword_args(self):
        """Test capability decorator with proper keyword arguments."""
        
        # This should work fine
        @self.app.capability(
            agent_name="test_agent",
            name="test_capability",
            description="Test capability"
        )
        def test_capability(text: str) -> str:
            return text
            
        # Verify the capability was registered
        self.assertIn("test_capability", self.app.registry.capabilities)
        
    def test_capability_without_agent_name(self):
        """Test capability decorator without agent_name should raise ValueError."""
        
        with self.assertRaises(ValueError):
            @self.app.capability(
                name="test_capability_2"
            )
            def test_capability_2(text: str) -> str:
                return text
                
    def test_capability_with_empty_agent_name(self):
        """Test capability decorator with empty agent_name should raise ValueError."""
        
        with self.assertRaises(ValueError):
            @self.app.capability(
                agent_name="",
                name="test_capability_3"
            )
            def test_capability_3(text: str) -> str:
                return text

    def test_capability_without_name(self):
        """Test capability decorator without name should use function name."""
        
        @self.app.capability(
            agent_name="test_agent"
        )
        def test_capability_4(text: str) -> str:
            return text
            
        # Verify the capability was registered with function name
        self.assertIn("test_capability_4", self.app.registry.capabilities)
        
    @patch('openagents_json.core.decorators.extract_schema_from_function')
    def test_capability_extracts_schema(self, mock_extract):
        """Test that capability decorator extracts schema from function."""
        mock_extract.return_value = ({}, {})
        
        @self.app.capability(
            agent_name="test_agent",
            name="test_capability_5"
        )
        def test_capability_5(text: str) -> str:
            return text
            
        # Verify extract_schema_from_function was called
        mock_extract.assert_called_once()
        
    def test_capability_with_positional_args_fails(self):
        """Test capability decorator with positional arguments should fail."""
        
        # This is designed to fail with TypeError because agent_name must be a keyword arg
        with self.assertRaises(TypeError):
            # The following line is purposefully using incorrect syntax to test the validation
            # The TypeError will be raised by Python itself due to the * in the parameter list
            @self.app.capability("test_agent", name="test_capability_6")
            def test_capability_6(text: str) -> str:
                return text


if __name__ == "__main__":
    unittest.main() 