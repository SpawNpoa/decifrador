@echo off
set PYTHON_CMD=C:\Users\SpawN\AppData\Local\Programs\Python\Python311\python.exe

if not exist "%PYTHON_CMD%" (
    echo Python nao encontrado.
    pause
    exit /b 1
)

"%PYTHON_CMD%" aes_decrypt.py
pause 