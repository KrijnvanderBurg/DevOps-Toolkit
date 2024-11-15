#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.bandit}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install bandit --quiet

# Print the current bandit version
echo "bandit version:"
bandit --version

# Scanning the target folder with bandit
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

bandit -r "$target_path" \
  -c "$config_filepath"
