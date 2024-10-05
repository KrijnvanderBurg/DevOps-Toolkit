ARG UBUNTU_VARIANT
FROM mcr.microsoft.com/devcontainers/base:ubuntu-${UBUNTU_VARIANT} AS base

# Required for TruffleHog VsCode task
RUN curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
