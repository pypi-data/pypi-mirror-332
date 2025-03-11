import { beforeEach, describe, expect, it, vi } from 'vitest';
import { useValidationStore } from './validationStore';
import { useWorkflowStore } from './workflowStore';
import { ValidationResult, ValidationSeverity } from '../types/validation';
import type { Workflow } from '../types/workflow';

// Mock the workflow store
vi.mock('./workflowStore', () => ({
  useWorkflowStore: {
    getState: vi.fn(),
  },
}));

// Sample workflow and validation data for testing
const sampleWorkflow: Workflow = {
  id: 'workflow-1',
  version: '1.0.0',
  name: 'Test Workflow',
  steps: [],
  connections: [],
  inputs: {},
  outputs: {},
};

const validValidationResult: ValidationResult = {
  valid: true,
  issues: [],
};

const invalidValidationResult: ValidationResult = {
  valid: false,
  issues: [
    {
      message: 'Test error message',
      code: 'VALIDATION_ERROR',
      severity: ValidationSeverity.ERROR,
      location: { path: 'steps[0]' }
    },
    {
      message: 'Test warning message',
      code: 'VALIDATION_WARNING',
      severity: ValidationSeverity.WARNING,
      location: { path: 'connections[0]' }
    },
  ],
};

// Type for the mock return value of useWorkflowStore.getState()
interface MockWorkflowState {
  currentWorkflow: Workflow | null;
  validateWorkflow: (workflow: Workflow) => Promise<ValidationResult>;
  workflows: Workflow[];
  isLoading: boolean;
  error: string | null;
  fetchWorkflows: () => Promise<void>;
  fetchWorkflow: () => Promise<void>;
  clearError: () => void;
  selectedWorkflow: Workflow | null;
  setCurrentWorkflow: (workflow: Workflow | null) => void;
  updateWorkflow: (workflow: Workflow) => Promise<void>;
  deleteWorkflow: (id: string) => void;
  addWorkflow: (workflow: Workflow) => void;
}

describe('validationStore', () => {
  beforeEach(() => {
    // Reset the store
    useValidationStore.setState({
      validationResult: null,
      isValidating: false,
      error: null,
      focusedIssue: null,
    });
    
    // Reset the mock functions
    vi.resetAllMocks();
    
    // Set up a default mock implementation for workflow store with dummy values for missing properties
    vi.mocked(useWorkflowStore.getState).mockReturnValue({
      currentWorkflow: sampleWorkflow,
      validateWorkflow: vi.fn().mockResolvedValue(validValidationResult),
      workflows: [],
      isLoading: false,
      error: null,
      fetchWorkflows: vi.fn().mockResolvedValue(undefined),
      fetchWorkflow: vi.fn().mockResolvedValue(undefined),
      clearError: vi.fn(),
      selectedWorkflow: null,
      setCurrentWorkflow: vi.fn(),
      updateWorkflow: vi.fn().mockResolvedValue(undefined),
      deleteWorkflow: vi.fn(),
      addWorkflow: vi.fn(),
    } as MockWorkflowState);
  });
  
  describe('validateCurrentWorkflow', () => {
    it('should validate the current workflow', async () => {
      // Mock the validation function to return a valid result
      const validateWorkflowMock = vi.fn().mockResolvedValue(validValidationResult);
      vi.mocked(useWorkflowStore.getState).mockReturnValue({
        currentWorkflow: sampleWorkflow,
        validateWorkflow: validateWorkflowMock,
        workflows: [],
        isLoading: false,
        error: null,
        fetchWorkflows: vi.fn().mockResolvedValue(undefined),
        fetchWorkflow: vi.fn().mockResolvedValue(undefined),
        clearError: vi.fn(),
        selectedWorkflow: null,
        setCurrentWorkflow: vi.fn(),
        updateWorkflow: vi.fn().mockResolvedValue(undefined),
        deleteWorkflow: vi.fn(),
        addWorkflow: vi.fn(),
      } as MockWorkflowState);
      
      // Execute the validation action
      await useValidationStore.getState().validateCurrentWorkflow();
      
      // Check the store was updated correctly
      expect(useValidationStore.getState().validationResult).toEqual(validValidationResult);
      expect(useValidationStore.getState().isValidating).toBe(false);
      expect(useValidationStore.getState().error).toBeNull();
      expect(useValidationStore.getState().focusedIssue).toBeNull();
      
      // Verify the workflow validation was called correctly
      expect(validateWorkflowMock).toHaveBeenCalledTimes(1);
      expect(validateWorkflowMock).toHaveBeenCalledWith(sampleWorkflow);
    });
    
    it('should set first issue as focused when validation fails', async () => {
      // Mock the validation function to return an invalid result
      const validateWorkflowMock = vi.fn().mockResolvedValue(invalidValidationResult);
      vi.mocked(useWorkflowStore.getState).mockReturnValue({
        currentWorkflow: sampleWorkflow,
        validateWorkflow: validateWorkflowMock,
        workflows: [],
        isLoading: false,
        error: null,
        fetchWorkflows: vi.fn().mockResolvedValue(undefined),
        fetchWorkflow: vi.fn().mockResolvedValue(undefined),
        clearError: vi.fn(),
        selectedWorkflow: null,
        setCurrentWorkflow: vi.fn(),
        updateWorkflow: vi.fn().mockResolvedValue(undefined),
        deleteWorkflow: vi.fn(),
        addWorkflow: vi.fn(),
      } as MockWorkflowState);
      
      // Execute the validation action
      await useValidationStore.getState().validateCurrentWorkflow();
      
      // Check the store was updated correctly
      expect(useValidationStore.getState().validationResult).toEqual(invalidValidationResult);
      expect(useValidationStore.getState().isValidating).toBe(false);
      expect(useValidationStore.getState().error).toBeNull();
      expect(useValidationStore.getState().focusedIssue).toEqual(invalidValidationResult.issues[0]);
    });
    
    it('should handle case when no workflow is selected', async () => {
      // Mock the workflow store to return no current workflow
      vi.mocked(useWorkflowStore.getState).mockReturnValue({
        currentWorkflow: null,
        validateWorkflow: vi.fn(),
        workflows: [],
        isLoading: false,
        error: null,
        fetchWorkflows: vi.fn().mockResolvedValue(undefined),
        fetchWorkflow: vi.fn().mockResolvedValue(undefined),
        clearError: vi.fn(),
        selectedWorkflow: null,
        setCurrentWorkflow: vi.fn(),
        updateWorkflow: vi.fn().mockResolvedValue(undefined),
        deleteWorkflow: vi.fn(),
        addWorkflow: vi.fn(),
      } as MockWorkflowState);
      
      // Execute the validation action
      await useValidationStore.getState().validateCurrentWorkflow();
      
      // Check the store was updated with an error
      expect(useValidationStore.getState().validationResult).toBeNull();
      expect(useValidationStore.getState().isValidating).toBe(false);
      expect(useValidationStore.getState().error).toBe('No workflow selected for validation');
      expect(useValidationStore.getState().focusedIssue).toBeNull();
    });
    
    it('should handle validation errors', async () => {
      // Mock the validation function to throw an error
      const errorMessage = 'Validation error';
      const validateWorkflowMock = vi.fn().mockRejectedValue(new Error(errorMessage));
      vi.mocked(useWorkflowStore.getState).mockReturnValue({
        currentWorkflow: sampleWorkflow,
        validateWorkflow: validateWorkflowMock,
        workflows: [],
        isLoading: false,
        error: null,
        fetchWorkflows: vi.fn().mockResolvedValue(undefined),
        fetchWorkflow: vi.fn().mockResolvedValue(undefined),
        clearError: vi.fn(),
        selectedWorkflow: null,
        setCurrentWorkflow: vi.fn(),
        updateWorkflow: vi.fn().mockResolvedValue(undefined),
        deleteWorkflow: vi.fn(),
        addWorkflow: vi.fn(),
      } as MockWorkflowState);
      
      // Execute the validation action
      await useValidationStore.getState().validateCurrentWorkflow();
      
      // Check the store was updated with the error
      expect(useValidationStore.getState().validationResult).toBeNull();
      expect(useValidationStore.getState().isValidating).toBe(false);
      expect(useValidationStore.getState().error).toBe(errorMessage);
      expect(useValidationStore.getState().focusedIssue).toBeNull();
    });
  });
  
  describe('focusing issues', () => {
    it('should focus on a specific issue', () => {
      // Set up an initial validation result
      useValidationStore.setState({
        validationResult: invalidValidationResult,
        isValidating: false,
        error: null,
        focusedIssue: null,
      });
      
      // Focus on a specific issue
      useValidationStore.getState().focusIssue(invalidValidationResult.issues[1]);
      
      // Check the store was updated correctly
      expect(useValidationStore.getState().focusedIssue).toEqual(invalidValidationResult.issues[1]);
    });
    
    it('should clear the focused issue', () => {
      // Set up an initial state with a focused issue
      useValidationStore.setState({
        validationResult: invalidValidationResult,
        isValidating: false,
        error: null,
        focusedIssue: invalidValidationResult.issues[0],
      });
      
      // Clear the focused issue
      useValidationStore.getState().clearFocusedIssue();
      
      // Check the store was updated correctly
      expect(useValidationStore.getState().focusedIssue).toBeNull();
    });
  });
  
  describe('clearing validation', () => {
    it('should clear all validation data', () => {
      // Set up an initial state with validation data
      useValidationStore.setState({
        validationResult: invalidValidationResult,
        isValidating: false,
        error: 'Some error',
        focusedIssue: invalidValidationResult.issues[0],
      });
      
      // Clear the validation
      useValidationStore.getState().clearValidation();
      
      // Check the store was reset
      expect(useValidationStore.getState().validationResult).toBeNull();
      expect(useValidationStore.getState().error).toBeNull();
      expect(useValidationStore.getState().focusedIssue).toBeNull();
    });
  });
}); 