#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/.pyright}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

# Print the current pyright version
echo "pyright version:"
pyright --version

# Scanning the target folder with pyright
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

pyright "$target_path" \
  --project "$config_filepath"
  --level warning
  --warnings
