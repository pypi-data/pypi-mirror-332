"""
Enhanced router for FastAPI applications using OpenAgents JSON.
"""

from typing import Any, Dict, List, Optional, Union

from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, Request
from pydantic import BaseModel, Field

from openagents_json.core.app import OpenAgentsApp
from openagents_json.settings import settings
from openagents_json.workflow import Connection, Parameter, Step, Workflow
from openagents_json.workflow.validator import validate_workflow


# Pydantic models for API request/response
class JobRequest(BaseModel):
    """Request model for creating a job."""

    workflow_id: str = Field(..., description="ID of the workflow to execute")
    inputs: Dict[str, Any] = Field(
        default_factory=dict, description="Input values for the workflow"
    )


class JobResponse(BaseModel):
    """Response model for job operations."""

    id: str = Field(..., description="ID of the job")
    workflow_id: str = Field(..., description="ID of the workflow")
    status: str = Field(..., description="Status of the job")
    created_at: str = Field(..., description="Creation timestamp")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="Input values")
    outputs: Optional[Dict[str, Any]] = Field(
        None, description="Output values (if completed)"
    )


class WorkflowResponse(BaseModel):
    """Response model for workflow operations."""

    id: str = Field(..., description="ID of the workflow")
    name: str = Field(..., description="Name of the workflow")
    description: Optional[str] = Field(None, description="Description of the workflow")
    version: str = Field(..., description="Version of the workflow")
    steps: List[Dict[str, Any]] = Field(..., description="Steps in the workflow")
    connections: List[Dict[str, Any]] = Field(
        ..., description="Connections between steps"
    )
    inputs: List[Dict[str, Any]] = Field(..., description="Input parameters")
    outputs: List[Dict[str, Any]] = Field(..., description="Output parameters")
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Metadata about the workflow"
    )


class ValidationResponse(BaseModel):
    """Response model for workflow validation."""

    valid: bool = Field(..., description="Whether the workflow is valid")
    validation_result: Dict[str, Any] = Field(
        ..., description="Detailed validation result"
    )


class VisualizationResponse(BaseModel):
    """Response model for workflow visualization."""

    nodes: List[Dict[str, Any]] = Field(..., description="Nodes in the visualization")
    edges: List[Dict[str, Any]] = Field(..., description="Edges in the visualization")
    metadata: Optional[Dict[str, Any]] = Field(
        None, description="Additional visualization metadata"
    )


class AgentResponse(BaseModel):
    """Response model for agent operations."""

    name: str = Field(..., description="Name of the agent")
    metadata: Dict[str, Any] = Field(..., description="Metadata about the agent")
    capabilities: List[str] = Field(..., description="List of capabilities")


class ErrorResponse(BaseModel):
    """Response model for errors."""

    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")


def create_api_router(openagents_app: OpenAgentsApp) -> APIRouter:
    """
    Create an enhanced API router for OpenAgents JSON.

    Args:
        openagents_app: An instance of OpenAgentsApp

    Returns:
        An APIRouter instance with enhanced endpoints
    """
    router = APIRouter(tags=["openagents"])

    #
    # Workflow endpoints
    #
    @router.get(
        "/workflows",
        response_model=List[WorkflowResponse],
        summary="List all registered workflows",
        description="Returns a list of all registered workflows in the system",
    )
    async def get_workflows(
        request: Request,
        tag: Optional[str] = Query(None, description="Filter workflows by tag"),
        category: Optional[str] = Query(
            None, description="Filter workflows by category"
        ),
    ) -> List[Dict[str, Any]]:
        """Get all workflows, optionally filtered by tag or category."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        if hasattr(app.workflow_registry, "list"):
            # Use the enhanced list method if available
            return app.workflow_registry.list(tag=tag, category=category)
        else:
            # Fall back to the basic method
            workflows = await app._get_workflows()

            # Filter by tag or category if provided
            if tag or category:
                filtered = []
                for workflow in workflows:
                    metadata = workflow.get("metadata", {})
                    tags = metadata.get("tags", [])
                    wf_category = metadata.get("category")

                    if (tag and tag in tags) or (category and category == wf_category):
                        filtered.append(workflow)
                return filtered

            return workflows

    @router.get(
        "/workflows/{workflow_id}",
        response_model=WorkflowResponse,
        summary="Get a specific workflow",
        description="Returns details of a specific workflow by ID",
    )
    async def get_workflow(
        request: Request,
        workflow_id: str = Path(..., description="ID of the workflow to retrieve"),
        version: Optional[str] = Query(
            None, description="Specific version to retrieve"
        ),
    ) -> Dict[str, Any]:
        """Get a specific workflow by ID and optionally a specific version."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        if hasattr(app.workflow_registry, "get"):
            # Use the enhanced get method if available
            workflow = app.workflow_registry.get(workflow_id, version=version)
            if not workflow:
                raise HTTPException(
                    status_code=404, detail=f"Workflow {workflow_id} not found"
                )
            return workflow
        else:
            # Fall back to the basic method
            workflows = await app._get_workflows()
            for workflow in workflows:
                if workflow.get("id") == workflow_id:
                    # Check version if specified
                    if version and workflow.get("version") != version:
                        continue
                    return workflow

            raise HTTPException(
                status_code=404, detail=f"Workflow {workflow_id} not found"
            )

    @router.post(
        "/workflows",
        response_model=WorkflowResponse,
        status_code=201,
        summary="Register a new workflow",
        description="Register a new workflow definition in the system",
    )
    async def create_workflow(
        request: Request,
        workflow: Dict[str, Any] = Body(..., description="Workflow definition"),
    ) -> Dict[str, Any]:
        """Register a new workflow."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        try:
            if app.register_workflow(workflow):
                # Get the registered workflow details
                if hasattr(app.workflow_registry, "get"):
                    # Use the enhanced get method if available
                    registered = app.workflow_registry.get(workflow["id"])
                    if registered:
                        return registered

                return workflow
            else:
                raise HTTPException(
                    status_code=400, detail="Failed to register workflow"
                )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.delete(
        "/workflows/{workflow_id}",
        status_code=204,
        summary="Delete a workflow",
        description="Delete a workflow from the registry",
    )
    async def delete_workflow(
        request: Request,
        workflow_id: str = Path(..., description="ID of the workflow to delete"),
        version: Optional[str] = Query(None, description="Specific version to delete"),
    ):
        """Delete a workflow by ID and optionally a specific version."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        if hasattr(app.workflow_registry, "delete"):
            # Use the enhanced delete method
            result = app.workflow_registry.delete(workflow_id, version=version)
            if not result:
                raise HTTPException(
                    status_code=404, detail=f"Workflow {workflow_id} not found"
                )
        else:
            # No delete method available
            raise HTTPException(
                status_code=501,
                detail="Delete operation not supported by this workflow registry",
            )

    @router.post(
        "/workflows/validate",
        response_model=ValidationResponse,
        summary="Validate a workflow",
        description="Validate a workflow definition against schema and logic rules",
    )
    async def validate_workflow_endpoint(
        workflow: Dict[str, Any] = Body(
            ..., description="Workflow definition to validate"
        )
    ) -> Dict[str, Any]:
        """Validate a workflow definition."""
        result = validate_workflow(workflow)
        return {"valid": result.valid, "validation_result": result.dict()}

    @router.get(
        "/workflows/visualize/{workflow_id}",
        response_model=VisualizationResponse,
        summary="Get workflow visualization data",
        description="Get data for visualizing a workflow as a diagram",
    )
    async def visualize_workflow(
        request: Request,
        workflow_id: str = Path(..., description="ID of the workflow to visualize"),
    ) -> Dict[str, Any]:
        """Get visualization data for a workflow."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        # Get the workflow
        if hasattr(app.workflow_registry, "get"):
            # Use the enhanced get method if available
            workflow = app.workflow_registry.get(workflow_id)
            if not workflow:
                raise HTTPException(
                    status_code=404, detail=f"Workflow {workflow_id} not found"
                )
        else:
            # Fall back to the basic method
            workflows = await app._get_workflows()
            workflow = next((w for w in workflows if w.get("id") == workflow_id), None)
            if not workflow:
                raise HTTPException(
                    status_code=404, detail=f"Workflow {workflow_id} not found"
                )

        # Generate visualization data
        nodes = []
        edges = []

        # Create nodes for each step
        for i, step in enumerate(workflow.get("steps", [])):
            step_id = step.get("id")
            position_x = i * 200  # Simple positioning strategy
            position_y = 100

            nodes.append(
                {
                    "id": step_id,
                    "type": "step",
                    "position": {"x": position_x, "y": position_y},
                    "data": {
                        "label": step.get("name", step_id),
                        "description": step.get("description", ""),
                        "component": step.get("component", ""),
                        "step": step,
                    },
                }
            )

        # Create edges for connections
        for i, connection in enumerate(workflow.get("connections", [])):
            source = connection.get("source", "").split(".")
            target = connection.get("target", "").split(".")

            if len(source) == 2 and len(target) == 2:
                source_id, source_output = source
                target_id, target_input = target

                edges.append(
                    {
                        "id": f"edge-{i}",
                        "source": source_id,
                        "target": target_id,
                        "data": {
                            "sourceHandle": source_output,
                            "targetHandle": target_input,
                            "label": f"{source_output} → {target_input}",
                            "condition": connection.get("condition"),
                            "connection": connection,
                        },
                    }
                )

        return {
            "nodes": nodes,
            "edges": edges,
            "metadata": {
                "workflowId": workflow_id,
                "workflowName": workflow.get("name", workflow_id),
                "workflowVersion": workflow.get("version", "1.0.0"),
            },
        }

    #
    # Job endpoints
    #
    @router.post(
        "/jobs",
        response_model=JobResponse,
        status_code=201,
        summary="Create a new job",
        description="Create a new job from a workflow definition",
    )
    async def create_job(
        request: Request,
        job_request: JobRequest = Body(..., description="Job creation request"),
    ) -> Dict[str, Any]:
        """Create a new job for a workflow."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        try:
            job = await app.create_job(job_request.workflow_id, job_request.inputs)
            return job
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get(
        "/jobs/{job_id}/status",
        response_model=JobResponse,
        summary="Get job status",
        description="Get the status of a specific job",
    )
    async def get_job_status(
        request: Request,
        job_id: str = Path(..., description="ID of the job to retrieve status for"),
    ) -> Dict[str, Any]:
        """Get the status of a job."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        try:
            status = await app.get_job_status(job_id)
            return status
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    @router.get(
        "/jobs/{job_id}/results",
        response_model=JobResponse,
        summary="Get job results",
        description="Get the results of a completed job",
    )
    async def get_job_results(
        request: Request,
        job_id: str = Path(..., description="ID of the job to retrieve results for"),
    ) -> Dict[str, Any]:
        """Get the results of a completed job."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        try:
            results = await app.get_job_results(job_id)
            return results
        except ValueError as e:
            if "not completed" in str(e).lower():
                raise HTTPException(status_code=400, detail=str(e))
            else:
                raise HTTPException(status_code=404, detail=str(e))

    #
    # Agent endpoints
    #
    @router.get(
        "/agents",
        response_model=List[AgentResponse],
        summary="List all registered agents",
        description="Returns a list of all registered agents in the system",
    )
    async def get_agents(request: Request) -> List[Dict[str, Any]]:
        """Get all registered agents."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        agents = await app._get_agents()
        return agents

    @router.get(
        "/agents/{agent_name}",
        response_model=AgentResponse,
        summary="Get a specific agent",
        description="Returns details of a specific agent by name",
    )
    async def get_agent(
        request: Request,
        agent_name: str = Path(..., description="Name of the agent to retrieve"),
    ) -> Dict[str, Any]:
        """Get a specific agent by name."""
        # Use the app from middleware if available
        app = getattr(request.state, "openagents_app", openagents_app)

        agents = await app._get_agents()
        for agent in agents:
            if agent.get("name") == agent_name:
                return agent

        raise HTTPException(status_code=404, detail=f"Agent {agent_name} not found")

    #
    # System endpoints
    #
    @router.get(
        "/health",
        summary="Health check",
        description="Check if the API is up and running",
    )
    async def health() -> Dict[str, str]:
        """Health check endpoint."""
        return {"status": "ok"}

    @router.get(
        "/version",
        summary="Get API version",
        description="Get the version of the OpenAgents JSON API",
    )
    async def version() -> Dict[str, str]:
        """Get the API version."""
        return {
            "version": getattr(settings, "version", "unknown"),
            "app_name": settings.app.app_name,
        }

    return router
