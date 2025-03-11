import { beforeEach, describe, expect, it, vi } from 'vitest';
import { useWorkflowStore } from './workflowStore';
import workflowApi from '../api/workflowApi';

// Mock the workflow API
vi.mock('../api/workflowApi', () => ({
  default: {
    getWorkflows: vi.fn(),
    getWorkflow: vi.fn(),
    saveWorkflow: vi.fn(),
    validateWorkflow: vi.fn(),
  },
}));

// Sample workflow data for testing
const sampleWorkflows = [
  {
    id: 'workflow-1',
    version: '1.0.0',
    name: 'Test Workflow 1',
    steps: [],
    connections: [],
    inputs: {},
    outputs: {},
  },
  {
    id: 'workflow-2',
    version: '1.0.0',
    name: 'Test Workflow 2',
    steps: [],
    connections: [],
    inputs: {},
    outputs: {},
  },
];

const sampleWorkflow = {
  id: 'workflow-1',
  version: '1.0.0',
  name: 'Test Workflow 1',
  steps: [],
  connections: [],
  inputs: {},
  outputs: {},
};

describe('workflowStore', () => {
  beforeEach(() => {
    // Reset the store
    useWorkflowStore.setState({
      workflows: [],
      currentWorkflow: null,
      isLoading: false,
      error: null,
    });
    
    // Reset the mock functions
    vi.resetAllMocks();
  });
  
  describe('fetchWorkflows', () => {
    it('should fetch and store workflows', async () => {
      // Mock the API response
      vi.mocked(workflowApi.getWorkflows).mockResolvedValue(sampleWorkflows);
      
      // Initial state should be empty
      expect(useWorkflowStore.getState().workflows).toEqual([]);
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      
      // Execute the fetch action
      const fetchPromise = useWorkflowStore.getState().fetchWorkflows();
      
      // Loading state should be true during fetch
      expect(useWorkflowStore.getState().isLoading).toBe(true);
      
      // Wait for the fetch to complete
      await fetchPromise;
      
      // Check the store was updated correctly
      expect(useWorkflowStore.getState().workflows).toEqual(sampleWorkflows);
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBeNull();
      
      // Verify the API was called correctly
      expect(workflowApi.getWorkflows).toHaveBeenCalledTimes(1);
    });
    
    it('should handle fetch errors', async () => {
      // Mock the API to throw an error
      const errorMessage = 'API error';
      vi.mocked(workflowApi.getWorkflows).mockRejectedValue(new Error(errorMessage));
      
      // Execute the fetch action
      const fetchPromise = useWorkflowStore.getState().fetchWorkflows();
      
      // Wait for the fetch to complete
      await fetchPromise;
      
      // Check the store was updated with the error
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBe(errorMessage);
      expect(useWorkflowStore.getState().workflows).toEqual([]);
    });
  });
  
  describe('fetchWorkflow', () => {
    it('should fetch and store a single workflow', async () => {
      // Mock the API response
      vi.mocked(workflowApi.getWorkflow).mockResolvedValue(sampleWorkflow);
      
      // Initial state should be empty
      expect(useWorkflowStore.getState().currentWorkflow).toBeNull();
      
      // Execute the fetch action
      const fetchPromise = useWorkflowStore.getState().fetchWorkflow('workflow-1');
      
      // Wait for the fetch to complete
      await fetchPromise;
      
      // Check the store was updated correctly
      expect(useWorkflowStore.getState().currentWorkflow).toEqual(sampleWorkflow);
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBeNull();
      
      // Verify the API was called correctly
      expect(workflowApi.getWorkflow).toHaveBeenCalledTimes(1);
      expect(workflowApi.getWorkflow).toHaveBeenCalledWith('workflow-1');
    });
    
    it('should handle fetch errors', async () => {
      // Mock the API to throw an error
      const errorMessage = 'API error';
      vi.mocked(workflowApi.getWorkflow).mockRejectedValue(new Error(errorMessage));
      
      // Execute the fetch action
      const fetchPromise = useWorkflowStore.getState().fetchWorkflow('workflow-1');
      
      // Wait for the fetch to complete
      await fetchPromise;
      
      // Check the store was updated with the error
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBe(errorMessage);
      expect(useWorkflowStore.getState().currentWorkflow).toBeNull();
    });
  });
  
  describe('updateWorkflow', () => {
    it('should update a workflow and update the workflows list', async () => {
      // Setup initial state with workflows
      useWorkflowStore.setState({
        workflows: [...sampleWorkflows],
        currentWorkflow: null,
        isLoading: false,
        error: null,
      });
      
      // Prepare the updated workflow
      const updatedWorkflow = {
        ...sampleWorkflow,
        name: 'Updated Workflow',
      };
      
      // Mock the API response
      vi.mocked(workflowApi.saveWorkflow).mockResolvedValue(updatedWorkflow);
      
      // Execute the update action
      const updatePromise = useWorkflowStore.getState().updateWorkflow(updatedWorkflow);
      
      // Wait for the update to complete
      await updatePromise;
      
      // Check the store was updated correctly
      expect(useWorkflowStore.getState().currentWorkflow).toEqual(updatedWorkflow);
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBeNull();
      
      // Workflows list should also be updated
      const storedWorkflows = useWorkflowStore.getState().workflows;
      const updatedWorkflowInList = storedWorkflows.find(w => w.id === 'workflow-1');
      expect(updatedWorkflowInList).toEqual(updatedWorkflow);
      
      // Verify the API was called correctly
      expect(workflowApi.saveWorkflow).toHaveBeenCalledTimes(1);
      expect(workflowApi.saveWorkflow).toHaveBeenCalledWith(updatedWorkflow);
    });
  });
  
  describe('validateWorkflow', () => {
    it('should validate a workflow', async () => {
      // Mock the validation result
      const validationResult = {
        valid: true,
        issues: [],
      };
      
      // Mock the API response
      vi.mocked(workflowApi.validateWorkflow).mockResolvedValue(validationResult);
      
      // Execute the validate action
      const result = await useWorkflowStore.getState().validateWorkflow(sampleWorkflow);
      
      // Check the result is correct
      expect(result).toEqual(validationResult);
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBeNull();
      
      // Verify the API was called correctly
      expect(workflowApi.validateWorkflow).toHaveBeenCalledTimes(1);
      expect(workflowApi.validateWorkflow).toHaveBeenCalledWith(sampleWorkflow);
    });
    
    it('should handle validation errors', async () => {
      // Mock the API to throw an error
      const errorMessage = 'Validation error';
      vi.mocked(workflowApi.validateWorkflow).mockRejectedValue(new Error(errorMessage));
      
      // Execute the validate action
      const result = await useWorkflowStore.getState().validateWorkflow(sampleWorkflow);
      
      // Check the result is a default invalid result
      expect(result).toEqual({ valid: false, issues: [] });
      expect(useWorkflowStore.getState().isLoading).toBe(false);
      expect(useWorkflowStore.getState().error).toBe(errorMessage);
    });
  });
}); 