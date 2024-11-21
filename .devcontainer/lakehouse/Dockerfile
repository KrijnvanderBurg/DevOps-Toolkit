ARG UBUNTU_VARIANT
FROM mcr.microsoft.com/devcontainers/base:ubuntu-${UBUNTU_VARIANT} AS base

# Install Terraform CLI
RUN apt-get update && apt-get install -y gnupg software-properties-common \
    && wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    && gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint \
    && echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list \
    && apt-get update \
    && apt-get install -y terraform

# Install CDK for Terraform
# RUN npm install --global cdktf-cli@latest --verbose && npm install -g cdktf-cli 
