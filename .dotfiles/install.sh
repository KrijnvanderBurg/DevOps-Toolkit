#!/bin/bash

# Stop on error
set -e

# Dotfiles directory path
DOTFILES_DIR="$(pwd)/../.dotfiles"

# Ensure the dotfiles directory exists
if [ ! -d "$DOTFILES_DIR" ]; then
  echo "Dotfiles directory not found at $DOTFILES_DIR. Please ensure it's in the correct location."
  exit 1
fi

# Copy the dotfiles from the repo to the home directory
echo "Copying dotfiles..."
rm -f ~/.zshrc
cp -f "$DOTFILES_DIR/.zshrc" "$HOME/.zshrc"

# # Install Oh My Zsh
echo "Installing Oh My Zsh..."
# # Install Oh My Zsh (already installed in devcontainer)
# Note, devcontainers handles zsh really weird. 
# If you want to make changes to the process, debug your steps properly and verify .zshrc contents.
# If you get errors like `command not found: ^M`, you have windows line endings in .zshrc file.
# if [ ! -d "$HOME/.oh-my-zsh" ]; then
#   echo "Installing Oh My Zsh..."
#   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# fi

echo "Dotfiles setup complete!"
