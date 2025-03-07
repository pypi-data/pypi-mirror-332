#!/bin/bash
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN environment variable is not set"
    echo "Please set it with: export GITHUB_TOKEN=your_personal_access_token"
    exit 1
fi
./update_issue.sh --issue 31 --update-tasks
