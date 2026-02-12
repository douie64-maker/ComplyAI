@echo off
REM Stop all ComplyAI services

echo Stopping ComplyAI services...
docker-compose down

echo.
echo All services stopped.
pause
