ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim-bullseye AS BASE

ENV \
    # Java
    JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/ \
    # Poetry
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.7.1

RUN apt-get update && \
    apt-get install -y \
    curl \
    git \
    openjdk-11-jdk && \
    apt-get clean

RUN pip install poetry

WORKDIR /repo

COPY . .