/**
 * Temporary workflow types until we generate them from Pydantic models.
 * These will be replaced by the generated types once we set up the type generation.
 */

/**
 * Parameter definition for workflow inputs and outputs
 */
export interface Parameter {
  type: string;
  description?: string;
  default?: unknown;
  required?: boolean;
  enum?: unknown[];
  pattern?: string;
  minimum?: number;
  maximum?: number;
  format?: string;
}

/**
 * Retry configuration for workflow steps
 */
export interface RetryConfig {
  max_attempts: number;
  delay_seconds: number;
  backoff_multiplier: number;
}

/**
 * Step in a workflow
 */
export interface Step {
  id: string;
  component: string;
  name?: string;
  description?: string;
  inputs: Record<string, string>;
  outputs: Record<string, string>;
  condition?: string;
  retry?: RetryConfig;
  timeout?: number;
  metadata?: Record<string, unknown>;
}

/**
 * Connection between steps in a workflow
 */
export interface Connection {
  source: string;
  target: string;
  condition?: string;
  transform?: string;
}

/**
 * Workflow metadata
 */
export interface WorkflowMetadata {
  author?: string;
  created?: string;
  updated?: string;
  tags: string[];
  category?: string;
  license?: string;
  custom?: Record<string, unknown>;
}

/**
 * Workflow definition
 */
export interface Workflow {
  id: string;
  version: string;
  name?: string;
  description?: string;
  steps: Step[];
  connections: Connection[];
  inputs: Record<string, Parameter>;
  outputs: Record<string, Parameter>;
  metadata?: WorkflowMetadata;
}

/**
 * Visualization data for rendering a workflow diagram
 */
export interface VisualizationData {
  nodes: Node[];
  edges: Edge[];
  metadata?: Record<string, unknown>;
}

/**
 * Node in a workflow visualization
 */
export interface Node {
  id: string;
  type?: string;
  position: { x: number; y: number };
  data: Record<string, unknown>;
  style?: Record<string, unknown>;
}

/**
 * Edge in a workflow visualization
 */
export interface Edge {
  id: string;
  source: string;
  target: string;
  type?: string;
  animated?: boolean;
  label?: string;
  data?: Record<string, unknown>;
  style?: Record<string, unknown>;
} 