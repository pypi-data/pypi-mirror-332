"""
Job executor for OpenAgents JSON.

This module provides the JobExecutor class for executing jobs with state
management support.
"""

import asyncio
import logging
import time
from typing import Any, Dict, List, Optional, Tuple, Type, Union

from openagents_json.agent.base import BaseAgent
from openagents_json.core.state import get_state_manager, StateManager
from openagents_json.job.context import JobContext

logger = logging.getLogger(__name__)


class JobExecutor:
    """
    Executes job steps with state management.
    
    JobExecutor handles the execution of job steps, including state persistence
    between steps and across processes.
    """
    
    def __init__(self, state_manager: Optional[StateManager] = None):
        """
        Initialize the job executor.
        
        Args:
            state_manager: Optional custom state manager
        """
        self.state_manager = state_manager or get_state_manager()
    
    async def execute_step(
        self, agent: BaseAgent, inputs: Dict[str, Any], context: JobContext
    ) -> Tuple[Dict[str, Any], JobContext]:
        """
        Execute a single job step with state management.
        
        Args:
            agent: Agent to execute the step
            inputs: Input parameters for the step
            context: Job context information
            
        Returns:
            Tuple of (step outputs, updated context)
        """
        # Set agent ID in context if not present
        if context.agent_id is None:
            context.agent_id = agent.agent_id
        
        # Load agent state if we have a state checkpoint
        if context.state_checkpoint:
            logger.debug(f"Loading state from checkpoint {context.state_checkpoint}")
            snapshot = self.state_manager.get_state(
                agent.agent_id, f"snapshot_{context.state_checkpoint}", None
            )
            if snapshot:
                logger.info(f"Restoring agent state from checkpoint {context.state_checkpoint}")
                agent.restore_from_snapshot(snapshot)
            else:
                logger.warning(f"State checkpoint {context.state_checkpoint} not found")
        
        # Execute the agent with transaction support
        async with self.transaction():
            # Execute the agent
            outputs = await agent.execute(inputs)
            
            # Save agent state after execution
            snapshot = agent.get_state_snapshot()
            checkpoint_id = context.create_checkpoint()
            self.state_manager.set_state(
                agent.agent_id, f"snapshot_{checkpoint_id}", snapshot
            )
            
            logger.info(f"Saved agent state to checkpoint {checkpoint_id}")
            
            return outputs, context
    
    async def transaction(self):
        """
        Context manager for transaction handling.
        
        Example:
            ```python
            async with executor.transaction():
                # Operations within a transaction
                outputs = await agent.execute(inputs)
            ```
            
        Yields:
            Transaction context
        """
        self.state_manager.begin_transaction()
        try:
            yield
            self.state_manager.commit_transaction()
        except Exception as e:
            logger.exception("Error during job execution, rolling back transaction")
            self.state_manager.rollback_transaction()
            raise e


def execute_step_in_process(
    agent_class: Type[BaseAgent],
    agent_kwargs: Dict[str, Any],
    inputs: Dict[str, Any],
    context_dict: Dict[str, Any],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Execute a step in a separate process.
    
    This function is designed to be called by multiprocessing.Process to execute
    a job step in a separate process.
    
    Args:
        agent_class: Agent class to instantiate
        agent_kwargs: Arguments for agent constructor
        inputs: Input parameters for the step
        context_dict: Job context as a dictionary
        
    Returns:
        Tuple of (step outputs, updated context as dict)
    """
    # Set up state manager
    state_manager = get_state_manager()
    
    # Create agent instance with state manager
    agent_kwargs["state_manager"] = state_manager
    agent = agent_class(**agent_kwargs)
    
    # Convert context back to object
    context = JobContext.from_dict(context_dict)
    
    # Create executor
    executor = JobExecutor(state_manager)
    
    # Run execution sync in this process
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        outputs, updated_context = loop.run_until_complete(
            executor.execute_step(agent, inputs, context)
        )
        
        # Return results as serializable dictionaries
        return outputs, updated_context.to_dict()
    finally:
        loop.close() 