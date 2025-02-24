#!/bin/bash

# Default values
tests_path="${1:-$PWD/tests/}"  # Default to tests/unit if not specified
coverage_path="${2:-$PWD/src/}"  # Default to current directory if not specified
config_filepath_pytest="${3:-$PWD/../.tools/v1/configs/pytest.ini}"  # Default config file path if not specified
config_filepath_coverage="${4:-$PWD/../.tools/v1/configs/.coveragerc}"  # Default config file path if not specified
output_coverage_filepath="${5:-$PWD/coverage.xml}"  # Default coverage output file
output_junit_filepath="${6:-$PWD/JUNIT-TEST.xml}"  # Default coverage output file

# Parse named parameters using a for loop
for i in "$@"; do
  case $i in
    --tests_path=*) tests_path="${i#*=}" ;;
    --coverage_path=*) coverage_path="${i#*=}" ;;
    --config_filepath_pytest=*) config_filepath_pytest="${i#*=}" ;;
    --config_filepath_coverage=*) config_filepath_coverage="${i#*=}" ;;
    --output_coverage_filepath=*) output_coverage_filepath="${i#*=}" ;;
    --output_junit_filepath=*) output_junit_filepath="${i#*=}" ;;
    *) echo "Unknown option: $i" ;;  # Handle invalid arguments
  esac
done

pip install pytest --quiet
pip install pytest-cov pytest-xdist --quiet

# Running pytest scan
echo "Tests path: $tests_path"
echo "Coverage path: $coverage_path"
echo "Config file pytest: $config_filepath_pytest"
echo "Config file coverage: $config_filepath_coverage"
echo "Coverage output will be saved to: $output_coverage_filepath"
echo "Pytest junit output will be saved to: $output_junit_filepath"

# -s // disables print/log statements in output
pytest "$tests_path" \
-c="$config_filepath_pytest" \
-o "cache_dir=$PWD/.pytest_cache" \
--cov="$coverage_path" \
--cov-report="xml:$output_coverage_filepath" \
--cov-config="$config_filepath_coverage" \
--junit-xml="$output_junit_filepath"
# --verbose
