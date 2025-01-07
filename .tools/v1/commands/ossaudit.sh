#!/bin/bash

# Default values
temp_dirpath="${1:-$PWD}/temp"
config_filepath="${2:-$PWD/../.tools/v1/configs/ossaudit.yaml}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --temp_dirpath=*) temp_dirpath="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pip install poetry --quiet
poetry self add poetry-plugin-export

# https://github.com/python-poetry/poetry-plugin-export
poetry export --format requirements.txt \
  --all-extras \
  --all-groups \
  --without-hashes \
  | tee "$temp_dirpath/requirements.txt"

pip install ossaudit --quiet

# Print the current ossaudit version
echo "ossaudit has no option to print version."

# Scanning the target folder with ossaudit
echo "Config filepath: $config_filepath"
echo "Temp dirpath: $temp_dirpath"

ossaudit -f "$temp_dirpath/requirements.txt" \
  --config "$config_filepath"
