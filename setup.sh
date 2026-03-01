#!/bin/bash

# Personal Website Setup Script
# Automates the initial setup process

set -e  # Exit on error

echo "🚀 Setting up your personal website..."
echo ""

# Check Python version
echo "1️⃣  Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Create virtual environment
echo "2️⃣  Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi
echo ""

# Activate virtual environment
echo "3️⃣  Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"
echo ""

# Install dependencies
echo "4️⃣  Installing dependencies..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Check if content file exists
echo "5️⃣  Checking content file..."
if [ -f "content/data.yaml" ]; then
    echo "✅ Content file exists"
else
    echo "❌ content/data.yaml not found"
    exit 1
fi
echo ""

# Run tests
echo "6️⃣  Running tests..."
pytest -v
echo ""

# Final instructions
echo "🎉 Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Edit content/data.yaml with your information"
echo "   2. Replace static/images/profile.jpg with your photo"
echo "   3. Run the development server:"
echo ""
echo "      python app.py"
echo ""
echo "   4. Open http://localhost:5000 in your browser"
echo ""
echo "📚 For more info, see README.md or QUICKSTART.md"
echo ""
