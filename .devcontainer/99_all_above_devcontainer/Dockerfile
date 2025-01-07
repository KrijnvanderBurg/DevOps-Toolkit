ARG VARIANT
FROM mcr.microsoft.com/devcontainers/base:${VARIANT} AS base

RUN ZSH_SNIPPET="export HISTFILE=/commandhistory/.zsh_history && export HISTSIZE=10000 && export SAVEHIST=10000" \
    && mkdir /commandhistory \
    && touch /commandhistory/.zsh_history \
    && chown -R ${USER}:${USER} /commandhistory \
    && echo "$ZSH_SNIPPET" >> "/home/${USER}/.zshrc"
