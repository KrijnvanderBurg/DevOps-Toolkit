#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install pyre-check --quiet

# Print the current pyre version
echo "pyre version:"
pyre --version

# Scanning the target folder with pyre
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

pyre --source-directory "$target_path" \
  --log-level INFO \
  --noninteractive \
  --sequential check
