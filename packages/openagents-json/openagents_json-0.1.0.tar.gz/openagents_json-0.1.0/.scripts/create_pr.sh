#!/bin/bash

# Exit on error
set -e

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Error: Not in a git repository."
  exit 1
fi

# Get the current branch name
CURRENT_BRANCH=$(git symbolic-ref --short HEAD)
echo "Current branch: $CURRENT_BRANCH"

# Get a description of the changes from the user
echo "Please enter a detailed description of your changes (multi-line, press Ctrl+D when done):"
DESCRIPTION=$(cat)

# Create a commit message with a title and description
COMMIT_TITLE=$(echo "$DESCRIPTION" | head -n 1)
COMMIT_BODY=$(echo "$DESCRIPTION" | tail -n +2)

# Stage all changes
echo "Staging all changes..."
git add -A

# Commit the changes
echo "Committing changes with message: $COMMIT_TITLE"
if [ -z "$COMMIT_BODY" ]; then
  git commit -m "$COMMIT_TITLE"
else
  git commit -m "$COMMIT_TITLE" -m "$COMMIT_BODY"
fi

# Push to the remote repository
echo "Pushing changes to remote..."
git push -u origin "$CURRENT_BRANCH"

# Create a pull request using GitHub CLI
echo "Creating pull request to main branch..."
gh pr create --base main --head "$CURRENT_BRANCH" --title "$COMMIT_TITLE" --body "$DESCRIPTION"

echo "Done! Pull request created. The branch '$CURRENT_BRANCH' remains open." 