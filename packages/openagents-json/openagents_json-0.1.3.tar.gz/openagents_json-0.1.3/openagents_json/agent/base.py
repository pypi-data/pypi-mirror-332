"""
Base Agent Classes for OpenAgents JSON.

This module defines the base classes and interfaces for all agent types in the
OpenAgents JSON framework. These include abstract base classes, lifecycle methods,
and common agent functionality.
"""

import abc
import asyncio
import logging
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Type, Union

from openagents_json.core.registry import ComponentMetadata

logger = logging.getLogger(__name__)


@dataclass
class AgentState:
    """State object for tracking agent execution context."""

    agent_id: str
    session_id: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    memory: Dict[str, Any] = field(default_factory=dict)
    context: Dict[str, Any] = field(default_factory=dict)


class BaseAgent(abc.ABC):
    """
    Abstract base class for all agents.
    
    This class defines the core interface that all agents must implement,
    including lifecycle methods and execution patterns.
    """

    def __init__(self, name: str, **kwargs):
        """
        Initialize the base agent.
        
        Args:
            name: The name of the agent
            **kwargs: Additional configuration parameters
        """
        self.name = name
        self.agent_id = str(uuid.uuid4())
        self.metadata = ComponentMetadata.from_component(self.__class__, name)
        self.state = AgentState(agent_id=self.agent_id, session_id=str(uuid.uuid4()))
        self.capabilities = {}
        self._initialized = False
        
        # Set additional attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    @abc.abstractmethod
    async def initialize(self) -> bool:
        """
        Initialize the agent and its resources.
        
        This method should be called before the agent is used and should handle
        loading models, connecting to external services, and other setup tasks.
        
        Returns:
            bool: True if initialization was successful, False otherwise
        """
        self._initialized = True
        return True
        
    @abc.abstractmethod
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with the given inputs.
        
        This is the main method for agent execution and should handle the core
        agent logic, including calling capabilities and tools.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            Dictionary of output values
        """
        if not self._initialized:
            await self.initialize()
        return {}
    
    async def validate(self, inputs: Dict[str, Any]) -> bool:
        """
        Validate that the inputs meet the agent's requirements.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            True if inputs are valid, False otherwise
        """
        return True
        
    async def cleanup(self) -> None:
        """
        Clean up any resources used by the agent.
        
        This method should be called when the agent is no longer needed
        and should handle releasing models, closing connections, etc.
        """
        pass
    
    def add_capability(self, name: str, capability_func, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a capability to the agent.
        
        Args:
            name: Name of the capability
            capability_func: Function implementing the capability
            metadata: Optional metadata about the capability
        """
        if metadata is None:
            metadata = {}
        
        self.capabilities[name] = {
            "func": capability_func,
            "metadata": metadata
        }
    
    async def call_capability(self, name: str, **kwargs) -> Any:
        """
        Call a capability by name with the given arguments.
        
        Args:
            name: Name of the capability to call
            **kwargs: Arguments to pass to the capability
            
        Returns:
            The result of the capability execution
            
        Raises:
            ValueError: If the capability does not exist
        """
        if name not in self.capabilities:
            raise ValueError(f"Capability '{name}' not found")
        
        capability = self.capabilities[name]
        return await capability["func"](self, **kwargs)
    
    def update_state(self, **kwargs) -> None:
        """
        Update the agent's state with the given values.
        
        Args:
            **kwargs: Key-value pairs to update in the state
        """
        for key, value in kwargs.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)
            else:
                self.state.context[key] = value
        
        self.state.updated_at = datetime.now()
    
    def __str__(self) -> str:
        """Return a string representation of the agent."""
        return f"{self.__class__.__name__}(name={self.name}, id={self.agent_id})"
    
    def __repr__(self) -> str:
        """Return a detailed string representation of the agent."""
        return (f"{self.__class__.__name__}(name={self.name}, "
                f"id={self.agent_id}, capabilities={list(self.capabilities.keys())})")


class LLMAgent(BaseAgent):
    """
    Base class for Language Model-based agents.
    
    This class extends BaseAgent with functionality specific to language model agents,
    including prompt management, generation parameters, and response handling.
    """
    
    def __init__(self, name: str, model: str, **kwargs):
        """
        Initialize an LLM-based agent.
        
        Args:
            name: Name of the agent
            model: Identifier for the language model to use
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, **kwargs)
        self.model = model
        self.prompts = {}
        self.generation_params = kwargs.get("generation_params", {})
    
    async def initialize(self) -> bool:
        """
        Initialize the LLM agent.
        
        This method handles loading the language model and preparing resources.
        
        Returns:
            True if initialization was successful, False otherwise
        """
        # Implementation would handle LLM initialization
        logger.info(f"Initializing LLM agent with model: {self.model}")
        return await super().initialize()
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the LLM agent with the given inputs.
        
        This method handles preparing prompts, calling the LLM, and processing responses.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            Dictionary with the LLM response and any additional outputs
        """
        if not self._initialized:
            await self.initialize()
        
        # Basic implementation - would be extended in actual implementation
        prompt = self._prepare_prompt(inputs)
        response = await self._generate(prompt)
        
        return {
            "response": response,
            "model": self.model,
            "inputs": inputs,
        }
    
    async def _generate(self, prompt: str) -> str:
        """
        Generate a response using the language model.
        
        Args:
            prompt: The input prompt for the language model
            
        Returns:
            The generated response text
        """
        # This would be implemented to call the actual LLM API
        logger.info(f"Generating response for prompt: {prompt[:50]}...")
        return f"LLM response for {self.model} (placeholder)"
    
    def _prepare_prompt(self, inputs: Dict[str, Any]) -> str:
        """
        Prepare the prompt from the inputs.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            The formatted prompt string
        """
        # Basic implementation - would be extended based on use case
        if "prompt" in inputs:
            return inputs["prompt"]
        elif "messages" in inputs:
            # Simple conversion of chat format to text
            return "\n".join([f"{m.get('role', 'user')}: {m.get('content', '')}" 
                             for m in inputs["messages"]])
        else:
            return str(inputs)
    
    def add_prompt(self, name: str, template: str) -> None:
        """
        Add a prompt template to the agent.
        
        Args:
            name: Name of the prompt template
            template: The prompt template string
        """
        self.prompts[name] = template
    
    def format_prompt(self, name: str, **kwargs) -> str:
        """
        Format a prompt template with the given parameters.
        
        Args:
            name: Name of the prompt template
            **kwargs: Parameters to insert into the template
            
        Returns:
            The formatted prompt string
            
        Raises:
            ValueError: If the prompt template does not exist
        """
        if name not in self.prompts:
            raise ValueError(f"Prompt template '{name}' not found")
        
        template = self.prompts[name]
        return template.format(**kwargs)


class ToolAgent(BaseAgent):
    """
    Base class for Tool-using agents.
    
    This class extends BaseAgent with functionality for using tools,
    including tool registration, execution, and result handling.
    """
    
    def __init__(self, name: str, **kwargs):
        """
        Initialize a tool-using agent.
        
        Args:
            name: Name of the agent
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, **kwargs)
        self.tools = {}
    
    async def initialize(self) -> bool:
        """
        Initialize the tool agent.
        
        This method handles setting up tools and preparing resources.
        
        Returns:
            True if initialization was successful, False otherwise
        """
        logger.info(f"Initializing tool agent: {self.name}")
        return await super().initialize()
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the tool agent with the given inputs.
        
        This method handles determining which tools to use and executing them.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            Dictionary with the tool execution results
        """
        if not self._initialized:
            await self.initialize()
        
        # Basic implementation - would be extended in actual implementation
        tool_name = inputs.get("tool", None)
        if tool_name and tool_name in self.tools:
            tool_result = await self.call_tool(tool_name, **inputs.get("tool_inputs", {}))
            return {"result": tool_result, "tool": tool_name}
        else:
            # Execute all tools sequentially as a basic implementation
            results = {}
            for tool_name in self.tools:
                results[tool_name] = await self.call_tool(tool_name, **inputs)
            return {"results": results}
    
    def add_tool(self, name: str, tool_func, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Add a tool to the agent.
        
        Args:
            name: Name of the tool
            tool_func: Function implementing the tool
            metadata: Optional metadata about the tool
        """
        if metadata is None:
            metadata = {}
        
        self.tools[name] = {
            "func": tool_func,
            "metadata": metadata
        }
    
    async def call_tool(self, name: str, **kwargs) -> Any:
        """
        Call a tool by name with the given arguments.
        
        Args:
            name: Name of the tool to call
            **kwargs: Arguments to pass to the tool
            
        Returns:
            The result of the tool execution
            
        Raises:
            ValueError: If the tool does not exist
        """
        if name not in self.tools:
            raise ValueError(f"Tool '{name}' not found")
        
        tool = self.tools[name]
        tool_func = tool["func"]
        
        # Update state before tool execution
        self.update_state(last_tool=name, last_tool_inputs=kwargs)
        
        # Call the tool
        result = await tool_func(**kwargs) if asyncio.iscoroutinefunction(tool_func) else tool_func(**kwargs)
        
        # Update state after tool execution
        self.update_state(last_tool_result=result)
        
        return result


class WorkflowAgent(BaseAgent):
    """
    Base class for Workflow-based agents.
    
    This class extends BaseAgent with functionality for executing workflows,
    including step management, state tracking, and error handling.
    """
    
    def __init__(self, name: str, workflow_id: Optional[str] = None, **kwargs):
        """
        Initialize a workflow-based agent.
        
        Args:
            name: Name of the agent
            workflow_id: Optional ID of the workflow to execute
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, **kwargs)
        self.workflow_id = workflow_id
        self.steps = []
        self.current_step = 0
    
    async def initialize(self) -> bool:
        """
        Initialize the workflow agent.
        
        This method handles loading the workflow definition and preparing resources.
        
        Returns:
            True if initialization was successful, False otherwise
        """
        logger.info(f"Initializing workflow agent with workflow: {self.workflow_id}")
        
        # Would load the workflow definition here
        return await super().initialize()
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the workflow with the given inputs.
        
        This method handles executing each step of the workflow in sequence,
        managing state between steps, and handling errors.
        
        Args:
            inputs: Dictionary of input parameters
            
        Returns:
            Dictionary with the workflow execution results
        """
        if not self._initialized:
            await self.initialize()
        
        # Basic implementation - would be extended in actual implementation
        if not self.steps:
            return {"error": "No workflow steps defined"}
        
        step_results = []
        current_inputs = inputs
        
        for i, step in enumerate(self.steps):
            self.current_step = i
            try:
                step_result = await self._execute_step(step, current_inputs)
                step_results.append(step_result)
                
                # Use the output of this step as input to the next step
                if "outputs" in step_result:
                    current_inputs = {**current_inputs, **step_result["outputs"]}
            
            except Exception as e:
                logger.error(f"Error executing workflow step {i}: {str(e)}")
                return {
                    "error": f"Step {i} failed: {str(e)}",
                    "partial_results": step_results,
                    "completed_steps": i
                }
        
        return {
            "results": step_results,
            "completed_steps": len(self.steps),
            "final_state": current_inputs
        }
    
    async def _execute_step(self, step: Dict[str, Any], inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single workflow step.
        
        Args:
            step: The step definition
            inputs: The inputs for this step
            
        Returns:
            The results of the step execution
        """
        # This would be implemented based on the workflow system
        step_type = step.get("type", "unknown")
        step_id = step.get("id", f"step_{self.current_step}")
        
        logger.info(f"Executing workflow step {self.current_step} (type: {step_type}, id: {step_id})")
        
        # Very basic placeholder implementation
        if step_type == "agent":
            agent_name = step.get("agent", "")
            # Would get the agent from registry and execute
            return {"outputs": {"result": f"Executed agent {agent_name}"}}
        
        elif step_type == "tool":
            tool_name = step.get("tool", "")
            # Would get the tool from registry and execute
            return {"outputs": {"result": f"Executed tool {tool_name}"}}
        
        else:
            return {"outputs": {"result": f"Executed unknown step type {step_type}"}}
    
    def add_step(self, step_def: Dict[str, Any]) -> None:
        """
        Add a step to the workflow.
        
        Args:
            step_def: The step definition
        """
        self.steps.append(step_def)
    
    def set_workflow(self, workflow_id: str, steps: List[Dict[str, Any]]) -> None:
        """
        Set the workflow for this agent.
        
        Args:
            workflow_id: The ID of the workflow
            steps: The list of step definitions
        """
        self.workflow_id = workflow_id
        self.steps = steps
        self.current_step = 0 