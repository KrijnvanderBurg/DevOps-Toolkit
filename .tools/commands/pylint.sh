#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/.pylintrc}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install pylint --quiet

# Print the current pylint version
echo "pylint version:"
pylint --version

# Scanning the target folder with pylint
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

pylint "$target_path" \
  --rcfile "$config_filepath" \
  --recursive y

echo "Finished."