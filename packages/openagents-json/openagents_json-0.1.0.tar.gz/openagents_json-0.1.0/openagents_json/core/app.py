"""
Main application class for OpenAgents JSON.
"""

import inspect
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, create_model

from openagents_json.settings import Settings, settings


T = TypeVar("T")
AgentType = TypeVar("AgentType", bound=Type[Any])
CapabilityFunc = TypeVar("CapabilityFunc", bound=Callable[..., Any])


class AgentRegistry:
    """Registry for agents and their capabilities."""
    
    def __init__(self):
        self.agents: Dict[str, Dict[str, Any]] = {}
        self.capabilities: Dict[str, Dict[str, Callable]] = {}
        self.tools: Dict[str, Callable] = {}
        
    def register_agent(self, name: str, agent_cls: Type[Any], metadata: Dict[str, Any]) -> None:
        """Register an agent class."""
        self.agents[name] = {
            "cls": agent_cls,
            "metadata": metadata,
            "capabilities": {}
        }
        self.capabilities[name] = {}
        
    def register_capability(
        self, 
        agent_name: str, 
        capability_name: str, 
        func: Callable, 
        metadata: Dict[str, Any]
    ) -> None:
        """Register a capability for an agent."""
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not registered")
        
        self.capabilities[agent_name][capability_name] = func
        self.agents[agent_name]["capabilities"][capability_name] = metadata
        
    def register_tool(self, name: str, func: Callable, metadata: Dict[str, Any]) -> None:
        """Register a standalone tool."""
        self.tools[name] = func


class WorkflowRegistry:
    """Registry for workflows."""
    
    def __init__(self):
        self.workflows: Dict[str, Dict[str, Any]] = {}
        
    def register_workflow(self, workflow_def: Dict[str, Any]) -> None:
        """Register a workflow definition."""
        if "id" not in workflow_def:
            raise ValueError("Workflow definition must include an 'id' field")
        
        workflow_id = workflow_def["id"]
        self.workflows[workflow_id] = workflow_def


class JobManager:
    """Manager for workflow execution jobs."""
    
    def __init__(self):
        self.jobs: Dict[str, Dict[str, Any]] = {}
        self.job_counter = 0
        
    async def create_job(self, workflow_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new job from a workflow definition."""
        job_id = f"job_{self.job_counter}"
        self.job_counter += 1
        
        job = {
            "id": job_id,
            "workflow_id": workflow_id,
            "inputs": inputs,
            "status": "CREATED",
            "created_at": "__TIMESTAMP__",  # Placeholder
            "steps": {},
            "outputs": {}
        }
        
        self.jobs[job_id] = job
        return job
        
    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        """Get the status of a job."""
        if job_id not in self.jobs:
            raise ValueError(f"Job {job_id} not found")
        
        job = self.jobs[job_id]
        return {
            "id": job["id"],
            "status": job["status"],
            "created_at": job["created_at"]
        }
        
    async def get_job_results(self, job_id: str) -> Dict[str, Any]:
        """Get the results of a completed job."""
        if job_id not in self.jobs:
            raise ValueError(f"Job {job_id} not found")
        
        job = self.jobs[job_id]
        if job["status"] != "COMPLETED":
            raise ValueError(f"Job {job_id} is not completed")
        
        return {
            "id": job["id"],
            "outputs": job["outputs"]
        }


class OpenAgentsApp:
    """
    Main application class for OpenAgents JSON.
    
    This class serves as the entry point for the framework, providing methods
    for registering agents, defining workflows, and managing jobs.
    """
    
    def __init__(self, settings: Optional[Settings] = None):
        """
        Initialize the OpenAgents application.
        
        Args:
            settings: Custom settings for the application. If None, global settings are used.
        """
        self.settings = settings or settings
        self.agent_registry = AgentRegistry()
        self.workflow_registry = WorkflowRegistry()
        self.job_manager = JobManager()
        self.router = APIRouter()
        
        # Register API routes
        self._setup_routes()
        
    def _setup_routes(self) -> None:
        """Set up API routes for the application."""
        # Agents API
        self.router.add_api_route(
            "/agents",
            self._get_agents,
            methods=["GET"],
            response_model=List[Dict[str, Any]],
            summary="List all registered agents",
            tags=["agents"]
        )
        
        # Workflows API
        self.router.add_api_route(
            "/workflows",
            self._get_workflows,
            methods=["GET"],
            response_model=List[Dict[str, Any]],
            summary="List all registered workflows",
            tags=["workflows"]
        )
        
        # Jobs API
        self.router.add_api_route(
            "/jobs",
            self._create_job,
            methods=["POST"],
            response_model=Dict[str, Any],
            summary="Create a new job",
            tags=["jobs"]
        )
        
        self.router.add_api_route(
            "/jobs/{job_id}/status",
            self._get_job_status,
            methods=["GET"],
            response_model=Dict[str, Any],
            summary="Get job status",
            tags=["jobs"]
        )
        
        self.router.add_api_route(
            "/jobs/{job_id}/results",
            self._get_job_results,
            methods=["GET"],
            response_model=Dict[str, Any],
            summary="Get job results",
            tags=["jobs"]
        )
    
    async def _get_agents(self) -> List[Dict[str, Any]]:
        """API handler to list all registered agents."""
        return [
            {
                "name": name,
                "metadata": info["metadata"],
                "capabilities": list(info["capabilities"].keys())
            }
            for name, info in self.agent_registry.agents.items()
        ]
    
    async def _get_workflows(self) -> List[Dict[str, Any]]:
        """API handler to list all registered workflows."""
        return list(self.workflow_registry.workflows.values())
    
    async def _create_job(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """API handler to create a new job."""
        if "workflow_id" not in request:
            raise ValueError("Request must include a workflow_id")
        
        workflow_id = request["workflow_id"]
        inputs = request.get("inputs", {})
        
        return await self.job_manager.create_job(workflow_id, inputs)
    
    async def _get_job_status(self, job_id: str) -> Dict[str, Any]:
        """API handler to get job status."""
        return await self.job_manager.get_job_status(job_id)
    
    async def _get_job_results(self, job_id: str) -> Dict[str, Any]:
        """API handler to get job results."""
        return await self.job_manager.get_job_results(job_id)
    
    def agent(self, name: str, **metadata) -> Callable[[AgentType], AgentType]:
        """
        Decorator to register an agent class.
        
        Args:
            name: Name of the agent
            **metadata: Additional metadata for the agent
            
        Returns:
            Decorator function
        """
        def decorator(cls: AgentType) -> AgentType:
            self.agent_registry.register_agent(name, cls, metadata)
            return cls
        return decorator
    
    def capability(self, name: str, **metadata) -> Callable[[CapabilityFunc], CapabilityFunc]:
        """
        Decorator to register an agent capability.
        
        Args:
            name: Name of the capability
            **metadata: Additional metadata for the capability
            
        Returns:
            Decorator function
        """
        def decorator(func: CapabilityFunc) -> CapabilityFunc:
            # Extract agent class from the method
            agent_cls = None
            frame = inspect.currentframe()
            try:
                if frame and frame.f_back and frame.f_back.f_locals:
                    for agent_name, agent_info in self.agent_registry.agents.items():
                        if agent_info["cls"] == frame.f_back.f_locals.get("cls"):
                            self.agent_registry.register_capability(
                                agent_name, name, func, metadata
                            )
                            break
            finally:
                del frame  # Avoid reference cycles
                
            return func
        return decorator
    
    def tool(self, name: str, **metadata) -> Callable[[Callable], Callable]:
        """
        Decorator to register a standalone tool.
        
        Args:
            name: Name of the tool
            **metadata: Additional metadata for the tool
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            self.agent_registry.register_tool(name, func, metadata)
            return func
        return decorator
    
    def register_workflow(self, workflow_def: Dict[str, Any]) -> None:
        """
        Register a workflow definition.
        
        Args:
            workflow_def: Workflow definition as a dictionary
        """
        self.workflow_registry.register_workflow(workflow_def)
    
    async def create_job(self, workflow_id: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new job from a workflow definition.
        
        Args:
            workflow_id: ID of the workflow to execute
            inputs: Input values for the workflow
            
        Returns:
            Created job as a dictionary
        """
        return await self.job_manager.create_job(workflow_id, inputs)
    
    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        """
        Get the status of a job.
        
        Args:
            job_id: ID of the job
            
        Returns:
            Job status as a dictionary
        """
        return await self.job_manager.get_job_status(job_id)
    
    async def get_job_results(self, job_id: str) -> Dict[str, Any]:
        """
        Get the results of a completed job.
        
        Args:
            job_id: ID of the job
            
        Returns:
            Job results as a dictionary
        """
        return await self.job_manager.get_job_results(job_id)
        
    def mount(self, app: FastAPI, prefix: Optional[str] = None) -> None:
        """
        Mount the OpenAgents router to a FastAPI application.
        
        Args:
            app: FastAPI application
            prefix: URL prefix for the router
        """
        app.include_router(
            self.router,
            prefix=prefix or self.settings.api_prefix,
            tags=["openagents"]
        ) 