#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.vulture}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install vulture --quiet

# Print the current Vulture version
echo "Vulture version:"
vulture --version

# Scanning the target folder with Vulture
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

vulture "$target_path" \
  --config "$config_filepath"
