#!/bin/bash

# Default values
output_path="${1:-$PWD}"  # Default to current directory if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --output_path=*) output_path="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

npm install --silent --global cdktf-cli@0.20

echo "cdktf version:"
cdktf --version

echo "output folder: $output_path"

cdktf synth \
  --output "$output_path"
