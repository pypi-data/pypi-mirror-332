#!/bin/bash
# Script to update GitHub issues with progress information

# Check if the GitHub token is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN environment variable is not set"
    echo "Please set it with: export GITHUB_TOKEN=your_personal_access_token"
    exit 1
fi

# Default values
REPO="nznking/openagents-json"
ISSUE_NUMBER="22"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --repo)
        REPO="$2"
        shift 2
        ;;
        --issue)
        ISSUE_NUMBER="$2"
        shift 2
        ;;
        --update-tasks)
        UPDATE_TASKS="--update-tasks"
        shift
        ;;
        *)
        echo "Unknown option: $key"
        exit 1
        ;;
    esac
done

# Set the GitHub repository environment variable
export GITHUB_REPOSITORY="$REPO"

# Run the Python script with the appropriate arguments
python3 "$SCRIPT_DIR/github_issue_updater.py" \
    --issue "$ISSUE_NUMBER" \
    --completed "$SCRIPT_DIR/completed_tasks.json" \
    --pending "$SCRIPT_DIR/pending_tasks.json" \
    --notes "$(cat "$SCRIPT_DIR/notes.txt")" \
    $UPDATE_TASKS

# Exit with the status of the Python script
exit $? 