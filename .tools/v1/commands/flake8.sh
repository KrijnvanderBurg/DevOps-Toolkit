#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.flake8}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install flake8 --quiet

# Print the current flake8 version
echo "flake8 version:"
flake8 --version

# Scanning the target folder with flake8
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

flake8 "$target_path" \
  --config "$config_filepath"
