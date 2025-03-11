import { describe, expect, it, vi, beforeEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { WorkflowDiagram } from './WorkflowDiagram';
import workflowApi from '../../api/workflowApi';
import { act } from 'react';

// Properly type the hook returns to avoid undefined is not iterable error
const mockNodesState = [[], vi.fn(), vi.fn()];
const mockEdgesState = [[], vi.fn(), vi.fn()];

// Mock the workflow API
vi.mock('../../api/workflowApi', () => ({
  default: {
    getVisualizationData: vi.fn(),
  },
}));

// Mock React Flow module
vi.mock('reactflow', () => {
  return {
    __esModule: true,
    default: vi.fn().mockImplementation(({ children }) => (
      <div data-testid="react-flow-mock">
        {children}
        <div data-testid="nodes-container"></div>
        <div data-testid="edges-container"></div>
      </div>
    )),
    Controls: vi.fn().mockImplementation(() => <div data-testid="react-flow-controls"></div>),
    MiniMap: vi.fn().mockImplementation(() => <div data-testid="react-flow-minimap"></div>),
    Background: vi.fn().mockImplementation(() => <div data-testid="react-flow-background"></div>),
    Panel: vi.fn().mockImplementation(({ children }) => <div data-testid="react-flow-panel">{children}</div>),
    useNodesState: () => mockNodesState,
    useEdgesState: () => mockEdgesState,
    addEdge: vi.fn().mockImplementation((connection, edges) => edges),
  };
});

// Sample visualization data
const mockVisualizationData = {
  nodes: [
    {
      id: 'node-1',
      type: 'step',
      position: { x: 100, y: 100 },
      data: { label: 'Test Node 1' },
    },
    {
      id: 'node-2',
      type: 'step',
      position: { x: 300, y: 100 },
      data: { label: 'Test Node 2' },
    },
  ],
  edges: [
    {
      id: 'edge-1-2',
      source: 'node-1',
      target: 'node-2',
    },
  ],
};

describe('WorkflowDiagram', () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });
  
  it('should show loading state initially', () => {
    // Mock API to delay response
    vi.mocked(workflowApi.getVisualizationData).mockReturnValue(
      new Promise(() => {}) // Never resolves to keep loading state
    );
    
    // Render the component
    render(<WorkflowDiagram workflowId="test-workflow" />);
    
    // Check loading state is shown
    expect(screen.getByText(/loading workflow diagram/i)).toBeInTheDocument();
  });
  
  it('should show error state when API fails', async () => {
    // Mock API to return error
    const errorMessage = 'Failed to load visualization';
    vi.mocked(workflowApi.getVisualizationData).mockRejectedValueOnce(new Error(errorMessage));
    
    // Render the component
    render(<WorkflowDiagram workflowId="test-workflow" />);
    
    // Wait for error state to be shown
    await waitFor(() => {
      expect(screen.getByText(/error:/i)).toBeInTheDocument();
    });
    
    // Use a more flexible text matcher for the error message
    expect(screen.getByText((content) => content.includes(errorMessage))).toBeInTheDocument();
  });
  
  it('should update state with visualization data when loaded', async () => {
    // Mock the API implementation to resolve immediately with data
    vi.mocked(workflowApi.getVisualizationData).mockImplementation(() => {
      return Promise.resolve(mockVisualizationData);
    });
    
    // Mock the nodes/edges state setters
    const setNodesMock = vi.fn();
    const setEdgesMock = vi.fn();
    
    // Update the mock state to include the setter functions
    mockNodesState[1] = setNodesMock;
    mockEdgesState[1] = setEdgesMock;
    
    // Render the component
    await act(async () => {
      render(<WorkflowDiagram workflowId="test-workflow" />);
    });
    
    // Verify the API was called
    expect(workflowApi.getVisualizationData).toHaveBeenCalledWith('test-workflow');
    
    // Verify the setters were called with the mock data
    expect(setNodesMock).toHaveBeenCalledWith(mockVisualizationData.nodes);
    expect(setEdgesMock).toHaveBeenCalledWith(mockVisualizationData.edges);
  });
  
  it('should call API with correct workflow ID', () => {
    // Render the component with a specific workflow ID
    render(<WorkflowDiagram workflowId="specific-workflow-id" />);
    
    // Check that API was called with correct workflow ID
    expect(workflowApi.getVisualizationData).toHaveBeenCalledWith('specific-workflow-id');
  });
}); 