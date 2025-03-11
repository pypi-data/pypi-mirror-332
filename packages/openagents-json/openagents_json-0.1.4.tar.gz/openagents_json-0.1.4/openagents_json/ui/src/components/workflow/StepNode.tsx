/**
 * Custom node component for workflow steps
 */
import { memo } from 'react';
import { Handle, NodeProps, Position } from 'reactflow';

/**
 * Type for step node data
 */
export interface StepNodeData {
  label: string;
  description?: string;
  component?: string;
  step: Record<string, unknown>;
}

/**
 * Custom node component for workflow steps
 */
export const StepNode = memo(({ data, isConnectable }: NodeProps<StepNodeData>) => {
  const { label, description, component } = data;
  
  return (
    <div className="step-node">
      <Handle
        type="target"
        position={Position.Left}
        isConnectable={isConnectable}
      />
      <div className="step-node-content">
        <div className="step-node-header">{label}</div>
        {description && (
          <div className="step-node-description">{description}</div>
        )}
        {component && (
          <div className="step-node-component">{component}</div>
        )}
      </div>
      <Handle
        type="source"
        position={Position.Right}
        isConnectable={isConnectable}
      />
    </div>
  );
}); 