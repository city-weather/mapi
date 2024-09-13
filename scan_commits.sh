#!/bin/bash

# Save the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Get all commit hashes
commits=$(git rev-list --all)

# Iterate over each commit and run gitleaks
for commit in $commits
do
    echo "Scanning commit: $commit"
    git checkout $commit
    gitleaks detect --source . --log-opts "$commit"
done

# Go back to the original branch
#Adding comment
git checkout "$current_branch"