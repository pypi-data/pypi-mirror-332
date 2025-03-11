"""
Monitoring and observability for job execution in the OpenAgents JSON framework.

This module provides monitoring components for tracking job execution metrics,
collecting statistics, and enabling observability of the job system. It leverages
the event system to gather real-time information about job lifecycle events and
system performance.
"""

import asyncio
import collections
import json
import logging
import time
from datetime import datetime, timedelta
from threading import Lock
from typing import Any, Deque, Dict, List, Optional, Set, Tuple, Union

from openagents_json.job.events import Event, EventType, event_emitter
from openagents_json.job.model import Job, JobStatus

logger = logging.getLogger(__name__)


class JobMetrics:
    """
    Collects and stores metrics for job execution.

    Tracks job execution times, success/failure rates, retry counts,
    and other metrics for performance analysis and reporting.
    """

    def __init__(self, max_history: int = 1000):
        """
        Initialize job metrics collector.

        Args:
            max_history: Maximum number of job executions to keep in history
        """
        self._lock = Lock()
        self._max_history = max_history

        # General stats
        self._job_count = 0
        self._job_success_count = 0
        self._job_failure_count = 0
        self._job_cancel_count = 0

        # Time metrics (in seconds)
        self._total_execution_time = 0.0
        self._min_execution_time = float("inf")
        self._max_execution_time = 0.0

        # Job history for recent jobs (FIFO queue)
        self._job_history: Deque[Dict[str, Any]] = collections.deque(maxlen=max_history)

        # Metrics by job tag
        self._tag_metrics: Dict[str, Dict[str, Any]] = {}

        # Metrics by priority
        self._priority_metrics: Dict[str, Dict[str, Any]] = {}

        # Start/end times for currently running jobs
        self._job_start_times: Dict[str, float] = {}

        # Register event handlers
        event_emitter.on(EventType.JOB_STARTED, self._on_job_started)
        event_emitter.on(EventType.JOB_COMPLETED, self._on_job_completed)
        event_emitter.on(EventType.JOB_FAILED, self._on_job_failed)
        event_emitter.on(EventType.JOB_CANCELLED, self._on_job_cancelled)

    def _on_job_started(self, event: Event) -> None:
        """
        Handle job started event.

        Args:
            event: Job started event
        """
        with self._lock:
            self._job_count += 1
            self._job_start_times[event.job_id] = time.time()

            # Add to tag metrics
            job_data = event.data
            tags = job_data.get("tags", [])
            for tag in tags:
                if tag not in self._tag_metrics:
                    self._tag_metrics[tag] = {
                        "count": 0,
                        "success": 0,
                        "failure": 0,
                        "cancelled": 0,
                        "total_time": 0.0,
                    }
                self._tag_metrics[tag]["count"] += 1

            # Add to priority metrics
            priority = job_data.get("priority", "medium")
            if priority not in self._priority_metrics:
                self._priority_metrics[priority] = {
                    "count": 0,
                    "success": 0,
                    "failure": 0,
                    "cancelled": 0,
                    "total_time": 0.0,
                }
            self._priority_metrics[priority]["count"] += 1

    def _on_job_completed(self, event: Event) -> None:
        """
        Handle job completed event.

        Args:
            event: Job completed event
        """
        job_id = event.job_id
        if not job_id:
            return

        with self._lock:
            self._job_success_count += 1

            # Calculate execution time
            if job_id in self._job_start_times:
                start_time = self._job_start_times.pop(job_id)
                execution_time = time.time() - start_time

                self._total_execution_time += execution_time
                self._min_execution_time = min(self._min_execution_time, execution_time)
                self._max_execution_time = max(self._max_execution_time, execution_time)

                # Add to job history
                job_data = event.data
                history_entry = {
                    "job_id": job_id,
                    "name": job_data.get("name", ""),
                    "status": "completed",
                    "execution_time": execution_time,
                    "tags": job_data.get("tags", []),
                    "priority": job_data.get("priority", "medium"),
                    "created_at": job_data.get("created_at"),
                    "completed_at": job_data.get("completed_at"),
                }
                self._job_history.append(history_entry)

                # Update tag metrics
                tags = job_data.get("tags", [])
                for tag in tags:
                    if tag in self._tag_metrics:
                        self._tag_metrics[tag]["success"] += 1
                        self._tag_metrics[tag]["total_time"] += execution_time

                # Update priority metrics
                priority = job_data.get("priority", "medium")
                if priority in self._priority_metrics:
                    self._priority_metrics[priority]["success"] += 1
                    self._priority_metrics[priority]["total_time"] += execution_time

    def _on_job_failed(self, event: Event) -> None:
        """
        Handle job failed event.

        Args:
            event: Job failed event
        """
        job_id = event.job_id
        if not job_id:
            return

        with self._lock:
            self._job_failure_count += 1

            # Calculate execution time
            if job_id in self._job_start_times:
                start_time = self._job_start_times.pop(job_id)
                execution_time = time.time() - start_time

                # Add to job history
                job_data = event.data
                history_entry = {
                    "job_id": job_id,
                    "name": job_data.get("name", ""),
                    "status": "failed",
                    "execution_time": execution_time,
                    "tags": job_data.get("tags", []),
                    "priority": job_data.get("priority", "medium"),
                    "created_at": job_data.get("created_at"),
                    "failed_at": job_data.get("updated_at"),
                    "error": job_data.get("error"),
                }
                self._job_history.append(history_entry)

                # Update tag metrics
                tags = job_data.get("tags", [])
                for tag in tags:
                    if tag in self._tag_metrics:
                        self._tag_metrics[tag]["failure"] += 1

                # Update priority metrics
                priority = job_data.get("priority", "medium")
                if priority in self._priority_metrics:
                    self._priority_metrics[priority]["failure"] += 1

    def _on_job_cancelled(self, event: Event) -> None:
        """
        Handle job cancelled event.

        Args:
            event: Job cancelled event
        """
        job_id = event.job_id
        if not job_id:
            return

        with self._lock:
            self._job_cancel_count += 1

            # Calculate execution time if the job had started
            if job_id in self._job_start_times:
                start_time = self._job_start_times.pop(job_id)
                execution_time = time.time() - start_time

                # Add to job history
                job_data = event.data
                history_entry = {
                    "job_id": job_id,
                    "name": job_data.get("name", ""),
                    "status": "cancelled",
                    "execution_time": execution_time,
                    "tags": job_data.get("tags", []),
                    "priority": job_data.get("priority", "medium"),
                    "created_at": job_data.get("created_at"),
                    "cancelled_at": job_data.get("updated_at"),
                }
                self._job_history.append(history_entry)

                # Update tag metrics
                tags = job_data.get("tags", [])
                for tag in tags:
                    if tag in self._tag_metrics:
                        self._tag_metrics[tag]["cancelled"] += 1

                # Update priority metrics
                priority = job_data.get("priority", "medium")
                if priority in self._priority_metrics:
                    self._priority_metrics[priority]["cancelled"] += 1

    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of job metrics.

        Returns:
            Dictionary with job metrics summary
        """
        with self._lock:
            total_jobs = self._job_count
            success_rate = (
                (self._job_success_count / total_jobs) * 100 if total_jobs > 0 else 0
            )
            failure_rate = (
                (self._job_failure_count / total_jobs) * 100 if total_jobs > 0 else 0
            )
            cancel_rate = (
                (self._job_cancel_count / total_jobs) * 100 if total_jobs > 0 else 0
            )

            avg_execution_time = (
                self._total_execution_time / self._job_success_count
                if self._job_success_count > 0
                else 0
            )

            return {
                "total_jobs": total_jobs,
                "completed_jobs": self._job_success_count,
                "failed_jobs": self._job_failure_count,
                "cancelled_jobs": self._job_cancel_count,
                "success_rate": success_rate,
                "failure_rate": failure_rate,
                "cancel_rate": cancel_rate,
                "avg_execution_time": avg_execution_time,
                "min_execution_time": (
                    self._min_execution_time
                    if self._min_execution_time != float("inf")
                    else 0
                ),
                "max_execution_time": self._max_execution_time,
                "currently_running": len(self._job_start_times),
            }

    def get_tag_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Get metrics grouped by job tags.

        Returns:
            Dictionary with metrics for each tag
        """
        with self._lock:
            # Calculate averages and rates for each tag
            result = {}
            for tag, metrics in self._tag_metrics.items():
                total = metrics["count"]
                result[tag] = {
                    "total_jobs": total,
                    "completed_jobs": metrics["success"],
                    "failed_jobs": metrics["failure"],
                    "cancelled_jobs": metrics["cancelled"],
                    "success_rate": (
                        (metrics["success"] / total) * 100 if total > 0 else 0
                    ),
                    "failure_rate": (
                        (metrics["failure"] / total) * 100 if total > 0 else 0
                    ),
                    "cancel_rate": (
                        (metrics["cancelled"] / total) * 100 if total > 0 else 0
                    ),
                    "avg_execution_time": (
                        metrics["total_time"] / metrics["success"]
                        if metrics["success"] > 0
                        else 0
                    ),
                }
            return result

    def get_priority_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Get metrics grouped by job priority.

        Returns:
            Dictionary with metrics for each priority level
        """
        with self._lock:
            # Calculate averages and rates for each priority
            result = {}
            for priority, metrics in self._priority_metrics.items():
                total = metrics["count"]
                result[priority] = {
                    "total_jobs": total,
                    "completed_jobs": metrics["success"],
                    "failed_jobs": metrics["failure"],
                    "cancelled_jobs": metrics["cancelled"],
                    "success_rate": (
                        (metrics["success"] / total) * 100 if total > 0 else 0
                    ),
                    "failure_rate": (
                        (metrics["failure"] / total) * 100 if total > 0 else 0
                    ),
                    "cancel_rate": (
                        (metrics["cancelled"] / total) * 100 if total > 0 else 0
                    ),
                    "avg_execution_time": (
                        metrics["total_time"] / metrics["success"]
                        if metrics["success"] > 0
                        else 0
                    ),
                }
            return result

    def get_recent_jobs(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get most recent job executions.

        Args:
            limit: Maximum number of recent jobs to return

        Returns:
            List of recent job execution details
        """
        with self._lock:
            return list(self._job_history)[-limit:]

    def reset(self) -> None:
        """Reset all metrics."""
        with self._lock:
            self._job_count = 0
            self._job_success_count = 0
            self._job_failure_count = 0
            self._job_cancel_count = 0
            self._total_execution_time = 0.0
            self._min_execution_time = float("inf")
            self._max_execution_time = 0.0
            self._job_history.clear()
            self._tag_metrics.clear()
            self._priority_metrics.clear()
            self._job_start_times.clear()


class WorkerMetrics:
    """
    Collects and stores metrics for worker performance.

    Tracks worker heartbeats, job claim rates, execution times,
    and other metrics for worker performance analysis.
    """

    def __init__(self):
        """Initialize worker metrics collector."""
        self._lock = Lock()

        # Worker registrations
        self._workers: Dict[str, Dict[str, Any]] = {}

        # Job claims by worker
        self._worker_job_claims: Dict[str, int] = {}

        # Current workers heartbeat times
        self._worker_heartbeats: Dict[str, float] = {}

        # Register event handlers
        event_emitter.on(EventType.WORKER_REGISTERED, self._on_worker_registered)
        event_emitter.on(EventType.WORKER_HEARTBEAT, self._on_worker_heartbeat)
        event_emitter.on(EventType.WORKER_CLAIMED_JOB, self._on_worker_claimed_job)
        event_emitter.on(EventType.WORKER_OFFLINE, self._on_worker_offline)

    def _on_worker_registered(self, event: Event) -> None:
        """
        Handle worker registered event.

        Args:
            event: Worker registered event
        """
        worker_id = event.worker_id
        if not worker_id:
            return

        with self._lock:
            self._workers[worker_id] = {
                "registered_at": time.time(),
                "host": event.data.get("host", "unknown"),
                "tags": event.data.get("tags", []),
                "max_concurrent_jobs": event.data.get("max_concurrent_jobs", 1),
                "status": "online",
            }

            self._worker_heartbeats[worker_id] = time.time()
            self._worker_job_claims[worker_id] = 0

    def _on_worker_heartbeat(self, event: Event) -> None:
        """
        Handle worker heartbeat event.

        Args:
            event: Worker heartbeat event
        """
        worker_id = event.worker_id
        if not worker_id:
            return

        with self._lock:
            self._worker_heartbeats[worker_id] = time.time()

            if worker_id in self._workers:
                self._workers[worker_id]["status"] = "online"
                self._workers[worker_id]["running_jobs"] = event.data.get(
                    "running_jobs", 0
                )

    def _on_worker_claimed_job(self, event: Event) -> None:
        """
        Handle worker claimed job event.

        Args:
            event: Worker claimed job event
        """
        worker_id = event.worker_id
        if not worker_id:
            return

        with self._lock:
            if worker_id in self._worker_job_claims:
                self._worker_job_claims[worker_id] += 1

    def _on_worker_offline(self, event: Event) -> None:
        """
        Handle worker offline event.

        Args:
            event: Worker offline event
        """
        worker_id = event.worker_id
        if not worker_id:
            return

        with self._lock:
            if worker_id in self._workers:
                self._workers[worker_id]["status"] = "offline"
                self._workers[worker_id]["offline_at"] = time.time()

    def get_worker_status(self, worker_id: str) -> Optional[Dict[str, Any]]:
        """
        Get status information for a specific worker.

        Args:
            worker_id: ID of the worker

        Returns:
            Worker status information or None if not found
        """
        with self._lock:
            if worker_id not in self._workers:
                return None

            worker_info = self._workers[worker_id].copy()

            # Add claim count
            worker_info["jobs_claimed"] = self._worker_job_claims.get(worker_id, 0)

            # Calculate uptime
            if worker_info["status"] == "online":
                worker_info["uptime"] = time.time() - worker_info["registered_at"]
            else:
                worker_info["uptime"] = (
                    worker_info.get("offline_at", time.time())
                    - worker_info["registered_at"]
                )

            # Calculate last heartbeat
            if worker_id in self._worker_heartbeats:
                worker_info["last_heartbeat"] = (
                    time.time() - self._worker_heartbeats[worker_id]
                )

            return worker_info

    def get_all_workers(self) -> Dict[str, Dict[str, Any]]:
        """
        Get status information for all workers.

        Returns:
            Dictionary mapping worker IDs to their status information
        """
        with self._lock:
            result = {}
            for worker_id in self._workers:
                result[worker_id] = self.get_worker_status(worker_id)
            return result

    def get_active_workers_count(self) -> int:
        """
        Get the number of currently active workers.

        Returns:
            Count of active workers
        """
        with self._lock:
            return sum(1 for w in self._workers.values() if w["status"] == "online")

    def reset(self) -> None:
        """Reset all worker metrics."""
        with self._lock:
            self._workers.clear()
            self._worker_job_claims.clear()
            self._worker_heartbeats.clear()


class SystemMetrics:
    """
    Collects and stores system-wide metrics.

    Tracks overall system performance, resource usage, and health metrics.
    """

    def __init__(self):
        """Initialize system metrics collector."""
        self._lock = Lock()

        # System start time
        self._start_time = time.time()

        # Event counters
        self._event_counts: Dict[EventType, int] = {
            event_type: 0 for event_type in EventType
        }

        # Error counts
        self._error_count = 0

        # Queue depth
        self._queue_depth = 0
        self._max_queue_depth = 0

        # Register event handlers
        event_emitter.on_any(self._on_any_event)
        event_emitter.on(EventType.SYSTEM_ERROR, self._on_system_error)

    def _on_any_event(self, event: Event) -> None:
        """
        Handle any event for counting.

        Args:
            event: Any system event
        """
        with self._lock:
            self._event_counts[event.event_type] = (
                self._event_counts.get(event.event_type, 0) + 1
            )

    def _on_system_error(self, event: Event) -> None:
        """
        Handle system error event.

        Args:
            event: System error event
        """
        with self._lock:
            self._error_count += 1

    def update_queue_depth(self, depth: int) -> None:
        """
        Update the current job queue depth.

        Args:
            depth: Current depth of the job queue
        """
        with self._lock:
            self._queue_depth = depth
            self._max_queue_depth = max(self._max_queue_depth, depth)

    def get_system_metrics(self) -> Dict[str, Any]:
        """
        Get system-wide metrics.

        Returns:
            Dictionary with system metrics
        """
        with self._lock:
            uptime = time.time() - self._start_time

            return {
                "uptime": uptime,
                "uptime_formatted": self._format_duration(uptime),
                "queue_depth": self._queue_depth,
                "max_queue_depth": self._max_queue_depth,
                "error_count": self._error_count,
                "event_counts": self._event_counts.copy(),
            }

    def get_event_counts(self) -> Dict[str, int]:
        """
        Get counts of all events by type.

        Returns:
            Dictionary mapping event types to their counts
        """
        with self._lock:
            return {
                event_type.value: count
                for event_type, count in self._event_counts.items()
            }

    def reset(self) -> None:
        """Reset system metrics but keep start time."""
        with self._lock:
            self._event_counts = {event_type: 0 for event_type in EventType}
            self._error_count = 0
            self._queue_depth = 0
            self._max_queue_depth = 0

    def _format_duration(self, seconds: float) -> str:
        """
        Format duration in seconds to human-readable string.

        Args:
            seconds: Duration in seconds

        Returns:
            Formatted duration string
        """
        days, remainder = divmod(int(seconds), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0 or days > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or hours > 0 or days > 0:
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")

        return " ".join(parts)


class Monitor:
    """
    Central monitoring system for job execution and system health.

    Aggregates metrics from various sources, provides query capabilities,
    and manages metric collection lifecycle.
    """

    def __init__(self):
        """Initialize the monitoring system."""
        self.job_metrics = JobMetrics()
        self.worker_metrics = WorkerMetrics()
        self.system_metrics = SystemMetrics()

        # Flag indicating if metrics collection is active
        self._active = True

    def get_complete_status(self) -> Dict[str, Any]:
        """
        Get complete status of the job system.

        Returns:
            Dictionary with comprehensive metrics from all collectors
        """
        if not self._active:
            return {"error": "Monitoring system is disabled"}

        return {
            "jobs": self.job_metrics.get_summary(),
            "workers": {
                "active_count": self.worker_metrics.get_active_workers_count(),
                "workers": self.worker_metrics.get_all_workers(),
            },
            "system": self.system_metrics.get_system_metrics(),
            "tags": self.job_metrics.get_tag_metrics(),
            "priorities": self.job_metrics.get_priority_metrics(),
            "recent_jobs": self.job_metrics.get_recent_jobs(),
        }

    def update_queue_depth(self, depth: int) -> None:
        """
        Update the current job queue depth.

        Args:
            depth: Current depth of the job queue
        """
        if self._active:
            self.system_metrics.update_queue_depth(depth)

    def reset(self) -> None:
        """Reset all metrics collectors."""
        self.job_metrics.reset()
        self.worker_metrics.reset()
        self.system_metrics.reset()

    def disable(self) -> None:
        """Disable metrics collection."""
        self._active = False

    def enable(self) -> None:
        """Enable metrics collection."""
        self._active = True


# Global monitor instance
monitor = Monitor()
