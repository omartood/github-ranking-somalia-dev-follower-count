#!/bin/bash

echo "🧹 Cleaning repository from sensitive data..."

# Remove the problematic commits from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch .env.example' \
  --prune-empty --tag-name-filter cat -- --all

# Clean up
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo "✅ Repository cleaned!"
echo "Now you can push safely with: git push --force-with-lease"