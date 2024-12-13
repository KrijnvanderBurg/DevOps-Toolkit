#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/devskim.json}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

dotnet tool install --global Microsoft.CST.devskim.CLI

# Print the current bandit version
echo "devskim version:"
devskim --version

# Scanning the target folder with bandit
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

devskim analyze --source-code "$target_path" \
  --options-json "$config_filepath" \
  -E