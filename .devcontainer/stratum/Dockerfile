ARG VARIANT
FROM mcr.microsoft.com/devcontainers/${VARIANT} AS base

# install terraform
RUN apt-get update && \
        apt-get install -y gnupg software-properties-common wget && \
        wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
        gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint && \
        echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list && \
        apt-get update && \
        apt-get install -y terraform && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*
