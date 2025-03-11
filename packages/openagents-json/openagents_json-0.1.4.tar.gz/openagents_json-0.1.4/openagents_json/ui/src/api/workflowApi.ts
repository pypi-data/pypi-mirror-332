/**
 * API client for workflow operations
 */
import { API_BASE_URL } from '../utils/environment';
import type { Workflow, VisualizationData } from '../types/workflow';
import type { ValidationResult } from '../types/validation';

/**
 * API client for workflow operations
 */
export class WorkflowApi {
  private baseUrl: string;

  /**
   * Create a new WorkflowApi client
   * @param baseUrl API base URL (defaults to environment variable or '/api')
   */
  constructor(baseUrl: string = API_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  /**
   * Get all workflows
   * @returns Promise with workflow list
   */
  async getWorkflows(): Promise<Workflow[]> {
    const response = await fetch(`${this.baseUrl}/workflows`);
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(`Failed to fetch workflows: ${error.detail || response.statusText}`);
    }
    return response.json();
  }

  /**
   * Get a workflow by ID
   * @param id Workflow ID
   * @returns Promise with workflow details
   */
  async getWorkflow(id: string): Promise<Workflow> {
    const response = await fetch(`${this.baseUrl}/workflows/${id}`);
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(`Failed to fetch workflow: ${error.detail || response.statusText}`);
    }
    return response.json();
  }

  /**
   * Validate a workflow
   * @param workflow Workflow to validate
   * @returns Promise with validation result
   */
  async validateWorkflow(workflow: Workflow): Promise<ValidationResult> {
    const response = await fetch(`${this.baseUrl}/workflows/validate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(workflow)
    });
    
    return response.json();
  }

  /**
   * Get visualization data for a workflow
   * @param id Workflow ID
   * @returns Promise with visualization data
   */
  async getVisualizationData(id: string): Promise<VisualizationData> {
    const response = await fetch(`${this.baseUrl}/workflows/visualize/${id}`);
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(`Failed to fetch visualization data: ${error.detail || response.statusText}`);
    }
    return response.json();
  }

  /**
   * Create or update a workflow
   * @param workflow Workflow to save
   * @returns Promise with saved workflow
   */
  async saveWorkflow(workflow: Workflow): Promise<Workflow> {
    const method = workflow.id ? 'PUT' : 'POST';
    const url = workflow.id 
      ? `${this.baseUrl}/workflows/${workflow.id}` 
      : `${this.baseUrl}/workflows`;
    
    const response = await fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(workflow)
    });
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(`Failed to save workflow: ${error.detail || response.statusText}`);
    }
    
    return response.json();
  }

  /**
   * Delete a workflow
   * @param id Workflow ID
   * @returns Promise that resolves when the workflow is deleted
   */
  async deleteWorkflow(id: string): Promise<void> {
    const response = await fetch(`${this.baseUrl}/workflows/${id}`, {
      method: 'DELETE'
    });
    
    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(`Failed to delete workflow: ${error.detail || response.statusText}`);
    }
  }
}

// Export a singleton instance
export default new WorkflowApi(); 