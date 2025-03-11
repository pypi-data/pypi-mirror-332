import { useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import { useWorkflowStore } from './state/workflowStore'
import './App.css'

// Placeholder components for routes
const WorkflowList = () => {
  const { workflows, fetchWorkflows, isLoading, error } = useWorkflowStore();
  
  useEffect(() => {
    fetchWorkflows();
  }, [fetchWorkflows]);
  
  if (isLoading) return <div>Loading workflows...</div>;
  if (error) return <div>Error: {error}</div>;
  
  return (
    <div>
      <h1>Workflows</h1>
      {workflows.length === 0 ? (
        <p>No workflows found</p>
      ) : (
        <ul>
          {workflows.map(workflow => (
            <li key={workflow.id}>
              <Link to={`/ui/workflows/${workflow.id}`}>{workflow.name || workflow.id}</Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

const WorkflowDetail = () => {
  return <div>Workflow Detail (Coming Soon)</div>;
};

const WorkflowEditor = () => {
  return <div>Workflow Editor (Coming Soon)</div>;
};

const WorkflowVisualizer = () => {
  return <div>Workflow Visualizer (Coming Soon)</div>;
};

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>OpenAgents JSON</h1>
        <nav>
          <Link to="/ui/">Home</Link>
          <Link to="/ui/workflows">Workflows</Link>
          <Link to="/ui/editor">Editor</Link>
        </nav>
      </header>
      
      <main className="app-content">
        <Routes>
          <Route path="/" element={<div>Welcome to OpenAgents JSON Workflow UI</div>} />
          <Route path="/workflows" element={<WorkflowList />} />
          <Route path="/workflows/:id" element={<WorkflowDetail />} />
          <Route path="/editor" element={<WorkflowEditor />} />
          <Route path="/visualizer" element={<WorkflowVisualizer />} />
          <Route path="*" element={<div>Page not found</div>} />
        </Routes>
      </main>
      
      <footer className="app-footer">
        <p>OpenAgents JSON Workflow UI</p>
      </footer>
    </div>
  )
}

export default App
