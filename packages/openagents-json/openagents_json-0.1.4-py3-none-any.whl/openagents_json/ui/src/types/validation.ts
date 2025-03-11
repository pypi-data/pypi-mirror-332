/**
 * Temporary validation types until we generate them from Pydantic models.
 * These will be replaced by the generated types once we set up the type generation.
 */

/**
 * Severity levels for validation issues
 */
export enum ValidationSeverity {
  ERROR = "error",
  WARNING = "warning",
  INFO = "info"
}

/**
 * Validation modes for the validation system
 */
export enum ValidationMode {
  STRICT = "strict",
  NORMAL = "normal",
  PERMISSIVE = "permissive",
  NONE = "none"
}

/**
 * Location of a validation issue within a workflow
 */
export interface ValidationLocation {
  path: string;
  step_id?: string;
  connection_index?: number;
  field?: string;
}

/**
 * Represents a single validation issue
 */
export interface ValidationIssue {
  code: string;
  message: string;
  severity: ValidationSeverity;
  location: ValidationLocation;
  suggestion?: string;
  details?: Record<string, unknown>;
}

/**
 * Results of a validation run
 */
export interface ValidationResult {
  valid: boolean;
  issues: ValidationIssue[];
} 