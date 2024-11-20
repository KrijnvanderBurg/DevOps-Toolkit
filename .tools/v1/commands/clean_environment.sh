#!/bin/bash

# List of directories to remove
directories_to_clean=(
    "__pycache__"
    ".mypy_cache"
    ".nox"
    ".pyre"
    ".pytest_cache"
    ".venv"
    "runtime"
    "logs"
)

# List of files to remove
files_to_clean=(
    ".coverage"
    "coverage.xml"
    "JUNIT-TEST.xml"
)

echo "Cleaning up temporary and generated project files..."

# Remove directories
for dir in "${directories_to_clean[@]}"; do
    find . -maxdepth 2 -type d -name "$dir" -exec rm -rf {} + 2>/dev/null
    echo "Removed directory (if found): $dir"
done

# Remove files
for file in "${files_to_clean[@]}"; do
    find . -maxdepth 2 -type f -name "$file" -exec rm -f {} + 2>/dev/null
    echo "Removed file (if found): $file"
done

echo "Cleanup complete."
