/**
 * Validation state management with Zustand
 */
import { create } from 'zustand';
import { useWorkflowStore } from './workflowStore';
import type { ValidationResult, ValidationIssue } from '../types/validation';

/**
 * Validation store state interface
 */
interface ValidationState {
  // State
  validationResult: ValidationResult | null;
  isValidating: boolean;
  error: string | null;
  focusedIssue: ValidationIssue | null;
  
  // Actions
  validateCurrentWorkflow: () => Promise<void>;
  setValidationResult: (result: ValidationResult | null) => void;
  clearValidation: () => void;
  focusIssue: (issue: ValidationIssue) => void;
  clearFocusedIssue: () => void;
}

/**
 * Validation store with Zustand
 */
export const useValidationStore = create<ValidationState>((set) => ({
  // Initial state
  validationResult: null,
  isValidating: false,
  error: null,
  focusedIssue: null,
  
  // Actions
  validateCurrentWorkflow: async () => {
    const { currentWorkflow, validateWorkflow } = useWorkflowStore.getState();
    
    if (!currentWorkflow) {
      set({ error: 'No workflow selected for validation' });
      return;
    }
    
    set({ isValidating: true, error: null });
    
    try {
      const result = await validateWorkflow(currentWorkflow);
      set({ 
        validationResult: result, 
        isValidating: false,
        focusedIssue: result.issues.length > 0 ? result.issues[0] : null
      });
    } catch (error) {
      set({ 
        error: error instanceof Error ? error.message : 'Failed to validate workflow', 
        isValidating: false 
      });
    }
  },
  
  setValidationResult: (result) => set({ validationResult: result }),
  
  clearValidation: () => set({ 
    validationResult: null, 
    focusedIssue: null, 
    error: null 
  }),
  
  focusIssue: (issue) => set({ focusedIssue: issue }),
  
  clearFocusedIssue: () => set({ focusedIssue: null }),
})); 