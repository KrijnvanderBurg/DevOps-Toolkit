#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.black}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pip install black --quiet

# Print the current black version
echo "black version:"
black --version

# Scanning the target folder with black
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

black "$target_path" \
  --config "$config_filepath" \
  --check \
  --diff \
  --color \
  --verbose
