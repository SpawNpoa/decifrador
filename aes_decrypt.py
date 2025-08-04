#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AES-CBC Decryptor
Decifrador de texto usando algoritmo AES em modo CBC (Cipher Block Chaining)

Author: Lucas Spawn
Version: 1.0.0
License: MIT
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

def hex_to_bytes(hex_string):
    """Converte string hexadecimal para bytes"""
    return binascii.unhexlify(hex_string)

def decrypt_aes_cbc(key_hex, ciphertext_hex, iv_hex):
    """
    Decifra texto usando AES-CBC
    
    Args:
        key_hex (str): Chave AES em hexadecimal
        ciphertext_hex (str): Texto cifrado em hexadecimal
        iv_hex (str): Vetor de inicialização em hexadecimal
    
    Returns:
        str: Texto claro em UTF-8
    """
    try:
        # Converter hex para bytes
        key = hex_to_bytes(key_hex)
        ciphertext = hex_to_bytes(ciphertext_hex)
        iv = hex_to_bytes(iv_hex)
        
        # Criar objeto de decifração AES-CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decifrar o texto
        decrypted_padded = cipher.decrypt(ciphertext)
        
        # Remover padding
        decrypted = unpad(decrypted_padded, AES.block_size)
        
        # Converter para UTF-8
        plaintext = decrypted.decode('utf-8')
        
        return plaintext
        
    except Exception as e:
        return f"Erro na decifração: {str(e)}"

def main():
    """Função principal"""
    print("🔐 === DECIFRADOR AES-CBC INTERATIVO === 🔐")
    print("Digite 'sair' para encerrar o programa")
    print("Digite 'exemplo' para usar os dados de exemplo")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 60)
        print("📝 INSIRA OS DADOS PARA DECIFRAÇÃO:")
        print("=" * 60)
        
        # Obter dados do usuário
        key_hex = input("🔑 Chave AES (hex): ").strip()
        
        if key_hex.lower() == 'sair':
            print("\n👋 Programa encerrado. Até logo!")
            break
        elif key_hex.lower() == 'exemplo':
            key_hex = "240B31B44A27BEC5062B3A74C63271A4"
            ciphertext_hex = "EF794476D605765572683CE849FBD4555CE8EC1382019662E277F31B8035E285787C1DA9D2CC5B3441F5CB900C41BA70902A932209C3966B83FB4387ABBC95E0"
            iv_hex = "C4AB0DF3D808D72AAADBC68206483B18"
            print(f"✅ Usando dados de exemplo:")
            print(f"   Chave: {key_hex}")
            print(f"   IV: {iv_hex}")
            print(f"   Texto cifrado: {ciphertext_hex[:32]}...")
        else:
            ciphertext_hex = input("🔒 Texto cifrado (hex): ").strip()
            if ciphertext_hex.lower() == 'sair':
                print("\n👋 Programa encerrado. Até logo!")
                break
            
            iv_hex = input("🔐 Vetor de inicialização (IV) (hex): ").strip()
            if iv_hex.lower() == 'sair':
                print("\n👋 Programa encerrado. Até logo!")
                break
        
        print("\n" + "=" * 60)
        print("🔄 PROCESSANDO...")
        print("=" * 60)
        
        # Validar entradas
        if not all([key_hex, ciphertext_hex, iv_hex]):
            print("❌ Erro: Todos os campos são obrigatórios!")
            continue
        
        # Verificar se são hex válidos
        try:
            int(key_hex, 16)
            int(ciphertext_hex, 16)
            int(iv_hex, 16)
        except ValueError:
            print("❌ Erro: Dados devem estar em formato hexadecimal válido!")
            continue
        
        # Decifrar o texto
        plaintext = decrypt_aes_cbc(key_hex, ciphertext_hex, iv_hex)
        
        if plaintext.startswith("Erro na decifração"):
            print(f"\n❌ {plaintext}")
        else:
            print(f"\n✅ DECIFRAÇÃO CONCLUÍDA!")
            print(f"📄 Texto claro: '{plaintext}'")
            print(f"📊 Tamanho: {len(plaintext)} caracteres")
            
            # Salvar resultado em arquivo com timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'decrypted_text_{timestamp}.txt'
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                    f.write(f"Chave: {key_hex}\n")
                    f.write(f"IV: {iv_hex}\n")
                    f.write(f"Texto cifrado: {ciphertext_hex}\n")
                    f.write(f"Texto claro: {plaintext}\n")
                print(f"💾 Resultado salvo em '{filename}'")
            except Exception as e:
                print(f"❌ Erro ao salvar arquivo: {str(e)}")
        
        print("\n" + "=" * 60)
        print("🔄 Pronto para próxima decifração...")
        print("=" * 60)

if __name__ == "__main__":
    main() 