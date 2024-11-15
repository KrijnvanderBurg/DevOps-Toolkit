#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.mypy.ini}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install mypy --quiet

# Print the current mypy version
echo "mypy version:"
mypy --version

# Scanning the target folder with mypy
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

mypy "$target_path" \
  --config-file "$config_filepath"
