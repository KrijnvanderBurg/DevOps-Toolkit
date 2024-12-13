#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.ruff}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install ruff --quiet --force

# Print the current ruff version
echo "ruff version:"
ruff --version

# Scanning the target folder with ruff
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

ruff format "$target_path" \
  --config "$config_filepath" \
  --diff 
