@echo off
title Configuracion de YtApp

echo Comprobando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python no esta instalado.
    pause
    exit /b
)

echo.

echo Comprobando yt-dlp...
python -m yt_dlp --version >nul 2>&1
if errorlevel 1 (
    echo Instalando yt-dlp...
    python -m pip install --upgrade yt-dlp
) else (
    echo yt-dlp ya esta instalado.
)

echo.

echo Comprobando FFmpeg...
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo Instalando FFmpeg...
    winget install -e --id Gyan.FFmpeg
) else (
    echo FFmpeg ya esta instalado.
)

echo.
echo Todo listo.
echo Si acabas de instalar FFmpeg, reinicia VS Code.
pause