#!/bin/bash

# Script to create GitHub issues for monitoring enhancements

# Exit on error
set -e

# Check if GitHub token is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN environment variable is not set"
    echo "Please set it with: export GITHUB_TOKEN=your_personal_access_token"
    exit 1
fi

# Get repository from environment or default
REPO=${GITHUB_REPOSITORY:-"nznking/openagents-json"}

# Create issue function
create_issue() {
    local title="$1"
    local body="$2"
    local labels="$3"
    
    echo "Creating issue: $title"
    
    # Use GitHub CLI if available
    if command -v gh >/dev/null 2>&1; then
        gh issue create --repo "$REPO" --title "$title" --body "$body" --label "$labels"
    else
        # Fallback to curl
        curl -s -X POST \
            -H "Authorization: token $GITHUB_TOKEN" \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/repos/$REPO/issues" \
            -d "{\"title\":\"$title\",\"body\":\"$body\",\"labels\":[$labels]}"
    fi
    
    echo "Issue created: $title"
    # Avoid rate limiting
    sleep 2
}

# Enhancement 1: UI Dashboard
title="[Enhancement] UI Dashboard for Monitoring Visualization"
body="## Overview
Create a web-based dashboard for visualizing job metrics and system health.

## Objectives
- Design a responsive dashboard UI for monitoring data
- Implement real-time updates for active metrics
- Create visualizations for job success rates, execution times, and worker status
- Support filtering and time-range selection
- Integrate with the existing monitoring REST API

## Background
This enhancement builds on the monitoring and observability system to provide a visual interface for metrics data. The UI dashboard will make it easier for users to track job execution, identify patterns, and troubleshoot issues.

## Acceptance Criteria
- [ ] Dashboard displays key metrics from jobs, workers, and system
- [ ] Real-time updates for active metrics
- [ ] Graphs and charts for historical data
- [ ] Responsive design for different screen sizes
- [ ] Documentation for setup and customization
- [ ] Example deployment configuration

## Related Work
- Builds on the monitoring and observability implementation (Issue #31)
- Should integrate with the existing monitoring REST API"
labels="\"enhancement\", \"ui\", \"monitoring\""

create_issue "$title" "$body" "$labels"

# Enhancement 2: External Monitoring Tool Integrations
title="[Enhancement] External Monitoring Tool Integrations"
body="## Overview
Add connectors for popular monitoring tools like Prometheus and Grafana.

## Objectives
- Implement metrics export for Prometheus
- Create sample Grafana dashboards
- Support statsd/DogStatsD protocol for metric forwarding
- Add documentation for integration with external monitoring systems

## Background
While the built-in monitoring system provides essential metrics, many organizations use dedicated monitoring tools like Prometheus and Grafana for their observability needs. This enhancement will allow the OpenAgents JSON framework to integrate with these external systems.

## Acceptance Criteria
- [ ] Prometheus metrics endpoint with configurable export
- [ ] Sample Grafana dashboards for job metrics
- [ ] statsd/DogStatsD support for metric forwarding
- [ ] Configuration options for external integrations
- [ ] Documentation for setup and customization
- [ ] Example deployment configurations

## Related Work
- Builds on the monitoring and observability implementation (Issue #31)
- Should leverage the existing metrics collection system"
labels="\"enhancement\", \"integration\", \"monitoring\""

create_issue "$title" "$body" "$labels"

# Enhancement 3: Alerting System
title="[Enhancement] Configurable Alerting System for Metrics"
body="## Overview
Implement a configurable alerting system based on metrics thresholds.

## Objectives
- Create an alert configuration system with threshold definitions
- Implement alert generation based on metric values
- Support multiple notification channels (email, webhook, etc.)
- Add alert history and management
- Provide a user interface for alert configuration

## Background
Monitoring systems are most effective when they can proactively notify users of potential issues. This enhancement will add alerting capabilities to the existing monitoring system, allowing users to define thresholds and receive notifications when metrics exceed those thresholds.

## Acceptance Criteria
- [ ] Alert configuration system with threshold definitions
- [ ] Support for multiple notification channels
- [ ] Alert history and management
- [ ] User interface for alert configuration
- [ ] Documentation for setup and customization
- [ ] Example alert configurations

## Related Work
- Builds on the monitoring and observability implementation (Issue #31)
- Should integrate with the UI Dashboard enhancement"
labels="\"enhancement\", \"alerting\", \"monitoring\""

create_issue "$title" "$body" "$labels"

# Enhancement 4: Historical Metrics Storage
title="[Enhancement] Persistent Historical Metrics Storage"
body="## Overview
Add database backends for long-term metrics storage and historical analysis.

## Objectives
- Implement persistent storage for metrics data
- Support multiple database backends (PostgreSQL, SQLite, etc.)
- Add data retention policies and aggregation
- Create historical data query API
- Develop migration path from in-memory to persistent storage

## Background
The current monitoring system stores metrics in memory, which limits historical analysis and doesn't persist across restarts. This enhancement will add support for storing metrics in databases, enabling long-term trend analysis and historical reporting.

## Acceptance Criteria
- [ ] Persistent storage implementation for metrics data
- [ ] Support for multiple database backends
- [ ] Data retention policies and aggregation
- [ ] Historical data query API
- [ ] Migration path from in-memory to persistent storage
- [ ] Documentation for setup and configuration
- [ ] Performance benchmarks for different storage backends

## Related Work
- Builds on the monitoring and observability implementation (Issue #31)
- Should integrate with the UI Dashboard enhancement for historical data visualization"
labels="\"enhancement\", \"storage\", \"monitoring\""

create_issue "$title" "$body" "$labels"

# Enhancement 5: Performance Optimizations
title="[Enhancement] Performance Optimizations for High-Volume Event Processing"
body="## Overview
Optimize event handling and metrics collection for high-throughput applications.

## Objectives
- Benchmark current event processing performance
- Identify and address bottlenecks in event handling
- Implement batched event processing
- Add sampling options for high-volume metrics
- Optimize memory usage for metrics storage
- Create performance testing suite for monitoring components

## Background
In high-throughput applications with many events per second, monitoring overhead can become significant. This enhancement focuses on optimizing the event system and metrics collection to minimize performance impact while maintaining comprehensive observability.

## Acceptance Criteria
- [ ] Performance benchmarks for event processing
- [ ] Batched event processing implementation
- [ ] Sampling options for high-volume metrics
- [ ] Memory usage optimizations
- [ ] Performance testing suite
- [ ] Documentation for performance tuning
- [ ] Comparison benchmarks showing improvement

## Related Work
- Builds on the monitoring and observability implementation (Issue #31)
- Related to Historical Metrics Storage enhancement for efficient data handling"
labels="\"enhancement\", \"performance\", \"monitoring\""

create_issue "$title" "$body" "$labels"

echo "All enhancement issues created successfully" 