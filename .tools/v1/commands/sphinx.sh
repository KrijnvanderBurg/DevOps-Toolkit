#!/bin/bash

# Default values
docs_dirpath="${1:-$PWD/docs}"  # Default to ./docs/ if not specified

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --docs_dirpath=*) docs_dirpath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pipx install sphinx --quiet
pip install sphinx-autoapi sphinx-rtd-theme --quiet

# Running semgrep scan
echo "Set CWD to: $docs_dirpath"
cd $docs_dirpath

make html
