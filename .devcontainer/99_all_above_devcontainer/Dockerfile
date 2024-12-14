ARG UBUNTU_VARIANT
FROM mcr.microsoft.com/devcontainers/base:ubuntu-${UBUNTU_VARIANT} AS base

RUN BASH_SNIPPET="export HISTFILE=/commandhistory/.bash_history && export HISTSIZE=10000 && export SAVEHIST=10000" \
    && ZSH_SNIPPET="export HISTFILE=/commandhistory/.zsh_history && export HISTSIZE=10000 && export SAVEHIST=10000" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && touch /commandhistory/.zsh_history \
    && chown -R ${USER}:${USER} /commandhistory \
    # Add history settings to both .bashrc and .zshrc
    && echo "$BASH_SNIPPET" >> "/home/${USER}/.bashrc" \
    && echo "$ZSH_SNIPPET" >> "/home/${USER}/.zshrc"
