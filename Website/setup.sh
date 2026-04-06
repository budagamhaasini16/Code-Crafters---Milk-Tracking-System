#!/bin/bash

# Milk Tracking System - Quick Setup Script
# This script sets up the development environment

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  Milk Tracking System - Development Environment Setup        ║"
echo "║  Gujarat Dairy Cooperative Solution                          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check for required tools
check_requirement() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}✓${NC} $2 found"
        return 0
    else
        echo -e "${RED}✗${NC} $2 not found. Install it first."
        return 1
    fi
}

echo -e "${BLUE}Checking requirements...${NC}"
requirements_met=true

check_requirement "git" "Git" || requirements_met=false
check_requirement "python3" "Python 3" || requirements_met=false
check_requirement "node" "Node.js" || requirements_met=false
check_requirement "npm" "npm" || requirements_met=false

if [ "$requirements_met" = false ]; then
    echo -e "${RED}Please install missing requirements.${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}Setting up Backend...${NC}"

# Backend setup
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo -e "${YELLOW}⚠ Please update backend/.env with your configuration${NC}"
else
    echo ".env file already exists"
fi

echo -e "${GREEN}✓ Backend setup complete${NC}"

echo ""
echo -e "${BLUE}Setting up Frontend...${NC}"

# Frontend setup
cd ../frontend

# Install dependencies
echo "Installing npm dependencies..."
npm install

# Create .env file if doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo -e "${YELLOW}⚠ Please update frontend/.env if needed${NC}"
else
    echo ".env file already exists"
fi

echo -e "${GREEN}✓ Frontend setup complete${NC}"

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  Setup Complete! Ready to start development                  ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Start MongoDB:"
echo "   - Windows: mongod.exe"
echo "   - macOS: brew services start mongodb-community"
echo "   - Linux: sudo systemctl start mongod"
echo ""
echo "2. Start Backend (Terminal 1):"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   python run.py"
echo ""
echo "3. Start Frontend (Terminal 2):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "4. Open your browser: http://localhost:5173"
echo ""
echo -e "${YELLOW}Documentation:${NC}"
echo "  - Setup Guide: docs/SETUP_GUIDE.md"
echo "  - API Docs: docs/API_DOCUMENTATION.md"
echo "  - Problem Understanding: docs/PROBLEM_UNDERSTANDING.md"
echo ""
