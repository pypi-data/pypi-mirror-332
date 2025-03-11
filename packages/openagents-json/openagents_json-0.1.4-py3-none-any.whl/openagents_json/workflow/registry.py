"""
Workflow registry for storing and managing workflows.

This module provides a registry for workflows, including registration,
validation, versioning, and querying capabilities.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from openagents_json.workflow.models import Workflow
from openagents_json.workflow.schema import (
    WorkflowMetadata,
    WorkflowValidator,
    WorkflowVersion,
)


class WorkflowRegistry:
    """Registry for storing and managing workflows."""

    def __init__(self):
        """Initialize a workflow registry."""
        self.workflows: Dict[str, Dict[str, Any]] = {}
        self.validator = WorkflowValidator()

    def register(self, workflow: Union[Dict[str, Any], Workflow]) -> bool:
        """
        Register a workflow with the registry.

        Args:
            workflow: Workflow definition or Workflow model

        Returns:
            True if registration was successful, False otherwise

        Raises:
            ValueError: If the workflow is invalid
        """
        # Convert Workflow model to dict if needed
        if isinstance(workflow, Workflow):
            workflow_dict = workflow.to_dict()
        else:
            workflow_dict = workflow

        # Validate the workflow
        is_valid, error = self.validator.validate(workflow_dict)
        if not is_valid:
            raise ValueError(f"Invalid workflow: {error}")

        # Extract workflow ID and version
        workflow_id = workflow_dict["id"]
        workflow_version = workflow_dict.get("version", "1.0.0")

        # Update metadata
        if "metadata" not in workflow_dict:
            workflow_dict["metadata"] = {}

        # Set creation timestamp if not present
        if "created" not in workflow_dict["metadata"]:
            workflow_dict["metadata"]["created"] = datetime.utcnow().isoformat()

        # Always update the updated timestamp
        workflow_dict["metadata"]["updated"] = datetime.utcnow().isoformat()

        # Store the workflow
        if workflow_id not in self.workflows:
            self.workflows[workflow_id] = {}

        self.workflows[workflow_id][workflow_version] = workflow_dict
        return True

    def get(
        self, workflow_id: str, version: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Get a workflow from the registry.

        Args:
            workflow_id: ID of the workflow to retrieve
            version: Specific version to retrieve (latest if None)

        Returns:
            Workflow definition or None if not found
        """
        if workflow_id not in self.workflows:
            return None

        if version:
            # Get specific version
            return self.workflows[workflow_id].get(version)
        else:
            # Get latest version
            versions = sorted(
                self.workflows[workflow_id].keys(),
                key=lambda v: WorkflowVersion.compare("0.0.0", v),
            )
            if not versions:
                return None
            return self.workflows[workflow_id][versions[-1]]

    def list(
        self, tag: Optional[str] = None, category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        List workflows in the registry.

        Args:
            tag: Filter by tag (if provided)
            category: Filter by category (if provided)

        Returns:
            List of workflow definitions (latest versions)
        """
        result = []

        # Get the latest version of each workflow
        for workflow_id, versions in self.workflows.items():
            version_keys = sorted(
                versions.keys(), key=lambda v: WorkflowVersion.compare("0.0.0", v)
            )
            if not version_keys:
                continue

            workflow = versions[version_keys[-1]]

            # Filter by tag if provided
            if tag:
                tags = WorkflowMetadata.get_tags(workflow)
                if tag not in tags:
                    continue

            # Filter by category if provided
            if category:
                metadata = workflow.get("metadata", {})
                if metadata.get("category") != category:
                    continue

            result.append(workflow)

        return result

    def delete(self, workflow_id: str, version: Optional[str] = None) -> bool:
        """
        Delete a workflow from the registry.

        Args:
            workflow_id: ID of the workflow to delete
            version: Specific version to delete (all versions if None)

        Returns:
            True if deletion was successful, False otherwise
        """
        if workflow_id not in self.workflows:
            return False

        if version:
            # Delete specific version
            if version in self.workflows[workflow_id]:
                del self.workflows[workflow_id][version]

                # Remove workflow entry if no versions left
                if not self.workflows[workflow_id]:
                    del self.workflows[workflow_id]

                return True
            return False
        else:
            # Delete all versions
            del self.workflows[workflow_id]
            return True

    def save_to_file(self, file_path: Union[str, Path]) -> bool:
        """
        Save the registry to a JSON file.

        Args:
            file_path: Path to save the registry to

        Returns:
            True if save was successful, False otherwise
        """
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Create a serializable representation of the registry
            serializable = {}
            for workflow_id, versions in self.workflows.items():
                serializable[workflow_id] = versions

            with open(file_path, "w") as f:
                json.dump(serializable, f, indent=2)

            return True
        except Exception as e:
            print(f"Error saving registry: {e}")
            return False

    def load_from_file(self, file_path: Union[str, Path]) -> bool:
        """
        Load the registry from a JSON file.

        Args:
            file_path: Path to load the registry from

        Returns:
            True if load was successful, False otherwise
        """
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return False

            with open(file_path, "r") as f:
                data = json.load(f)

            # Replace the current registry
            self.workflows = data

            return True
        except Exception as e:
            print(f"Error loading registry: {e}")
            return False

    def get_versions(self, workflow_id: str) -> List[str]:
        """
        Get all versions of a workflow.

        Args:
            workflow_id: ID of the workflow

        Returns:
            List of versions sorted by semver
        """
        if workflow_id not in self.workflows:
            return []

        versions = list(self.workflows[workflow_id].keys())
        return sorted(versions, key=lambda v: WorkflowVersion.compare("0.0.0", v))

    def categorize(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Categorize workflows by their category.

        Returns:
            Dictionary of {category: [workflows]}
        """
        return WorkflowMetadata.categorize(self.list())

    def get_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """
        Get workflows with a specific tag.

        Args:
            tag: Tag to filter by

        Returns:
            List of workflow definitions
        """
        return self.list(tag=tag)

    def get_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get workflows in a specific category.

        Args:
            category: Category to filter by

        Returns:
            List of workflow definitions
        """
        return self.list(category=category)
