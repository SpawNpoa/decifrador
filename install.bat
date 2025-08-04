@echo off
setlocal
set PYTHON_CMD=python
where python >nul 2>&1
if errorlevel 1 (
    if exist "%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe" (
        set PYTHON_CMD=%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe
        echo ⚠️ Python não estava no PATH, usando instalacao padrao do Windows.
    ) else (
        echo ❌ Python nao encontrado. Instale o Python 3.7+ primeiro.
        pause
        exit /b 1
    )
)
echo ✅ Python encontrado!

echo.
echo [2/4] Criando ambiente virtual...
%PYTHON_CMD% -m venv .venv
if errorlevel 1 (
    echo ❌ Erro ao criar ambiente virtual.
    pause
    exit /b 1
)
echo ✅ Ambiente virtual criado!

echo.
echo [3/4] Ativando ambiente virtual...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Erro ao ativar ambiente virtual.
    pause
    exit /b 1
)
echo ✅ Ambiente virtual ativado!

echo.
echo [4/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Erro ao instalar dependencias.
    pause
    exit /b 1
)
echo ✅ Dependencias instaladas!

echo.
echo ========================================
echo    Instalacao concluida com sucesso!
echo ========================================
echo.
echo Para executar o programa:
echo   .venv\Scripts\python.exe aes_decrypt.py
echo.
pause
endlocal 