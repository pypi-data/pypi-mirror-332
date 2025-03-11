"""
LLM Agent Examples for OpenAgents JSON.

This module demonstrates how to create LLM-based agents
using the decorator pattern.
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional

from openagents_json.agent.base import LLMAgent
from openagents_json.agent.capabilities import Capability

logger = logging.getLogger(__name__)


class SimpleCompletion(LLMAgent):
    """
    A simple LLM agent that provides text completion.
    
    This agent demonstrates basic LLM functionality with prompt templates
    and generation parameters.
    """
    
    def __init__(self, name: str, model: str = "gpt-3.5-turbo", **kwargs):
        """
        Initialize the simple completion agent.
        
        Args:
            name: Name of the agent
            model: Name of the LLM model to use
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, model, **kwargs)
        
        # Add prompt templates
        self.add_prompt("default", "You are a helpful assistant. {prompt}")
        self.add_prompt("summarize", "Summarize the following text in {num_sentences} sentences: {text}")
        self.add_prompt("translate", "Translate the following text from {source_language} to {target_language}: {text}")
        
        # Set default generation parameters
        self.generation_params = {
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 500),
            "top_p": kwargs.get("top_p", 1.0),
        }
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with the given inputs.
        
        Args:
            inputs: Dictionary with the following possible keys:
                - prompt: The prompt to send to the LLM
                - template: Name of the prompt template to use
                - template_vars: Variables for the prompt template
                - generation_params: Override default generation parameters
                
        Returns:
            Dictionary with the LLM response
        """
        if not self._initialized:
            await self.initialize()
        
        # Check if a template is specified
        if "template" in inputs and inputs["template"] in self.prompts:
            template_name = inputs["template"]
            template_vars = inputs.get("template_vars", {})
            prompt = self.format_prompt(template_name, **template_vars)
        else:
            # Use the provided prompt or default template
            if "prompt" in inputs:
                if "default" in self.prompts:
                    prompt = self.format_prompt("default", prompt=inputs["prompt"])
                else:
                    prompt = inputs["prompt"]
            else:
                return {"error": "No prompt or valid template provided"}
        
        # Override generation parameters if provided
        gen_params = self.generation_params.copy()
        if "generation_params" in inputs and isinstance(inputs["generation_params"], dict):
            gen_params.update(inputs["generation_params"])
        
        # Generate response
        response = await self._generate(prompt)
        
        return {
            "response": response,
            "model": self.model,
            "prompt": prompt,
            "generation_params": gen_params
        }
    
    async def _generate(self, prompt: str) -> str:
        """
        Generate a response using the language model.
        
        In a real implementation, this would call an actual LLM API.
        
        Args:
            prompt: The input prompt for the language model
            
        Returns:
            The generated response text
        """
        logger.info(f"Generating response for prompt: {prompt[:50]}...")
        
        # This is a mock implementation
        # In a real implementation, this would call an actual LLM API
        await asyncio.sleep(0.5)  # Simulate API call latency
        
        # Return a mock response
        if "summarize" in prompt.lower():
            return "This is a summary of the provided text."
        elif "translate" in prompt.lower():
            return "This is a translation of the provided text."
        else:
            return f"This is a response from {self.model} to your prompt."


class ChatAgent(LLMAgent):
    """
    An LLM agent that supports chat-style interactions.
    
    This agent demonstrates handling chat history and
    maintaining conversation context.
    """
    
    def __init__(self, name: str, model: str = "gpt-3.5-turbo", **kwargs):
        """
        Initialize the chat agent.
        
        Args:
            name: Name of the agent
            model: Name of the LLM model to use
            **kwargs: Additional configuration parameters
        """
        super().__init__(name, model, **kwargs)
        
        # Initialize chat history
        self.state.context["chat_history"] = []
        
        # Add system prompt
        self.system_prompt = kwargs.get("system_prompt", "You are a helpful assistant.")
    
    async def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent with the given inputs.
        
        Args:
            inputs: Dictionary with the following possible keys:
                - message: The user message
                - clear_history: Whether to clear chat history
                - system_prompt: Override the system prompt
                - generation_params: Override default generation parameters
                
        Returns:
            Dictionary with the LLM response and updated chat history
        """
        if not self._initialized:
            await self.initialize()
        
        # Check if we should clear history
        if inputs.get("clear_history", False):
            self.state.context["chat_history"] = []
        
        # Get or update system prompt
        if "system_prompt" in inputs:
            self.system_prompt = inputs["system_prompt"]
        
        # Get user message
        if "message" not in inputs:
            return {"error": "No message provided"}
        
        user_message = inputs["message"]
        
        # Add user message to history
        self.state.context["chat_history"].append({"role": "user", "content": user_message})
        
        # Prepare messages for the LLM
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.state.context["chat_history"])
        
        # Generate response
        response = await self._chat_generate(messages)
        
        # Add assistant response to history
        self.state.context["chat_history"].append({"role": "assistant", "content": response})
        
        return {
            "response": response,
            "model": self.model,
            "chat_history": self.state.context["chat_history"]
        }
    
    async def _chat_generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Generate a response using the language model in chat mode.
        
        In a real implementation, this would call an actual LLM API.
        
        Args:
            messages: The chat messages
            
        Returns:
            The generated response text
        """
        logger.info(f"Generating chat response with {len(messages)} messages")
        
        # This is a mock implementation
        # In a real implementation, this would call an actual LLM API
        await asyncio.sleep(0.5)  # Simulate API call latency
        
        # Get the last user message
        last_user_message = None
        for message in reversed(messages):
            if message["role"] == "user":
                last_user_message = message["content"]
                break
        
        # Return a mock response
        if last_user_message:
            return f"This is a response from {self.model} to: {last_user_message[:30]}..."
        else:
            return f"This is a response from {self.model}."
    
    @Capability.register(name="get_chat_history")
    async def get_chat_history(self) -> List[Dict[str, str]]:
        """
        Get the chat history.
        
        Returns:
            The chat history
        """
        return self.state.context.get("chat_history", [])
    
    @Capability.register(name="clear_chat_history")
    async def clear_chat_history(self) -> bool:
        """
        Clear the chat history.
        
        Returns:
            True if the history was cleared
        """
        self.state.context["chat_history"] = []
        return True


# Example usage
async def example():
    """Example of using the LLM agents."""
    # Simple completion example
    completion_agent = SimpleCompletion("example_completion_agent")
    await completion_agent.initialize()
    
    completion_result = await completion_agent.execute({
        "prompt": "What is the capital of France?"
    })
    print(f"Completion result: {completion_result}")
    
    template_result = await completion_agent.execute({
        "template": "summarize",
        "template_vars": {
            "text": "This is a long text that needs to be summarized. It contains multiple sentences and ideas.",
            "num_sentences": 2
        }
    })
    print(f"Template result: {template_result}")
    
    # Chat agent example
    chat_agent = ChatAgent("example_chat_agent")
    await chat_agent.initialize()
    
    chat_result1 = await chat_agent.execute({
        "message": "Hello, how are you?"
    })
    print(f"Chat result 1: {chat_result1}")
    
    chat_result2 = await chat_agent.execute({
        "message": "What's the weather like today?"
    })
    print(f"Chat result 2: {chat_result2}")
    
    # Get chat history
    history = await chat_agent.call_capability("get_chat_history")
    print(f"Chat history: {history}")


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Run the example
    asyncio.run(example()) 