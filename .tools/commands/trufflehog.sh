#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/trufflehog}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin

# Print the current TruffleHog version
echo "TruffleHog version:"
trufflehog --version

# Scanning the target folder with TruffleHog
echo "Config file: $config_filepath"
echo "Scanning folder: file://$target_path"

trufflehog git "$target_path" \
  --config "$config_filepath" \
  --no-update \
  --include-detectors="all" \
  --only-verified \
  --fail


    vulture --version

    vulture ${{ parameters.targetPath }} \
    --config ${{ parameters.configFilepath }} \