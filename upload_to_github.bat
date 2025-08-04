@echo off
echo ========================================
echo    UPLOAD PARA GITHUB - DECIFRADOR
echo ========================================
echo.

echo [1/4] Verificando se Git esta instalado...
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git nao encontrado. Instale o Git primeiro:
    echo    https://git-scm.com/download/win
    pause
    exit /b 1
)
echo ✅ Git encontrado!

echo.
echo [2/4] Inicializando repositorio Git...
git init
if errorlevel 1 (
    echo ❌ Erro ao inicializar Git.
    pause
    exit /b 1
)
echo ✅ Repositorio Git inicializado!

echo.
echo [3/4] Adicionando arquivos...
git add .
if errorlevel 1 (
    echo ❌ Erro ao adicionar arquivos.
    pause
    exit /b 1
)
echo ✅ Arquivos adicionados!

echo.
echo [4/4] Fazendo primeiro commit...
git commit -m "Projeto decifrador AES-CBC profissional - v1.0.0"
if errorlevel 1 (
    echo ❌ Erro ao fazer commit.
    pause
    exit /b 1
)
echo ✅ Commit realizado!

echo.
echo ========================================
echo    REPOSITORIO LOCAL CRIADO!
echo ========================================
echo.
echo 📝 PROXIMOS PASSOS:
echo    1. Crie um repositorio no GitHub
echo    2. Execute os comandos abaixo:
echo.
echo    git branch -M main
echo    git remote add origin https://github.com/SEU_USUARIO/decifrador.git
echo    git push -u origin main
echo.
echo 💡 Substitua 'SEU_USUARIO' pelo seu nome de usuario do GitHub
echo.
pause 