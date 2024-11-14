#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath_pytest="${2:-$PWD/../.tools/pytest.ini}"  # Default config file path if not specified
config_filepath_coverage="${2:-$PWD/../.tools/.coveragerc}"  # Default config file path if not specified
output_filepath="${3:-$PWD/coverage.xml}"  # Default output file

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) TARGET_PATH="${i#*=}" ;;
    --config_filepath_pytest=*) config_filepath_pytest="${i#*=}" ;;
    --config_filepath_coverage=*) config_filepath_coverage="${i#*=}" ;;  # Fix typo here
    --output_filepath=*) output_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

# Running pytest scan
echo "Config file pytest: $config_filepath_pytest"
echo "Config file coverage: $config_filepath_coverage"
echo "Scanning folder: $target_path"
echo "Output will be saved to: $output_filepath"

pytest ./src/ ./tests/unit \
-o cache_dir=./.pytest_cache \
-s \
-c="$config_filepath_pytest" \
--cov=./ \
--cov-report="xml:$output_filepath" \
--cov-config="$config_filepath_coverage"
