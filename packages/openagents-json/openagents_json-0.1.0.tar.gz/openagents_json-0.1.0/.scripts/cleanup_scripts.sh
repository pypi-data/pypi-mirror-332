#!/bin/bash
# Script to clean up unnecessary files for the simplified agentic workflow

echo "Cleaning up unnecessary script files..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Remove each file if it exists
for file in "$SCRIPT_DIR/end_of_cycle_review.sh" "$SCRIPT_DIR/generate_repo_tree.sh" "$SCRIPT_DIR/setup_review_tools.sh" "$SCRIPT_DIR/gh_issue_management/additional_notes.txt"; do
  if [ -f "$file" ]; then
    echo "Removing $file"
    rm "$file"
  fi
done

echo "Cleanup complete!"
