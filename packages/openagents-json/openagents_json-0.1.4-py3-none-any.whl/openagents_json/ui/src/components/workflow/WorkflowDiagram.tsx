/**
 * Workflow diagram component using React Flow
 */
import { useCallback, useEffect, useState } from 'react';
import ReactFlow, {
  Controls,
  Background,
  MiniMap,
  Panel,
  useNodesState,
  useEdgesState,
  addEdge,
  Connection,
  NodeTypes
} from 'reactflow';
import 'reactflow/dist/style.css';

import workflowApi from '../../api/workflowApi';
import { StepNode } from './StepNode';
import './workflow.css';

// Define custom node types
const nodeTypes: NodeTypes = {
  step: StepNode
};

// Define props for the component
interface WorkflowDiagramProps {
  workflowId: string;
  readOnly?: boolean;
}

/**
 * Workflow diagram component that visualizes a workflow using React Flow
 */
export const WorkflowDiagram: React.FC<WorkflowDiagramProps> = ({ 
  workflowId, 
  readOnly = true 
}) => {
  // State for loading and errors
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  
  // React Flow state
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  
  // Handle node connections (only used in edit mode)
  const onConnect = useCallback(
    (connection: Connection) => {
      setEdges((eds) => addEdge(connection, eds));
    },
    [setEdges]
  );
  
  // Load visualization data when the component mounts or workflowId changes
  useEffect(() => {
    async function loadVisualizationData() {
      setIsLoading(true);
      setError(null);
      
      try {
        const visualizationData = await workflowApi.getVisualizationData(workflowId);
        setNodes(visualizationData.nodes);
        setEdges(visualizationData.edges);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load workflow visualization');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    }
    
    loadVisualizationData();
  }, [workflowId]);
  
  // Show loading state
  if (isLoading) {
    return <div className="workflow-loading">Loading workflow diagram...</div>;
  }
  
  // Show error state
  if (error) {
    return <div className="workflow-error">Error: {error}</div>;
  }
  
  // Render the workflow diagram
  return (
    <div className="workflow-diagram">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={readOnly ? undefined : onNodesChange}
        onEdgesChange={readOnly ? undefined : onEdgesChange}
        onConnect={readOnly ? undefined : onConnect}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-right"
      >
        <Controls />
        <MiniMap />
        <Background />
        <Panel position="top-right">
          <div className="workflow-info">
            <h3>Workflow: {workflowId}</h3>
          </div>
        </Panel>
      </ReactFlow>
    </div>
  );
}; 