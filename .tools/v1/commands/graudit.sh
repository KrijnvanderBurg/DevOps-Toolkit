#!/bin/bash

# Default values
target_path="${1:-$PWD}"  # Default to current directory if not specified
# graudit has no config file

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --target_path=*) target_path="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

git clone https://github.com/wireghoul/graudit $HOME/.graudit/
echo "export PATH=$PATH:$HOME/.graudit" >> ~/.profile
source ~/.profile

# Print the current version
echo "graudit version:"
graudit -v

# Scanning the target folder with flake8
echo "Scanning folder: $target_path"

graudit -d python -A "$target_path"
