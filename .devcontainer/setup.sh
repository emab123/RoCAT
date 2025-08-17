#!/bin/bash
set -e

echo "🚀 Starting RoCAT setup..."

echo "🔧 Installing system dependencies..."
sudo apt-get update
sudo apt-get install -y gfortran build-essential

echo "📦 Installing Python dependencies globally in container..."
pip install --upgrade pip

if [ -f requirements.txt ]; then
    echo "📚 Installing from requirements.txt..."
    pip install -r requirements.txt
    echo "✅ Requirements installed successfully!"
else
    echo "⚠️  requirements.txt not found - skipping Python dependencies"
fi

echo "✅ RoCAT development environment setup complete!"
echo "🎯 You can now start developing with all dependencies installed"