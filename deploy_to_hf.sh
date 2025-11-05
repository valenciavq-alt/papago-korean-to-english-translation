#!/bin/bash
# Automated script to prepare and upload to Hugging Face Spaces
# This script will help you deploy your Papago Translation app

set -e

echo "🚀 Hugging Face Space Deployment Helper"
echo "========================================"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "📝 Please provide the following information:"
echo ""
read -p "Your Hugging Face username: " HF_USERNAME
read -p "Your Space name (e.g., papago-korean-translation): " SPACE_NAME

SPACE_URL="https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME"
REPO_URL="https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME"

echo ""
echo "📋 Instructions:"
echo "   1. First, create the Space at: https://huggingface.co/new-space"
echo "   2. Set SDK to: Gradio"
echo "   3. Set name to: $SPACE_NAME"
echo "   4. Set hardware to: CPU Basic (free)"
echo ""
read -p "Press Enter after you've created the Space..."

echo ""
echo "📦 Preparing files..."

# Clone the repository
echo "   Cloning Space repository..."
if [ -d "$SPACE_NAME" ]; then
    echo "   Directory exists, removing old clone..."
    rm -rf "$SPACE_NAME"
fi

git clone "$REPO_URL" "$SPACE_NAME" || {
    echo "❌ Failed to clone repository."
    echo "   Make sure:"
    echo "   1. The Space exists: $SPACE_URL"
    echo "   2. You're logged in: huggingface-cli login"
    echo "   3. You have write access to the Space"
    exit 1
}

cd "$SPACE_NAME"

# Copy files
echo "   Copying files..."
cp "../app.py" .
cp "../papago_translation.py" .
cp "../requirements_hf.txt" requirements.txt
cp "../README_HF.md" README.md

# Show what will be committed
echo ""
echo "📋 Files ready to commit:"
git status --short

echo ""
read -p "Ready to commit and push? (y/n): " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    echo ""
    echo "💾 Committing changes..."
    git add .
    git commit -m "Initial commit: Papago Korean Translation" || {
        echo "⚠️  Nothing to commit (files may already be committed)"
    }
    
    echo "📤 Pushing to Hugging Face..."
    git push || {
        echo "❌ Push failed. You may need to:"
        echo "   1. Login: huggingface-cli login"
        echo "   2. Check your permissions"
        exit 1
    }
    
    echo ""
    echo "✅ Success! Your Space is being built."
    echo "   Check it at: $SPACE_URL"
    echo "   Build logs: $SPACE_URL/logs"
else
    echo "❌ Cancelled. Files are ready in: $(pwd)"
    echo "   You can commit manually when ready."
fi

cd ..


