@echo off
REM ComplyAI - Simple Local Launch Script

echo.
echo ========================================
echo  ComplyAI - Starting Services
echo ========================================
echo.

REM Check if Docker is running
docker ps >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not running. Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo [1/4] Building and starting Docker containers...
docker-compose up -d

if errorlevel 1 (
    echo ERROR: Docker Compose failed. Check your setup.
    pause
    exit /b 1
)

timeout /t 3 /nobreak

echo [2/4] Backend starting on http://localhost:8000
echo [3/4] API docs available at http://localhost:8000/docs
echo [4/4] Frontend starting on http://localhost:3000
echo.
echo ========================================
echo  Services started successfully!
echo ========================================
echo.
echo To stop services, run: docker-compose down
echo.
pause
