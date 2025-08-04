# 🚀 Guia Completo - Upload para GitHub

## 📋 Pré-requisitos

1. **Conta no GitHub**: [github.com](https://github.com)
2. **Git instalado**: [git-scm.com/download/win](https://git-scm.com/download/win)
3. **Projeto organizado** ✅ (já está pronto!)

## 🔧 Passo a Passo

### 1. **Criar Repositório no GitHub**

1. Acesse [github.com](https://github.com) e faça login
2. Clique no botão **"New"** ou **"+"** → **"New repository"**
3. Configure:
   - **Repository name**: `decifrador`
   - **Description**: `AES-CBC Decryptor - Ferramenta Python profissional`
   - **Visibility**: Public (recomendado)
   - **NÃO** marque "Add a README file"
   - **NÃO** marque "Add .gitignore"
   - Clique em **"Create repository"**

### 2. **Preparar Repositório Local**

Execute o script automático:
```bash
.\upload_to_github.bat
```

Ou manualmente:
```bash
# Inicializar Git
git init

# Adicionar todos os arquivos
git add .

# Fazer primeiro commit
git commit -m "Projeto decifrador AES-CBC profissional - v1.0.0"
```

### 3. **Conectar ao GitHub**

Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub:

```bash
# Renomear branch para main
git branch -M main

# Adicionar repositório remoto
git remote add origin https://github.com/SEU_USUARIO/decifrador.git

# Fazer push inicial
git push -u origin main
```

### 4. **Verificar Upload**

1. Acesse seu repositório no GitHub
2. Verifique se todos os arquivos estão lá
3. O README.md deve aparecer na página principal

## 📁 Estrutura do Projeto no GitHub

```
decifrador/
├── 📄 README.md                    # Documentação principal
├── 🔧 aes_decrypt.py              # Programa principal
├── 📦 requirements.txt             # Dependências
├── ⚙️ setup.py                    # Configuração PyPI
├── 📋 pyproject.toml              # Configuração moderna
├── 📄 LICENSE                      # Licença MIT
├── 🚫 .gitignore                  # Arquivos ignorados
├── 🔧 install.bat                 # Instalador Windows
├── ▶️ run.bat                     # Executor Windows
├── 🚀 upload_to_github.bat        # Script de upload
├── 🔐 decifrador.ico              # Ícone do projeto
├── 📁 .github/                    # Configurações GitHub
│   ├── workflows/                 # CI/CD
│   ├── ISSUE_TEMPLATE/           # Templates issues
│   └── dependabot.yml            # Atualizações automáticas
├── 📁 .vscode/                   # Configurações VS Code
└── 📁 docs/                      # Documentação adicional
```

## 🎯 Próximos Passos (Opcionais)

### Configurar GitHub Pages
1. Vá em **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: main
4. **Folder**: /docs
5. Clique **Save**

### Configurar GitHub Actions
- O workflow já está configurado em `.github/workflows/`
- Será executado automaticamente em cada push

### Publicar no PyPI (Futuro)
```bash
# Instalar build tools
pip install build twine

# Construir distribuição
python -m build

# Publicar (requer conta PyPI)
twine upload dist/*
```

## 🔗 Links Úteis

- **GitHub**: [github.com](https://github.com)
- **Git Download**: [git-scm.com/download/win](https://git-scm.com/download/win)
- **GitHub Pages**: [pages.github.com](https://pages.github.com)
- **PyPI**: [pypi.org](https://pypi.org)

## ❓ Problemas Comuns

### Erro: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/SEU_USUARIO/decifrador.git
```

### Erro: "Authentication failed"
1. Use GitHub CLI: `gh auth login`
2. Ou configure credenciais: `git config --global user.name "Seu Nome"`

### Erro: "Permission denied"
- Verifique se você tem permissão no repositório
- Use HTTPS ou configure SSH keys

## 🎉 Sucesso!

Após o upload, seu projeto estará disponível em:
`https://github.com/SEU_USUARIO/decifrador`

Com todas as funcionalidades profissionais configuradas! 🚀 