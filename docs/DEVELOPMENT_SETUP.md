# Development Environment Setup

This document outlines the steps to set up the development environment for both iOS and Android platforms.

## Prerequisites

- **macOS:** Xcode Command Line Tools, Homebrew
- **Windows (WSL):** Ubuntu installed with WSL2

## Steps

1. **Install Xcode Command Line Tools (macOS):**
   ```bash
   xcode-select --install
   ```

2. **Install Homebrew (macOS):**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Android SDK:**
   - **macOS:**
     ```bash
     brew install --cask android-sdk
     ```
   - **Windows (WSL):**
     ```bash
     sudo apt-get update && sudo apt-get install -y android-sdk
     ```

4. **Configure Environment Variables:**
   Add the following to your `.bashrc` or `.zshrc`:
   ```bash
   export ANDROID_HOME="$HOME/Library/Android/sdk"
   export PATH="$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools"
   ```

5. **Verification:**
   - **Android SDK version:**
     ```bash
     sdkmanager --version
     ```
   - **iOS SDK version:**
     ```bash
     xcodebuild -version
     ```

## Troubleshooting
- **Common issues with SDK installations**
- **Network issues during downloads**

Ensure all steps are followed as per your operating system. Reach out to the team for help if you encounter issues not covered in this guide.