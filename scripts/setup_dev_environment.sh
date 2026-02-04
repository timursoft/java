#!/bin/bash

set -e

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Xcode command line tools for macOS
echo "Checking Xcode Command Line Tools..."
if ! command_exists xcode-select; then
    echo "Error: Xcode Command Line Tools not found. Please install them first."
    exit 1
fi

# Check and install Homebrew if not installed (macOS)
echo "Checking Homebrew..."
if ! command_exists brew; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Android SDK (macOS & WSL)
echo "Checking Android SDK..."
if ! command_exists sdkmanager; then
    if [ "$(uname)" == "Darwin" ]; then
        echo "Installing Android SDK via Homebrew..."
        brew install --cask android-sdk
    else
        echo "Installing Android SDK on WSL..."
        sudo apt-get update && sudo apt-get install -y android-sdk
    fi
fi

# Specify SDK versions in environment_config.yml
ANDROID_SDK_VERSION="30.0.3"
IOS_SDK_VERSION="14.5"

# Verify installation
echo "Verifying installations..."
echo "Android SDK version: $(sdkmanager --version)"
echo "iOS SDK version: $(xcodebuild -version)"

# Export necessary paths to environment variables
export ANDROID_HOME="$HOME/Library/Android/sdk"
export PATH="$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools"

echo "Development environment setup complete."