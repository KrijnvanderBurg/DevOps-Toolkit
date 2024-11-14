ARG ALPINE_VERSION
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04 AS BASE

# ENV \
#     # Java
#     JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/ \

# RUN apt-get update && \
#     apt-get install -y \
#     curl \
#     git \
#     openjdk-17-jdk && \
#     apt-get clean

RUN curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin

# USER vscode
# WORKDIR /workspace