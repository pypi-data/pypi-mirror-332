/**
 * Workflow state management with Zustand
 */
import { create } from 'zustand';
import workflowApi from '../api/workflowApi';
import type { Workflow } from '../types/workflow';
import type { ValidationResult } from '../types/validation';

/**
 * Workflow store state interface
 */
interface WorkflowState {
  // State
  workflows: Workflow[];
  currentWorkflow: Workflow | null;
  isLoading: boolean;
  error: string | null;
  
  // Actions
  fetchWorkflows: () => Promise<void>;
  fetchWorkflow: (id: string) => Promise<void>;
  updateWorkflow: (workflow: Workflow) => Promise<void>;
  validateWorkflow: (workflow: Workflow) => Promise<ValidationResult>;
  clearError: () => void;
  setCurrentWorkflow: (workflow: Workflow | null) => void;
}

/**
 * Workflow store with Zustand
 */
export const useWorkflowStore = create<WorkflowState>((set, get) => ({
  // Initial state
  workflows: [],
  currentWorkflow: null,
  isLoading: false,
  error: null,
  
  // Actions
  fetchWorkflows: async () => {
    set({ isLoading: true, error: null });
    try {
      const workflows = await workflowApi.getWorkflows();
      set({ workflows, isLoading: false });
    } catch (error) {
      set({ 
        error: error instanceof Error ? error.message : 'Failed to fetch workflows', 
        isLoading: false 
      });
    }
  },
  
  fetchWorkflow: async (id: string) => {
    set({ isLoading: true, error: null });
    try {
      const workflow = await workflowApi.getWorkflow(id);
      set({ currentWorkflow: workflow, isLoading: false });
    } catch (error) {
      set({ 
        error: error instanceof Error ? error.message : `Failed to fetch workflow ${id}`, 
        isLoading: false 
      });
    }
  },
  
  updateWorkflow: async (workflow: Workflow) => {
    set({ isLoading: true, error: null });
    try {
      const updatedWorkflow = await workflowApi.saveWorkflow(workflow);
      
      // Update in the workflows list if it exists
      const { workflows } = get();
      const updatedWorkflows = workflows.map(w => 
        w.id === updatedWorkflow.id ? updatedWorkflow : w
      );
      
      set({ 
        workflows: updatedWorkflows,
        currentWorkflow: updatedWorkflow,
        isLoading: false 
      });
    } catch (error) {
      set({ 
        error: error instanceof Error ? error.message : 'Failed to update workflow', 
        isLoading: false 
      });
    }
  },
  
  validateWorkflow: async (workflow: Workflow) => {
    set({ isLoading: true, error: null });
    try {
      const result = await workflowApi.validateWorkflow(workflow);
      set({ isLoading: false });
      return result;
    } catch (error) {
      set({ 
        error: error instanceof Error ? error.message : 'Failed to validate workflow', 
        isLoading: false 
      });
      // Return empty result with valid: false
      return { valid: false, issues: [] };
    }
  },
  
  clearError: () => set({ error: null }),
  
  setCurrentWorkflow: (workflow) => set({ currentWorkflow: workflow }),
})); 