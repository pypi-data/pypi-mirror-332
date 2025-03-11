"""
Tests for Pydantic v2 compatibility changes.

This module tests the Pydantic models with Literal types and ConfigDict
to ensure they function correctly.
"""

import unittest

from pydantic import ValidationError

from openagents_json.agent.config import (
    AgentConfigModel,
    LLMAgentConfigModel,
    ToolAgentConfigModel,
    WorkflowAgentConfigModel
)


class PydanticConfigTests(unittest.TestCase):
    """Test cases for Pydantic v2 compatibility."""

    def test_llm_agent_config_model(self):
        """Test LLMAgentConfigModel with Literal agent_type."""
        # Valid configuration
        config = LLMAgentConfigModel(
            name="test_agent",
            model="gpt-4"
        )
        
        # Verify agent_type is set to "llm"
        self.assertEqual(config.agent_type, "llm")
        
        # Trying to set agent_type to a different value should raise ValidationError
        with self.assertRaises(ValidationError):
            LLMAgentConfigModel(
                name="test_agent",
                model="gpt-4",
                agent_type="tool"  # This should fail
            )
    
    def test_tool_agent_config_model(self):
        """Test ToolAgentConfigModel with Literal agent_type."""
        # Valid configuration
        config = ToolAgentConfigModel(
            name="test_tool_agent",
            tools=["tool1", "tool2"]
        )
        
        # Verify agent_type is set to "tool"
        self.assertEqual(config.agent_type, "tool")
        
        # Trying to set agent_type to a different value should raise ValidationError
        with self.assertRaises(ValidationError):
            ToolAgentConfigModel(
                name="test_tool_agent",
                tools=["tool1", "tool2"],
                agent_type="llm"  # This should fail
            )
    
    def test_workflow_agent_config_model(self):
        """Test WorkflowAgentConfigModel with Literal agent_type."""
        # Valid configuration
        config = WorkflowAgentConfigModel(
            name="test_workflow_agent",
            workflow_id="workflow1"
        )
        
        # Verify agent_type is set to "workflow"
        self.assertEqual(config.agent_type, "workflow")
        
        # Trying to set agent_type to a different value should raise ValidationError
        with self.assertRaises(ValidationError):
            WorkflowAgentConfigModel(
                name="test_workflow_agent",
                workflow_id="workflow1",
                agent_type="llm"  # This should fail
            )
    
    def test_config_dict_extra_allow(self):
        """Test that ConfigDict extra='allow' works."""
        # Add an extra field that's not defined in the model
        config = LLMAgentConfigModel(
            name="test_agent",
            model="gpt-4",
            extra_field="extra value"  # This should be allowed
        )
        
        # Verify the extra field was added
        self.assertEqual(config.extra_field, "extra value")
    
    def test_model_validation(self):
        """Test model validation for required fields."""
        # Missing required field 'name'
        with self.assertRaises(ValidationError):
            LLMAgentConfigModel(
                model="gpt-4"
            )
        
        # Missing required field 'model'
        with self.assertRaises(ValidationError):
            LLMAgentConfigModel(
                name="test_agent"
            )
            
        # Missing required field 'workflow_id'
        with self.assertRaises(ValidationError):
            WorkflowAgentConfigModel(
                name="test_workflow_agent"
            )


if __name__ == "__main__":
    unittest.main() 