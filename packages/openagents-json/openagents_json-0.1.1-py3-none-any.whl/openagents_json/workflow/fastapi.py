"""
FastAPI integration for workflow validation.

This module provides middleware and helper functions to integrate
workflow validation with FastAPI.
"""

import inspect
import json
from typing import Any, Callable, Dict, List, Optional, Set, Type, Union

from fastapi import Body, Depends, FastAPI, HTTPException, Request, Response
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from openagents_json.workflow.models import Workflow
from openagents_json.workflow.openapi import (
    extend_openapi_with_workflows,
    extract_workflows_from_openapi,
)
from openagents_json.workflow.registry import WorkflowRegistry
from openagents_json.workflow.validator import (
    ValidationMode,
    ValidationResult,
    validate_workflow,
)


class WorkflowValidationMiddleware(BaseHTTPMiddleware):
    """
    Middleware for validating workflows in FastAPI requests.

    This middleware validates workflow definitions in incoming requests
    and adds validation information to the response.
    """

    def __init__(
        self,
        app: ASGIApp,
        validation_mode: ValidationMode = ValidationMode.NORMAL,
        validate_path_pattern: str = "/workflows",
    ):
        """
        Initialize the middleware.

        Args:
            app: The ASGI application
            validation_mode: The validation mode to use
            validate_path_pattern: Path pattern to determine which routes to validate
        """
        super().__init__(app)
        self.validation_mode = validation_mode
        self.validate_path_pattern = validate_path_pattern

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and response.

        Args:
            request: The incoming request
            call_next: Function to call the next middleware

        Returns:
            Response: The response from the application
        """
        # Only process certain paths
        if not request.url.path.startswith(self.validate_path_pattern):
            return await call_next(request)

        # Only process POST and PUT requests
        if request.method not in ["POST", "PUT"]:
            return await call_next(request)

        # Read the request body
        body = await request.body()

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            # Not a JSON request, skip validation
            return await call_next(request)

        # Check if the request contains a workflow definition
        if not isinstance(data, dict) or not data.get("id") or "steps" not in data:
            # Not a workflow definition, proceed without validation
            return await call_next(request)

        # Perform validation
        result = validate_workflow(data, mode=self.validation_mode)

        if not result.valid:
            # Invalid workflow
            return Response(
                content=json.dumps(
                    {
                        "detail": "Invalid workflow definition",
                        "validation_result": result.dict(),
                    }
                ),
                status_code=400,
                media_type="application/json",
            )

        # Valid workflow, proceed with the request
        response = await call_next(request)
        return response


def workflow_dependency(mode: ValidationMode = ValidationMode.NORMAL) -> Callable:
    """
    Create a FastAPI dependency for workflow validation.

    Args:
        mode: Validation mode to use

    Returns:
        Callable: A dependency function for workflow validation
    """

    def validate_workflow_dependency(
        workflow: Dict[str, Any] = Body(...),
    ) -> Dict[str, Any]:
        """
        Validate a workflow in a request body.

        Args:
            workflow: The workflow to validate

        Returns:
            Dict[str, Any]: The validated workflow

        Raises:
            HTTPException: If the workflow is invalid
        """
        result = validate_workflow(workflow, mode=mode)

        if not result.valid:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Invalid workflow definition",
                    "validation_result": result.dict(),
                },
            )

        return workflow

    return validate_workflow_dependency


def apply_workflow_validation_routes(
    app: FastAPI,
    prefix: str = "/workflows",
    validation_mode: ValidationMode = ValidationMode.NORMAL,
) -> FastAPI:
    """
    Apply workflow validation routes to a FastAPI application.

    Args:
        app: The FastAPI application
        prefix: Prefix for the workflow validation routes
        validation_mode: Validation mode to use

    Returns:
        FastAPI: The updated FastAPI application
    """
    # Get the workflow registry
    registry = WorkflowRegistry()

    # Add validation endpoint
    @app.post(f"{prefix}/validate", response_model=Dict[str, Any])
    async def validate_workflow_endpoint(workflow: Dict[str, Any] = Body(...)):
        """
        Validate a workflow definition.

        Args:
            workflow: The workflow to validate

        Returns:
            Dict[str, Any]: The validation result
        """
        result = validate_workflow(workflow, mode=validation_mode)
        return {"valid": result.valid, "validation_result": result.dict()}

    # Add workflow visualization endpoint
    @app.get(f"{prefix}/visualize/{{workflow_id}}")
    async def visualize_workflow(workflow_id: str):
        """
        Generate visualization data for a workflow.

        Args:
            workflow_id: ID of the workflow to visualize

        Returns:
            Dict[str, Any]: The visualization data

        Raises:
            HTTPException: If the workflow is not found
        """
        workflow = registry.get_workflow(workflow_id)
        if not workflow:
            raise HTTPException(
                status_code=404, detail=f"Workflow {workflow_id} not found"
            )

        # Generate visualization data (nodes and edges)
        nodes = []
        edges = []

        for i, step in enumerate(workflow.get("steps", [])):
            step_id = step.get("id")
            if step_id:
                nodes.append(
                    {
                        "id": step_id,
                        "label": step.get("name", step_id),
                        "description": step.get("description", ""),
                        "type": "step",
                        "position": {"x": 150 * i, "y": 150},
                    }
                )

        for i, connection in enumerate(workflow.get("connections", [])):
            source = connection.get("source", "")
            target = connection.get("target", "")

            source_parts = source.split(".", 1)
            target_parts = target.split(".", 1)

            if len(source_parts) == 2 and len(target_parts) == 2:
                source_step, source_output = source_parts
                target_step, target_input = target_parts

                edges.append(
                    {
                        "id": f"connection_{i}",
                        "source": source_step,
                        "target": target_step,
                        "sourceHandle": source_output,
                        "targetHandle": target_input,
                        "label": connection.get("transform", ""),
                    }
                )

        return {"nodes": nodes, "edges": edges, "workflow": workflow}

    # Extend the app's OpenAPI with workflow information
    original_openapi = app.openapi

    def get_openapi_with_workflows():
        if app.openapi_cache:
            return app.openapi_cache

        openapi_schema = original_openapi()

        # Get all workflows from the registry
        workflows = [w for w in registry.get_all_workflows()]

        # Extend the OpenAPI schema with workflows
        extended_schema = extend_openapi_with_workflows(openapi_schema, workflows)

        app.openapi_cache = extended_schema
        return extended_schema

    # Override the openapi function
    app.openapi = get_openapi_with_workflows

    return app


def create_validation_middleware(
    app: FastAPI, validation_mode: ValidationMode = ValidationMode.NORMAL
) -> None:
    """
    Add workflow validation middleware to a FastAPI application.

    Args:
        app: The FastAPI application
        validation_mode: Validation mode to use
    """
    app.add_middleware(WorkflowValidationMiddleware, validation_mode=validation_mode)
