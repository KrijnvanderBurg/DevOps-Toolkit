#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/trufflehog}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b $HOME/.local/bin

# Print the current TruffleHog version
echo "TruffleHog version:"
trufflehog --version

# Scanning the target folder with TruffleHog
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"

trufflehog git "$target_path" \
  --config "$config_filepath" \
  --no-update \
  --include-detectors="all" \
  --only-verified \
  --fail
