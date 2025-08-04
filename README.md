# 🔐 AES-CBC Decryptor

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/badge/PyPI-pycryptodome-blue.svg)](https://pypi.org/project/pycryptodome/)

Uma ferramenta Python profissional para decifrar texto usando o algoritmo AES em modo CBC (Cipher Block Chaining).

## ✨ Características

- 🔓 Decifração AES-CBC com suporte completo
- 🎯 Conversão automática hexadecimal para bytes
- 🛡️ Tratamento robusto de erros
- 📝 Saída em UTF-8
- 💾 Salvamento automático de resultados
- 🚀 Interface de linha de comando simples
- 📦 Instalação fácil via pip

## 📋 Exemplo de Uso

### Dados de Exemplo

- **Chave AES**: `240B31B44A27BEC5062B3A74C63271A4`
- **Texto Cifrado**: `EF794476D605765572683CE849FBD4555CE8EC1382019662E277F31B8035E285787C1DA9D2CC5B3441F5CB900C41BA70902A932209C3966B83FB4387ABBC95E0`
- **Vetor de Inicialização (IV)**: `C4AB0DF3D808D72AAADBC68206483B18`
- **Modo de Operação**: CBC

### Resultado Esperado

```
Texto claro: "CBC precisa utilizar algum modo de preenchimento."
```

## 🚀 Instalação

### Método 1: Instalação Direta

```bash
# Clone o repositório
git clone https://github.com/yourusername/aes-cbc-decryptor.git
cd aes-cbc-decryptor

# Instale as dependências
pip install -r requirements.txt
```

### Método 2: Instalação via pip (futuro)

```bash
pip install aes-cbc-decryptor
```

## 💻 Uso

### Execução Básica

```bash
python aes_decrypt.py
```

### Execução com Python Launcher (Windows)

```bash
py aes_decrypt.py
```

### O que o programa faz:

1. 🔓 Decifra o texto usando AES-CBC
2. 📺 Exibe o texto claro no terminal
3. 💾 Salva o resultado em `decrypted_text.txt`
4. 📊 Mostra estatísticas do processo

## 🛠️ Funcionalidades

- 🔄 Conversão automática de hexadecimal para bytes
- 🔓 Decifração AES-CBC com padding automático
- 🛡️ Tratamento robusto de erros
- 🌐 Saída em UTF-8
- 💾 Salvamento automático do resultado em arquivo
- 📊 Estatísticas detalhadas do processo

## 📚 Bibliotecas Utilizadas

- **`pycryptodome`**: Biblioteca criptográfica para operações AES
- **`binascii`**: Módulo padrão Python para conversão hexadecimal

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Seu Nome** - [@seutwitter](https://twitter.com/seutwitter)

## 🙏 Agradecimentos

- [PyCryptodome](https://pycryptodome.readthedocs.io/) pela excelente biblioteca criptográfica
- Comunidade Python por manter as melhores práticas 