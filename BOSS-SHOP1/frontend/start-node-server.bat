@echo off
echo ========================================
echo Starting BOSS SHOPP Node.js Server
echo ========================================
echo Make sure you have Node.js installed
echo ========================================

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if required packages are installed
if not exist node_modules (
    echo Installing required Node.js packages...
    npm install express sqlite3 cors bcryptjs jsonwebtoken
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install required packages
        pause
        exit /b 1
    )
)

echo Starting Node.js server on port 3000...
node server.js

pause