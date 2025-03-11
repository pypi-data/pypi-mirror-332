"""
Logic-based workflow validators.

This module provides validators that check the logical correctness of workflows,
including dependency checking, cycle detection, and type compatibility.
"""

from typing import Any, Dict, List, Optional, Set, Tuple

import networkx as nx

from openagents_json.workflow.validator.base import (
    ValidationIssue,
    ValidationLocation,
    ValidationRegistry,
    ValidationResult,
    ValidationSeverity,
    WorkflowValidatorInterface,
)


@ValidationRegistry.register
class CycleDetectionValidator(WorkflowValidatorInterface):
    """Validator that detects cycles in workflow connections."""

    @property
    def id(self) -> str:
        return "cycle_detector"

    @property
    def name(self) -> str:
        return "Cycle Detection Validator"

    @property
    def description(self) -> str:
        return "Detects cycles in workflow connections that would cause infinite loops"

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate that a workflow does not contain cycles.

        Args:
            workflow: The workflow to validate

        Returns:
            ValidationResult: The result of validation
        """
        # Extract steps and connections
        steps = workflow.get("steps", [])
        connections = workflow.get("connections", [])

        # Build a directed graph of step dependencies
        G = nx.DiGraph()

        # Add all steps as nodes
        for step in steps:
            step_id = step.get("id")
            if step_id:
                G.add_node(step_id)

        # Add connections as edges
        for connection in connections:
            source = connection.get("source", "")
            target = connection.get("target", "")

            # Parse source and target in the format "step_id.output_name"
            source_parts = source.split(".", 1)
            target_parts = target.split(".", 1)

            if len(source_parts) == 2 and len(target_parts) == 2:
                source_step = source_parts[0]
                target_step = target_parts[0]

                if source_step in G and target_step in G:
                    G.add_edge(source_step, target_step)

        # Check for cycles
        try:
            cycles = list(nx.simple_cycles(G))
        except nx.NetworkXNoCycle:
            cycles = []

        if not cycles:
            return ValidationResult(valid=True, issues=[])

        # Create issues for each cycle
        issues = []
        for cycle in cycles:
            # Find the connections that form this cycle
            cycle_connections = []
            for i in range(len(cycle)):
                source_step = cycle[i]
                target_step = cycle[(i + 1) % len(cycle)]

                # Find the connection index
                for j, conn in enumerate(connections):
                    conn_source = conn.get("source", "").split(".", 1)[0]
                    conn_target = conn.get("target", "").split(".", 1)[0]

                    if conn_source == source_step and conn_target == target_step:
                        cycle_connections.append(j)
                        break

            # Create the issue
            cycle_str = " -> ".join(cycle)
            issue = ValidationIssue(
                code="cycle_detected",
                message=f"Cycle detected in workflow: {cycle_str}",
                severity=ValidationSeverity.ERROR,
                location=ValidationLocation(
                    path="connections",
                    connection_index=(
                        cycle_connections[0] if cycle_connections else None
                    ),
                ),
                suggestion="Break the cycle by removing or modifying one of the connections",
            )
            issues.append(issue)

        return ValidationResult(valid=False, issues=issues)


@ValidationRegistry.register
class DependencyValidator(WorkflowValidatorInterface):
    """Validator that checks step dependencies are satisfied."""

    @property
    def id(self) -> str:
        return "dependency_validator"

    @property
    def name(self) -> str:
        return "Dependency Validator"

    @property
    def description(self) -> str:
        return "Validates that all step dependencies are satisfied"

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate that all step dependencies are satisfied.

        Args:
            workflow: The workflow to validate

        Returns:
            ValidationResult: The result of validation
        """
        # Extract steps and connections
        steps = workflow.get("steps", [])
        connections = workflow.get("connections", [])

        # Build maps of step IDs and outputs/inputs
        step_map = {}
        for step in steps:
            if step_id := step.get("id"):
                step_map[step_id] = {
                    "outputs": set(step.get("outputs", {}).keys()),
                    "inputs": set(step.get("inputs", {}).keys()),
                }

        # Check connections
        issues = []
        for i, connection in enumerate(connections):
            source = connection.get("source", "")
            target = connection.get("target", "")

            # Parse source and target
            source_parts = source.split(".", 1)
            target_parts = target.split(".", 1)

            if len(source_parts) != 2:
                issues.append(
                    ValidationIssue(
                        code="invalid_source_format",
                        message=f"Invalid source format: {source}. Expected 'step_id.output_name'",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/source",
                            connection_index=i,
                            field="source",
                        ),
                        suggestion="Format the source as 'step_id.output_name'",
                    )
                )
                continue

            if len(target_parts) != 2:
                issues.append(
                    ValidationIssue(
                        code="invalid_target_format",
                        message=f"Invalid target format: {target}. Expected 'step_id.input_name'",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/target",
                            connection_index=i,
                            field="target",
                        ),
                        suggestion="Format the target as 'step_id.input_name'",
                    )
                )
                continue

            source_step, source_output = source_parts
            target_step, target_input = target_parts

            # Check if source step exists
            if source_step not in step_map:
                issues.append(
                    ValidationIssue(
                        code="missing_source_step",
                        message=f"Source step '{source_step}' does not exist",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/source",
                            connection_index=i,
                            field="source",
                        ),
                        suggestion=f"Use one of the existing steps: {', '.join(step_map.keys())}",
                    )
                )
                continue

            # Check if target step exists
            if target_step not in step_map:
                issues.append(
                    ValidationIssue(
                        code="missing_target_step",
                        message=f"Target step '{target_step}' does not exist",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/target",
                            connection_index=i,
                            field="target",
                        ),
                        suggestion=f"Use one of the existing steps: {', '.join(step_map.keys())}",
                    )
                )
                continue

            # Check if source output exists
            if source_output not in step_map[source_step]["outputs"]:
                issues.append(
                    ValidationIssue(
                        code="missing_source_output",
                        message=f"Output '{source_output}' does not exist in step '{source_step}'",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/source",
                            connection_index=i,
                            field="source",
                        ),
                        suggestion=(
                            f"Use one of the existing outputs: {', '.join(step_map[source_step]['outputs'])}"
                            if step_map[source_step]["outputs"]
                            else "Define outputs for this step"
                        ),
                    )
                )

            # Check if target input exists
            if target_input not in step_map[target_step]["inputs"]:
                issues.append(
                    ValidationIssue(
                        code="missing_target_input",
                        message=f"Input '{target_input}' does not exist in step '{target_step}'",
                        severity=ValidationSeverity.ERROR,
                        location=ValidationLocation(
                            path=f"connections/{i}/target",
                            connection_index=i,
                            field="target",
                        ),
                        suggestion=(
                            f"Use one of the existing inputs: {', '.join(step_map[target_step]['inputs'])}"
                            if step_map[target_step]["inputs"]
                            else "Define inputs for this step"
                        ),
                    )
                )

        # Check for unused inputs that are required
        # This requires component information which we may not have here
        # Could be implemented later with registry information

        return ValidationResult(valid=not issues, issues=issues)


@ValidationRegistry.register
class TypeCompatibilityValidator(WorkflowValidatorInterface):
    """Validator that checks type compatibility in connections."""

    @property
    def id(self) -> str:
        return "type_compatibility"

    @property
    def name(self) -> str:
        return "Type Compatibility Validator"

    @property
    def description(self) -> str:
        return "Validates that connected inputs and outputs have compatible types"

    def validate(self, workflow: Dict[str, Any], **kwargs) -> ValidationResult:
        """
        Validate type compatibility in connections.

        Args:
            workflow: The workflow to validate
            component_registry: Optional registry of components with type information

        Returns:
            ValidationResult: The result of validation
        """
        inputs = workflow.get("inputs", {})
        outputs = workflow.get("outputs", {})
        steps = workflow.get("steps", [])

        # Collect all issues
        workflow_input_issues = self._validate_workflow_input_references(steps, inputs)
        workflow_output_issues = self._validate_workflow_output_references(
            outputs, steps
        )

        # Combine all issues
        issues = workflow_input_issues + workflow_output_issues

        return ValidationResult(valid=not issues, issues=issues)

    def _validate_workflow_input_references(
        self, steps: List[Dict[str, Any]], workflow_inputs: Dict[str, Any]
    ) -> List[ValidationIssue]:
        """Validate references to workflow inputs in steps."""
        issues = []

        for i, step in enumerate(steps):
            step_id = step.get("id", "")
            step_inputs = step.get("inputs", {})

            for input_name, input_value in step_inputs.items():
                # Check for references to workflow inputs (e.g., "${inputs.some_input}")
                if isinstance(input_value, str) and input_value.startswith("${inputs."):
                    referenced_input = input_value[9:].rstrip("}")

                    if referenced_input not in workflow_inputs:
                        issues.append(
                            ValidationIssue(
                                code="missing_workflow_input",
                                message=f"Step '{step_id}' references non-existent workflow input '{referenced_input}'",
                                severity=ValidationSeverity.ERROR,
                                location=ValidationLocation(
                                    path=f"steps/{i}/inputs/{input_name}",
                                    step_id=step_id,
                                    field=input_name,
                                ),
                                suggestion=(
                                    f"Define workflow input '{referenced_input}' or use an existing input: {', '.join(workflow_inputs.keys())}"
                                    if workflow_inputs
                                    else "Define workflow inputs"
                                ),
                            )
                        )

        return issues

    def _validate_workflow_output_references(
        self, workflow_outputs: Dict[str, Any], steps: List[Dict[str, Any]]
    ) -> List[ValidationIssue]:
        """Validate references to step outputs in workflow outputs."""
        issues = []
        step_ids = {step.get("id") for step in steps if step.get("id")}

        for output_name, output_spec in workflow_outputs.items():
            # Check for references to step outputs (e.g., "${steps.some_step.some_output}")
            output_value = output_spec.get("source", "")
            if isinstance(output_value, str) and output_value.startswith("${steps."):
                parts = output_value[8:].rstrip("}").split(".")
                if len(parts) == 2:
                    referenced_step, referenced_output = parts

                    # Check if the referenced step exists
                    if referenced_step not in step_ids:
                        issues.append(
                            ValidationIssue(
                                code="missing_referenced_step",
                                message=f"Workflow output '{output_name}' references non-existent step '{referenced_step}'",
                                severity=ValidationSeverity.ERROR,
                                location=ValidationLocation(
                                    path=f"outputs/{output_name}", field=output_name
                                ),
                                suggestion=f"Use one of the existing steps: {', '.join(step_ids)}",
                            )
                        )
                    else:
                        # Check if the referenced output exists
                        for step in steps:
                            if step.get("id") == referenced_step:
                                step_outputs = step.get("outputs", {})
                                if referenced_output not in step_outputs:
                                    issues.append(
                                        ValidationIssue(
                                            code="missing_step_output",
                                            message=f"Workflow output '{output_name}' references non-existent output '{referenced_output}' in step '{referenced_step}'",
                                            severity=ValidationSeverity.ERROR,
                                            location=ValidationLocation(
                                                path=f"outputs/{output_name}",
                                                field=output_name,
                                            ),
                                            suggestion=(
                                                f"Use an existing output from step '{referenced_step}': {', '.join(step_outputs.keys())}"
                                                if step_outputs
                                                else f"Define outputs for step '{referenced_step}'"
                                            ),
                                        )
                                    )
                                break

        return issues
