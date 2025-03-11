"""
Tests for the workflow validation system.
"""

import json
import unittest
from typing import Any, Dict, List

from openagents_json.workflow.validator import (
    CycleDetectionValidator,
    DependencyValidator,
    SchemaValidator,
    SemVerValidator,
    TypeCompatibilityValidator,
    ValidationIssue,
    ValidationLocation,
    ValidationMode,
    ValidationResult,
    ValidationSeverity,
    create_default_pipeline,
    validate_workflow,
)


class TestWorkflowValidator(unittest.TestCase):
    """Test the workflow validation system."""

    def setUp(self):
        """Set up test fixtures."""
        # Simple valid workflow
        self.valid_workflow = {
            "id": "test_workflow",
            "version": "1.0.0",
            "name": "Test Workflow",
            "description": "A test workflow",
            "steps": [
                {
                    "id": "step1",
                    "component": "test.component",
                    "inputs": {"input1": "value1"},
                    "outputs": {"output1": "result1"},
                },
                {
                    "id": "step2",
                    "component": "test.component2",
                    "inputs": {"input2": "value2"},
                    "outputs": {"output2": "result2"},
                },
            ],
            "connections": [{"source": "step1.output1", "target": "step2.input2"}],
        }

        # Invalid workflow (missing required field)
        self.invalid_workflow = {
            "id": "test_workflow",
            # "version" is missing
            "steps": [
                {
                    # "id" is missing
                    "component": "test.component"
                }
            ],
        }

        # Workflow with a cycle
        self.cyclic_workflow = {
            "id": "cyclic_workflow",
            "version": "1.0.0",
            "steps": [
                {
                    "id": "step1",
                    "component": "test.component",
                    "inputs": {"input1": "value1"},
                    "outputs": {"output1": "result1"},
                },
                {
                    "id": "step2",
                    "component": "test.component2",
                    "inputs": {"input2": "value2"},
                    "outputs": {"output2": "result2"},
                },
            ],
            "connections": [
                {"source": "step1.output1", "target": "step2.input2"},
                {"source": "step2.output2", "target": "step1.input1"},
            ],
        }

        # Workflow with dependency issues
        self.dependency_issue_workflow = {
            "id": "dependency_issue",
            "version": "1.0.0",
            "steps": [
                {
                    "id": "step1",
                    "component": "test.component",
                    "inputs": {"input1": "value1"},
                    "outputs": {"output1": "result1"},
                }
            ],
            "connections": [
                {
                    "source": "step1.output_nonexistent",
                    "target": "step_nonexistent.input1",
                }
            ],
        }

    def test_schema_validator(self):
        """Test the schema validator."""
        validator = SchemaValidator()

        # Test valid workflow
        result = validator.validate(self.valid_workflow)
        self.assertTrue(result.valid)
        self.assertEqual(len(result.issues), 0)

        # Test invalid workflow
        result = validator.validate(self.invalid_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

        # Check that issues are correctly formatted
        for issue in result.issues:
            self.assertIsInstance(issue.code, str)
            self.assertIsInstance(issue.message, str)
            self.assertIsInstance(issue.severity, ValidationSeverity)
            self.assertIsInstance(issue.location, ValidationLocation)

    def test_cycle_detection_validator(self):
        """Test the cycle detection validator."""
        validator = CycleDetectionValidator()

        # Test valid workflow
        result = validator.validate(self.valid_workflow)
        self.assertTrue(result.valid)
        self.assertEqual(len(result.issues), 0)

        # Test cyclic workflow
        result = validator.validate(self.cyclic_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

        # Check the cycle issue
        issue = result.issues[0]
        self.assertEqual(issue.code, "cycle_detected")
        self.assertIn("Cycle detected", issue.message)

    def test_dependency_validator(self):
        """Test the dependency validator."""
        validator = DependencyValidator()

        # Test valid workflow
        result = validator.validate(self.valid_workflow)
        self.assertTrue(result.valid)
        self.assertEqual(len(result.issues), 0)

        # Test workflow with dependency issues
        result = validator.validate(self.dependency_issue_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

        # Check the dependency issues
        for issue in result.issues:
            if "missing_source_output" in issue.code:
                self.assertIn("output_nonexistent", issue.message)
            elif "missing_target_step" in issue.code:
                self.assertIn("step_nonexistent", issue.message)

    def test_validation_pipeline(self):
        """Test the validation pipeline."""
        # Create a pipeline with all validators
        pipeline = create_default_pipeline()

        # Test valid workflow
        result = pipeline.validate(self.valid_workflow)
        self.assertTrue(result.valid)
        self.assertEqual(len(result.issues), 0)

        # Test invalid workflow
        result = pipeline.validate(self.invalid_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

        # Test cyclic workflow
        result = pipeline.validate(self.cyclic_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

        # Test dependency issue workflow
        result = pipeline.validate(self.dependency_issue_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

    def test_validation_modes(self):
        """Test different validation modes."""
        # The invalid workflow should fail in NORMAL mode
        result = validate_workflow(self.invalid_workflow, mode=ValidationMode.NORMAL)
        self.assertFalse(result.valid)

        # The invalid workflow should pass in NONE mode
        result = validate_workflow(self.invalid_workflow, mode=ValidationMode.NONE)
        self.assertTrue(result.valid)
        self.assertGreater(len(result.issues), 0)  # Issues are still reported

    def test_validation_result_merge(self):
        """Test merging validation results."""
        # Create two validation results
        result1 = ValidationResult(valid=True, issues=[])

        result2 = ValidationResult(
            valid=False,
            issues=[
                ValidationIssue(
                    code="test_issue",
                    message="Test issue",
                    severity=ValidationSeverity.ERROR,
                    location=ValidationLocation(path="/"),
                )
            ],
        )

        # Merge the results
        merged = result1.merge(result2)

        # The merged result should be invalid
        self.assertFalse(merged.valid)
        self.assertEqual(len(merged.issues), 1)


class TestValidationEdgeCases(unittest.TestCase):
    """Test edge cases for workflow validation."""

    def test_empty_workflow(self):
        """Test validating an empty workflow."""
        empty_workflow = {}
        result = validate_workflow(empty_workflow)
        self.assertFalse(result.valid)
        self.assertGreater(len(result.issues), 0)

    def test_minimal_valid_workflow(self):
        """Test validating a minimal valid workflow."""
        minimal_workflow = {
            "id": "minimal",
            "steps": [{"id": "step1", "component": "test.component"}],
        }

        result = validate_workflow(minimal_workflow)
        self.assertTrue(result.valid)

    def test_multiple_validation_errors(self):
        """Test a workflow with multiple validation errors."""
        multi_error_workflow = {
            # Missing ID
            "steps": [
                {
                    # Missing ID
                    "component": "test.component"
                }
            ],
            "connections": [
                {
                    # Invalid source and target format
                    "source": "invalid",
                    "target": "also_invalid",
                }
            ],
        }

        result = validate_workflow(multi_error_workflow)
        self.assertFalse(result.valid)
        self.assertTrue(len(result.issues) >= 3)  # At least 3 issues


if __name__ == "__main__":
    unittest.main()
