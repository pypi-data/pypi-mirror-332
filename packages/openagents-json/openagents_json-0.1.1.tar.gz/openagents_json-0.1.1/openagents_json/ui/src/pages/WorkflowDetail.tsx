/**
 * Workflow detail page
 */
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import { WorkflowDiagram } from '../components/workflow/WorkflowDiagram';
import workflowApi from '../api/workflowApi';
import { Workflow } from '../types/workflow';
import './pages.css';

/**
 * Workflow detail page component
 */
export const WorkflowDetail = () => {
  // Get workflow ID from URL params
  const { id } = useParams<{ id: string }>();
  
  // State for workflow data, loading, and errors
  const [workflow, setWorkflow] = useState<Workflow | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  
  // Load workflow data when the component mounts or ID changes
  useEffect(() => {
    async function loadWorkflow() {
      if (!id) {
        setError('No workflow ID provided');
        setIsLoading(false);
        return;
      }
      
      setIsLoading(true);
      setError(null);
      
      try {
        const workflowData = await workflowApi.getWorkflow(id);
        setWorkflow(workflowData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load workflow');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    }
    
    loadWorkflow();
  }, [id]);
  
  // Show loading state
  if (isLoading) {
    return <div className="loading">Loading workflow...</div>;
  }
  
  // Show error state
  if (error) {
    return <div className="error">Error: {error}</div>;
  }
  
  // Show not found state
  if (!workflow) {
    return <div className="not-found">Workflow not found</div>;
  }
  
  // Render the workflow detail page
  return (
    <div className="workflow-detail">
      <header className="workflow-detail-header">
        <h1>{workflow.name || workflow.id}</h1>
        {workflow.description && <p>{workflow.description}</p>}
        <div className="workflow-meta">
          <span className="workflow-version">Version: {workflow.version}</span>
          {workflow.metadata?.author && (
            <span className="workflow-author">Author: {workflow.metadata.author}</span>
          )}
        </div>
      </header>
      
      <section className="workflow-visualization">
        <h2>Workflow Diagram</h2>
        <WorkflowDiagram workflowId={workflow.id} />
      </section>
      
      <section className="workflow-details">
        <h2>Workflow Details</h2>
        
        <div className="workflow-section">
          <h3>Inputs</h3>
          <ul className="workflow-inputs">
            {Object.entries(workflow.inputs).map(([key, param]) => (
              <li key={key}>
                <strong>{key}</strong>: {param.description || param.type}
                {param.required && <span className="required">*</span>}
              </li>
            ))}
          </ul>
        </div>
        
        <div className="workflow-section">
          <h3>Outputs</h3>
          <ul className="workflow-outputs">
            {Object.entries(workflow.outputs).map(([key, param]) => (
              <li key={key}>
                <strong>{key}</strong>: {param.description || param.type}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}; 