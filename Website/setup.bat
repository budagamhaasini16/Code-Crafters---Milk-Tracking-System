@echo off
REM Milk Tracking System - Quick Setup Script for Windows

color 0A
echo.
echo ═══════════════════════════════════════════════════════════════════
echo   Milk Tracking System - Development Environment Setup (Windows)
echo   Gujarat Dairy Cooperative Solution
echo ═══════════════════════════════════════════════════════════════════
echo.

REM Check for required tools
echo Checking requirements...

where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.9+
    pause
    exit /b 1
)
echo [OK] Python found

where node >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Node.js not found. Please install Node.js 16+
    pause
    exit /b 1
)
echo [OK] Node.js found

where npm >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] npm not found. Please install npm
    pause
    exit /b 1
)
echo [OK] npm found

echo.
echo Setting up Backend...
cd backend

REM Create virtual environment
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing Python dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Create .env file if doesn't exist
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo [WARNING] Please update backend\.env with your configuration
) else (
    echo .env file already exists
)

echo [OK] Backend setup complete

echo.
echo Setting up Frontend...
cd ..\frontend

REM Install dependencies
echo Installing npm dependencies...
call npm install

REM Create .env file if doesn't exist
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo [WARNING] Please update frontend\.env if needed
) else (
    echo .env file already exists
)

echo [OK] Frontend setup complete

echo.
echo ═══════════════════════════════════════════════════════════════════
echo   Setup Complete! Ready to start development
echo ═══════════════════════════════════════════════════════════════════
echo.
echo Next steps:
echo.
echo 1. Start MongoDB:
echo    - Install: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
echo    - Run: mongod.exe
echo.
echo 2. Start Backend (Command Prompt 1):
echo    cd backend
echo    venv\Scripts\activate.bat
echo    python run.py
echo.
echo 3. Start Frontend (Command Prompt 2):
echo    cd frontend
echo    npm run dev
echo.
echo 4. Open your browser: http://localhost:5173
echo.
echo Documentation:
echo   - Setup Guide: docs\SETUP_GUIDE.md
echo   - API Docs: docs\API_DOCUMENTATION.md
echo   - Problem Understanding: docs\PROBLEM_UNDERSTANDING.md
echo.
pause
