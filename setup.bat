@echo off
REM Personal Website Setup Script for Windows
REM Automates the initial setup process

echo 🚀 Setting up your personal website...
echo.

REM Check Python
echo 1️⃣  Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3 is not installed. Please install Python 3.9 or higher.
    exit /b 1
)
echo ✅ Python found
echo.

REM Create virtual environment
echo 2️⃣  Creating virtual environment...
if exist "venv" (
    echo ⚠️  Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo ✅ Virtual environment created
)
echo.

REM Activate virtual environment
echo 3️⃣  Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Install dependencies
echo 4️⃣  Installing dependencies...
python -m pip install --upgrade pip >nul
pip install -r requirements.txt
echo ✅ Dependencies installed
echo.

REM Check content file
echo 5️⃣  Checking content file...
if exist "content\data.yaml" (
    echo ✅ Content file exists
) else (
    echo ❌ content\data.yaml not found
    exit /b 1
)
echo.

REM Run tests
echo 6️⃣  Running tests...
pytest -v
echo.

REM Final instructions
echo 🎉 Setup complete!
echo.
echo 📝 Next steps:
echo    1. Edit content\data.yaml with your information
echo    2. Replace static\images\profile.jpg with your photo
echo    3. Run the development server:
echo.
echo       python app.py
echo.
echo    4. Open http://localhost:5000 in your browser
echo.
echo 📚 For more info, see README.md or QUICKSTART.md
echo.
pause
