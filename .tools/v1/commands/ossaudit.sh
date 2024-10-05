#!/bin/bash

# Default values
requirements_filepath="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.ossaudit}"  # Default config file path if not specified


# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --requirements_filepath=*) requirements_filepath="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install ossaudit --quiet

# Print the current ossaudit version
echo "ossaudit has no option to print version."

# Scanning the target folder with ossaudit
echo "Config file: $config_filepath"
echo "Scanning folder: $requirements_filepath"

ossaudit -f "$requirements_filepath" \
  --config "$config_filepath"
