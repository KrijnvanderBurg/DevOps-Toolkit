#!/bin/bash

# Default values
pyproject_filepath="${1:-$PWD}/pyproject.toml"  
requirements_filepath="${2:-$PWD/runtime/requirements.txt}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --pyproject_filepath=*) pyproject_filepath="${i#*=}" ;;
    --requirements_filepath=*) requirements_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pip install poetry --quiet

# Print the current poetry version
echo "poetry version:"
poetry --version

# Scanning the target folder with poetry
echo "Scanning folder: $pyproject_filepath"
echo "output filepath: $requirements_filepath"

poetry export --directory "$pyproject_filepath" \
  --without-hashes \
  --format requirements.txt \
  | tee "$requirements_filepath"
