"""
Workflow integration for OpenAgents JSON agents.

This module provides utilities for integrating agents with the workflow system,
including step creation, workflow execution, and agent-to-workflow conversion.
"""

import logging
from typing import Any, Dict, List, Optional, TypeVar, Union

from openagents_json.agent.base import BaseAgent, LLMAgent, ToolAgent
from openagents_json.agent.monitoring import agent_monitor

logger = logging.getLogger(__name__)


class AgentStep:
    """
    Represents an agent as a workflow step.
    
    This class wraps an agent as a workflow step that can be executed
    as part of a workflow.
    """
    
    def __init__(
        self,
        agent: BaseAgent,
        step_id: str,
        input_mapping: Optional[Dict[str, str]] = None,
        output_mapping: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize an agent step.
        
        Args:
            agent: The agent to execute
            step_id: ID for this step
            input_mapping: Optional mapping from workflow inputs to agent inputs
            output_mapping: Optional mapping from agent outputs to workflow outputs
        """
        self.agent = agent
        self.step_id = step_id
        self.input_mapping = input_mapping or {}
        self.output_mapping = output_mapping or {}
    
    async def execute(self, workflow_inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent as a workflow step.
        
        Args:
            workflow_inputs: The inputs from the workflow
            
        Returns:
            The mapped outputs from the agent
        """
        # Map inputs from workflow to agent
        agent_inputs = {}
        for agent_input, workflow_input in self.input_mapping.items():
            if workflow_input in workflow_inputs:
                agent_inputs[agent_input] = workflow_inputs[workflow_input]
        
        # Execute the agent with monitoring
        @agent_monitor.track_workflow_step(
            workflow_id=f"workflow_with_{self.agent.name}",
            step_id=self.step_id,
            step_type=f"agent_{self.agent.__class__.__name__}"
        )
        async def _execute_agent():
            return await self.agent.execute(agent_inputs)
        
        agent_outputs = await _execute_agent()
        
        # Map outputs from agent to workflow
        workflow_outputs = {}
        for workflow_output, agent_output in self.output_mapping.items():
            if agent_output in agent_outputs:
                workflow_outputs[workflow_output] = agent_outputs[agent_output]
            elif workflow_output == agent_output and agent_output in agent_outputs:
                # If keys match, copy directly
                workflow_outputs[workflow_output] = agent_outputs[agent_output]
        
        # Also include all agent outputs if no mapping is provided
        if not self.output_mapping:
            workflow_outputs = agent_outputs
        
        return workflow_outputs


class SequentialAgentWorkflow:
    """
    A simple workflow that executes agents in sequence.
    
    This class allows defining a workflow as a sequence of agents
    that are executed one after another, with outputs from one agent
    being passed as inputs to the next.
    """
    
    def __init__(
        self,
        name: str,
        description: str = "",
        version: str = "0.1.0",
    ):
        """
        Initialize a sequential agent workflow.
        
        Args:
            name: Name of the workflow
            description: Description of the workflow
            version: Version of the workflow
        """
        self.name = name
        self.description = description
        self.version = version
        self.steps: List[AgentStep] = []
        self.workflow_id = f"{name}_v{version}"
    
    def add_agent(
        self,
        agent: BaseAgent,
        step_id: Optional[str] = None,
        input_mapping: Optional[Dict[str, str]] = None,
        output_mapping: Optional[Dict[str, str]] = None,
    ) -> "SequentialAgentWorkflow":
        """
        Add an agent to the workflow.
        
        Args:
            agent: The agent to add
            step_id: Optional ID for this step (defaults to agent name)
            input_mapping: Optional mapping from workflow inputs to agent inputs
            output_mapping: Optional mapping from agent outputs to workflow outputs
            
        Returns:
            This workflow instance for chaining
        """
        step_id = step_id or f"{agent.name}_step_{len(self.steps)}"
        step = AgentStep(
            agent=agent,
            step_id=step_id,
            input_mapping=input_mapping,
            output_mapping=output_mapping,
        )
        self.steps.append(step)
        return self
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the workflow with the given inputs.
        
        Args:
            inputs: The inputs for the workflow
            
        Returns:
            The final outputs from the workflow
        """
        current_state = inputs.copy()
        
        for i, step in enumerate(self.steps):
            logger.info(f"Executing workflow step {i+1}/{len(self.steps)}: {step.step_id}")
            
            # Execute the step
            step_result = await step.execute(current_state)
            
            # Update the current state with the step outputs
            current_state.update(step_result)
        
        return current_state


class LLMAgentWorkflowConverter:
    """
    Utility for converting LLM agents to workflow steps.
    
    This class provides methods for turning LLM agents into standard
    workflow steps that can be executed as part of a workflow.
    """
    
    @staticmethod
    def agent_to_workflow_step(
        agent: LLMAgent,
        step_id: Optional[str] = None,
        input_mapping: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Convert an LLM agent to a workflow step definition.
        
        Args:
            agent: The LLM agent to convert
            step_id: Optional ID for the step
            input_mapping: Optional mapping from workflow inputs to agent inputs
            
        Returns:
            Dictionary with the workflow step definition
        """
        step_id = step_id or f"{agent.name}_step"
        
        # Create a basic step definition
        step_def = {
            "id": step_id,
            "type": "llm",
            "name": agent.name,
            "description": agent.metadata.description,
            "model": agent.model,
            "prompt": "{{inputs.prompt}}",  # Default prompt placeholder
            "inputs": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt to send to the LLM"
                }
            },
            "outputs": {
                "response": {
                    "type": "string",
                    "description": "The LLM response"
                }
            }
        }
        
        # Add input mapping if provided
        if input_mapping:
            step_def["input_mapping"] = input_mapping
        
        return step_def


class ToolAgentWorkflowConverter:
    """
    Utility for converting Tool agents to workflow steps.
    
    This class provides methods for turning Tool agents into standard
    workflow steps that can be executed as part of a workflow.
    """
    
    @staticmethod
    def agent_to_workflow_step(
        agent: ToolAgent,
        step_id: Optional[str] = None,
        default_tool: Optional[str] = None,
        input_mapping: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Convert a Tool agent to a workflow step definition.
        
        Args:
            agent: The Tool agent to convert
            step_id: Optional ID for the step
            default_tool: Optional name of the default tool to use
            input_mapping: Optional mapping from workflow inputs to agent inputs
            
        Returns:
            Dictionary with the workflow step definition
        """
        step_id = step_id or f"{agent.name}_step"
        
        # Get the default tool to use
        default_tool = default_tool or (list(agent.tools.keys())[0] if agent.tools else None)
        
        # Create a basic step definition
        step_def = {
            "id": step_id,
            "type": "tool",
            "name": agent.name,
            "description": agent.metadata.description,
            "tool": default_tool,
            "inputs": {
                "tool_inputs": {
                    "type": "object",
                    "description": "The inputs for the tool"
                }
            },
            "outputs": {
                "result": {
                    "type": "any",
                    "description": "The result of the tool execution"
                }
            }
        }
        
        # Add available tools
        if agent.tools:
            step_def["available_tools"] = list(agent.tools.keys())
        
        # Add input mapping if provided
        if input_mapping:
            step_def["input_mapping"] = input_mapping
        
        return step_def


def create_agent_workflow(
    name: str,
    agents: List[BaseAgent],
    description: str = "",
    version: str = "0.1.0",
) -> SequentialAgentWorkflow:
    """
    Create a sequential workflow from a list of agents.
    
    Args:
        name: Name of the workflow
        agents: List of agents to include in the workflow
        description: Description of the workflow
        version: Version of the workflow
        
    Returns:
        A sequential agent workflow
    """
    workflow = SequentialAgentWorkflow(
        name=name,
        description=description,
        version=version,
    )
    
    for agent in agents:
        workflow.add_agent(agent)
    
    return workflow


def agent_to_workflow_definition(
    agent: BaseAgent,
    workflow_name: Optional[str] = None,
    workflow_description: str = "",
    workflow_version: str = "0.1.0",
) -> Dict[str, Any]:
    """
    Convert an agent to a workflow definition.
    
    This creates a simple workflow definition that wraps a single agent.
    
    Args:
        agent: The agent to convert
        workflow_name: Optional name for the workflow (defaults to agent name)
        workflow_description: Description for the workflow
        workflow_version: Version for the workflow
        
    Returns:
        Dictionary with the workflow definition
    """
    workflow_name = workflow_name or f"{agent.name}_workflow"
    
    # Create a step definition based on agent type
    if isinstance(agent, LLMAgent):
        step_def = LLMAgentWorkflowConverter.agent_to_workflow_step(agent)
    elif isinstance(agent, ToolAgent):
        step_def = ToolAgentWorkflowConverter.agent_to_workflow_step(agent)
    else:
        # Generic agent step
        step_def = {
            "id": f"{agent.name}_step",
            "type": "agent",
            "name": agent.name,
            "description": agent.metadata.description,
            "agent_id": agent.agent_id,
            "inputs": {
                "agent_inputs": {
                    "type": "object",
                    "description": "The inputs for the agent"
                }
            },
            "outputs": {
                "agent_outputs": {
                    "type": "object",
                    "description": "The outputs from the agent"
                }
            }
        }
    
    # Create the workflow definition
    workflow_def = {
        "id": f"{workflow_name}_v{workflow_version}",
        "name": workflow_name,
        "description": workflow_description or f"Workflow for {agent.name}",
        "version": workflow_version,
        "steps": [step_def],
        "inputs": step_def.get("inputs", {}),
        "outputs": step_def.get("outputs", {})
    }
    
    return workflow_def 