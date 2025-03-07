# JobManager Implementation Plan

## Issue Summary
Issue [#31](https://github.com/nznking/openagents-json/issues/31) requires the development of a robust JobManager class for the OpenAgents JSON framework to create and control workflow execution instances. The JobManager will be a central component for managing the lifecycle of jobs created from workflow definitions.

## Current State Analysis

The current codebase has:
- A minimal JobManager class in core/app.py with basic functionality
- Simple job creation with sequential numeric IDs (job_0, job_1, etc.)
- Basic get_job_status and get_job_results methods
- In-memory storage only with no persistence
- No implementation of job control, prioritization, or cancellation
- No workflow instantiation or execution tracking

### Relevant Code
The existing JobManager class in core/app.py provides:
- In-memory job storage using a dictionary
- Simple job creation with basic metadata
- Job status retrieval
- Job results retrieval for completed jobs

The core/config.py file includes job-related settings:
- job_store_type (memory, file, database)
- job_store_path for file-based storage
- job_retention_days for job history retention

## Requirements Analysis

### Job Creation and Management
- Create jobs from workflow definitions
- Generate unique job IDs (replacing the simple counter)
- Retrieve jobs by ID
- List jobs with filtering capabilities
- Implement job cleanup mechanisms

### Workflow Integration
- Instantiate workflows
- Validate inputs against workflow schema
- Map inputs to workflow parameters
- Initialize job execution context

### Execution Control
- Start/stop/pause job execution
- Track execution progress
- Handle step transitions
- Detect job completion

### Cancellation
- Implement graceful cancellation
- Add forced termination capabilities
- Clean up resources after cancellation
- Generate cancellation events

### Prioritization
- Implement priority levels for jobs
- Manage execution queue based on priority
- Allocate resources according to priority

## Technical Design

### Job Model
```python
from enum import Enum
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid

class JobStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

class JobPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Job:
    """
    Represents a workflow job instance.
    """
    
    def __init__(
        self,
        workflow_id: str,
        inputs: Dict[str, Any],
        priority: JobPriority = JobPriority.MEDIUM
    ):
        self.id = str(uuid.uuid4())
        self.workflow_id = workflow_id
        self.inputs = inputs
        self.outputs: Dict[str, Any] = {}
        self.status = JobStatus.CREATED
        self.priority = priority
        self.created_at = datetime.now()
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.current_step: Optional[str] = None
        self.steps: Dict[str, Dict[str, Any]] = {}
        self.errors: List[Dict[str, Any]] = []
```

### Storage Layer
```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class JobStore(ABC):
    """
    Abstract base class for job storage implementations.
    """
    
    @abstractmethod
    async def save_job(self, job: 'Job') -> None:
        """Save a job to the store."""
        pass
        
    @abstractmethod
    async def get_job(self, job_id: str) -> 'Job':
        """Get a job by ID."""
        pass
        
    @abstractmethod
    async def list_jobs(self, filters: Dict[str, Any] = None) -> List['Job']:
        """List jobs with optional filtering."""
        pass
        
    @abstractmethod
    async def delete_job(self, job_id: str) -> None:
        """Delete a job."""
        pass
        
    @abstractmethod
    async def cleanup_old_jobs(self, days: int = 7) -> int:
        """Clean up old jobs and return count of deleted jobs."""
        pass


class MemoryJobStore(JobStore):
    """
    In-memory implementation of job storage.
    """
    
    def __init__(self):
        self.jobs: Dict[str, 'Job'] = {}
        
    async def save_job(self, job: 'Job') -> None:
        self.jobs[job.id] = job
        
    async def get_job(self, job_id: str) -> 'Job':
        if job_id not in self.jobs:
            raise ValueError(f"Job {job_id} not found")
        return self.jobs[job_id]
        
    async def list_jobs(self, filters: Dict[str, Any] = None) -> List['Job']:
        if not filters:
            return list(self.jobs.values())
            
        result = []
        for job in self.jobs.values():
            matches = True
            for key, value in filters.items():
                if getattr(job, key, None) != value:
                    matches = False
                    break
            if matches:
                result.append(job)
        return result
        
    async def delete_job(self, job_id: str) -> None:
        if job_id in self.jobs:
            del self.jobs[job_id]
            
    async def cleanup_old_jobs(self, days: int = 7) -> int:
        # Implementation to clean up jobs older than specified days
        pass
```

### JobManager Class
```python
class JobManager:
    """
    Manages the creation, execution, and lifecycle of workflow jobs.
    """
    
    def __init__(self, store_type: str = "memory"):
        """
        Initialize the JobManager.
        
        Args:
            store_type: Type of storage to use (memory, file, database)
        """
        # Initialize storage
        # Setup execution engine
        # Initialize event system
        
    # Job CRUD operations
    async def create_job(self, workflow_id: str, inputs: Dict[str, Any], priority: str = "MEDIUM") -> str:
        """Create a new job from a workflow"""
        
    async def get_job(self, job_id: str) -> Job:
        """Get a job by ID"""
        
    async def list_jobs(self, filters: Dict[str, Any] = None) -> List[Job]:
        """List jobs with optional filtering"""
        
    async def delete_job(self, job_id: str) -> None:
        """Delete a job"""
        
    # Job execution control
    async def start_job(self, job_id: str) -> None:
        """Start job execution"""
        
    async def pause_job(self, job_id: str) -> None:
        """Pause job execution"""
        
    async def resume_job(self, job_id: str) -> None:
        """Resume paused job"""
        
    async def cancel_job(self, job_id: str, force: bool = False) -> None:
        """Cancel a job, optionally force immediate termination"""
        
    # Status and results
    async def get_job_status(self, job_id: str) -> Dict[str, Any]:
        """Get detailed job status"""
        
    async def get_job_results(self, job_id: str) -> Dict[str, Any]:
        """Get job results"""
        
    # Maintenance
    async def cleanup_old_jobs(self, days: int = 7) -> int:
        """Clean up old jobs and return count of deleted jobs"""
```

## Implementation Plan

### Phase 1: Core Job Management Structure (Days 1-3)

#### Day 1: Initial Setup
- Create basic directory structure for job module
- Define job models and enums
- Implement basic in-memory storage layer

#### Day 2: Core JobManager Implementation
- Implement job creation with UUID generation
- Create job retrieval methods
- Add job listing with filtering

#### Day 3: Job Lifecycle Management
- Implement job cleanup mechanisms
- Add basic job state transitions
- Create job deletion functionality

**Checkpoint 1:** Basic JobManager implementation with CRUD operations completed and tested

### Phase 2: Workflow Integration (Days 4-6)

#### Day 4: Workflow-Job Connection
- Define interfaces between workflows and jobs
- Implement workflow instantiation logic
- Create job context initialization

#### Day 5: Input Validation and Mapping
- Implement input validation against workflow schema
- Create input mapping to workflow parameters
- Add error handling for invalid inputs

#### Day 6: Job ID and Metadata Generation
- Implement job ID generation with workflow context
- Add metadata collection from workflow
- Create detailed job creation pipeline

**Checkpoint 2:** JobManager can create jobs from workflow definitions with proper validation

### Phase 3: Execution Control (Days 7-9)

#### Day 7: Job State Machine
- Implement job execution state machine
- Create start/stop/pause control methods
- Add execution context tracking

#### Day 8: Step Transition Handling
- Implement step transition logic
- Create step execution context
- Add error handling for step failures

#### Day 9: Event System
- Implement event system for job state changes
- Add job completion detection
- Create event listeners for job lifecycle events

**Checkpoint 3:** Jobs can be controlled and their execution can be tracked with state transitions

### Phase 4: Cancellation System (Days 10-11)

#### Day 10: Graceful Cancellation
- Implement graceful cancellation mechanics
- Add resource tracking for cleanup
- Create cancellation event triggers

#### Day 11: Forced Termination
- Implement forced termination logic
- Add cleanup processes for cancelled jobs
- Create comprehensive cancellation notifications

**Checkpoint 4:** Jobs can be cancelled gracefully or forcefully with proper cleanup

### Phase 5: Prioritization (Days 12-13)

#### Day 12: Priority Queue Implementation
- Define priority levels and queue structure
- Implement priority-based job queue
- Create scheduling logic based on priority

#### Day 13: Resource Allocation
- Implement resource allocation based on priority
- Add priority adjustment capabilities
- Create comprehensive priority management system

**Checkpoint 5:** Jobs are executed according to their priority with appropriate resource allocation

## Testing Strategy

### Unit Tests
- Test each method of JobManager class in isolation
- Validate job state transitions
- Test error handling and edge cases

### Integration Tests
- Test integration with workflow system
- Validate end-to-end job lifecycle
- Test concurrent job execution

### Performance Tests
- Test job scheduling performance under load
- Validate priority-based execution
- Test cancellation performance

## Documentation Strategy

### Code Documentation
- Add detailed docstrings to all classes and methods
- Document exception handling and error states
- Include usage examples in module documentation

### User Documentation
- Create usage guides for JobManager API
- Document job lifecycle and state transitions
- Add examples for common job management scenarios

## Dependencies

### Required Issue Completions
- Issue #30: Define Workflow Schema (high-priority)
- Issue #28: Implement ComponentRegistry Class (high-priority)

### Impacts Other Issues
- Issue #34: Create Job Execution Engine
- Issue #37: Implement Job State Management

## Risk Assessment

### Potential Challenges
- Complexity of state management across distributed components
- Error handling in long-running jobs
- Resource management during cancellation
- Performance implications of prioritization

### Mitigation Strategies
- Implement comprehensive logging
- Create robust error recovery mechanisms
- Design thorough resource tracking
- Implement efficient priority queue algorithms

## Development Statistics

### Traditional Development Estimates
- Analysis and planning: 2 days
- Initial implementation: 5 days
- Testing and debugging: 3 days
- Documentation: 1 day
- Integration and review: 2 days
- Total traditional time: 13 days (as stated in the issue)

### AI-Assisted Development Estimates
- Analysis with AI assistance: 0.5 days
- Implementation with AI guidance: 3 days
- Testing with AI test case generation: 1 day
- Documentation with AI assistance: 0.5 days
- Integration and review with AI checks: 1 day
- Total AI-assisted time: 6 days

### Savings Analysis
- Time saved: 7 days (54% reduction)
- Development velocity improvement: 2.17x faster
- Quality improvements:
  - More consistent documentation
  - Better test coverage
  - More comprehensive error handling
  - Improved code structure and organization 