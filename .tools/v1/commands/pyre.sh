#!/bin/bash

# Pyre is hardcoded to read config from the working directory
# So we copy the .pyre_configuration file to the target directory
# and remove it after the scan is complete

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
config_filepath="${2:-$PWD/../.tools/v1/configs/.pyre_configuration}"  # Default config file path if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    --config_filepath=*) config_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pip install pyre-check --quiet

# Copy the config file to the root of the project
cp "$config_filepath" "$target_path/.pyre_configuration"

# Print the current pyre version
echo "pyre version:"
pyre --version

# Scanning the target folder with pyre
echo "Scanning folder: $target_path"

pyre --source-directory "$target_path" \
  --log-level INFO \
  --noninteractive \
  --sequential check
exit_code=$?

# Remove the config file from the root of the project
rm "$target_path/.pyre_configuration"

exit $exit_code
