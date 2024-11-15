#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.semgrep}"  # Default config file path if not specified
output_filepath="${3:-$PWD/semgrep-junit.xml}"  # Default output file

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    --output_filepath=*) output_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install semgrep --quiet

# Running semgrep scan
echo "Config file: $config_filepath"
echo "Scanning folder: $target_path"
echo "Output will be saved to: $output_filepath"

semgrep scan "$target_path" \
  --config "p/default" \
  --config "p/python" \
  --config "$config_filepath" \
  --junit-xml \
  -o "$output_filepath" \
  --strict \
  --error \
  --text \
  --no-autofix \
  --force-color \
  --metrics "off" \
  --oss-only \
  --verbose
