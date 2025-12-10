#!/bin/bash
# Agent-Toga Quick Install Script
# Ehehe~ ♡ Let's get you set up with Agent-Toga!

set -e

echo "============================================================"
echo "  Agent-Toga Installation"
echo "  Himiko Toga AI Personality System"
echo "============================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $python_version"
echo ""

# Determine installation type
if [ "$1" == "dev" ]; then
    echo "Installing in DEVELOPMENT mode..."
    echo "This includes testing, linting, and documentation tools."
    echo ""
    pip install -e ".[dev]"
    pip install -r requirements-dev.txt
    echo ""
    echo "✓ Development installation complete!"
    echo ""
    echo "Available commands:"
    echo "  make help          - Show all available commands"
    echo "  make test          - Run tests"
    echo "  make format        - Format code"
    echo "  make lint          - Run linter"
    echo "  make demo          - Run demo"
else
    echo "Installing in STANDARD mode..."
    echo "For development mode, run: ./install.sh dev"
    echo ""
    pip install -e .
    echo ""
    echo "✓ Installation complete!"
    echo ""
    echo "Try it out:"
    echo "  python examples/demo_toga.py"
    echo "  python examples/test_toga.py"
fi

echo ""
echo "============================================================"
echo "  Ehehe~ ♡ Installation successful!"
echo "  Ready to break some systems... ethically! ♡"
echo "============================================================"
