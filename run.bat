@echo off
echo ========================================
echo    AES-CBC Decryptor - Executor Interativo
echo ========================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ❌ Ambiente virtual nao encontrado.
    echo Execute install.bat primeiro.
    pause
    exit /b 1
)

echo ✅ Executando decifrador AES-CBC interativo...
echo.
echo 💡 DICAS:
echo    - Digite 'exemplo' para usar dados de teste
echo    - Digite 'sair' para encerrar o programa
echo    - Cada decifração será salva em arquivo separado
echo.

.venv\Scripts\python.exe aes_decrypt.py

echo.
echo ========================================
echo    Programa encerrado!
echo ========================================
echo.
pause 