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
from Crypto.Util.Padding import unpad, pad
import binascii
import os
import base64
import hashlib
import secrets

def hex_to_bytes(hex_string):
    """Converte string hexadecimal para bytes"""
    return binascii.unhexlify(hex_string)

def hex_to_base64(hex_string):
    """Converte string hexadecimal para Base64"""
    return base64.b64encode(binascii.unhexlify(hex_string)).decode('utf-8')

def base64_to_hex(base64_string):
    """Converte string Base64 para hexadecimal"""
    return binascii.hexlify(base64.b64decode(base64_string)).decode('utf-8')

def generate_diffie_hellman_b():
    """Gera um valor aleatório b com no mínimo 40 dígitos e menor que p"""
    p = 1041607122029938459843911326429539139964006065005940226363139
    # Gerar um número aleatório com pelo menos 40 dígitos
    min_b = 10**39  # 40 dígitos
    max_b = p - 1
    b = secrets.randbelow(max_b - min_b) + min_b
    return b

def calculate_diffie_hellman_b(p, g, b):
    """Calcula B = g^b mod p"""
    return pow(g, b, p)

def calculate_diffie_hellman_v(p, A, b):
    """Calcula v = A^b mod p"""
    return pow(A, b, p)

def generate_shared_key(v):
    """Gera a chave compartilhada usando SHA256 e pega os primeiros 128 bits"""
    # Converter v para string
    v_str = str(v)
    # Calcular SHA256
    sha256_hash = hashlib.sha256(v_str.encode('utf-8')).hexdigest()
    # Pegar os primeiros 128 bits (32 caracteres hex)
    shared_key = sha256_hash[:32]
    return shared_key

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

def encrypt_aes_ctr(key_hex, plaintext, iv_hex=None):
    """
    Cifra texto usando AES-CTR
    
    Args:
        key_hex (str): Chave AES em hexadecimal
        plaintext (str): Texto claro para cifrar
        iv_hex (str): Vetor de inicialização em hexadecimal (opcional, gera aleatório se None)
    
    Returns:
        tuple: (iv_hex, ciphertext_hex) - IV e texto cifrado em hexadecimal
    """
    try:
        # Converter chave hex para bytes
        key = hex_to_bytes(key_hex)
        
        # Gerar IV aleatório se não fornecido
        if iv_hex is None:
            iv = os.urandom(16)  # 128 bits = 16 bytes
            iv_hex = binascii.hexlify(iv).decode('utf-8')
        else:
            iv = hex_to_bytes(iv_hex)
        
        # Converter texto para bytes e aplicar padding PKCS7
        plaintext_bytes = plaintext.encode('utf-8')
        padded_plaintext = pad(plaintext_bytes, AES.block_size)
        
        # Criar objeto de cifração AES-CTR
        cipher = AES.new(key, AES.MODE_CTR, nonce=iv[:8], initial_value=int.from_bytes(iv[8:], 'big'))
        
        # Cifrar o texto
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # Converter para hexadecimal
        ciphertext_hex = binascii.hexlify(ciphertext).decode('utf-8')
        
        return iv_hex, ciphertext_hex
        
    except Exception as e:
        return None, f"Erro na cifração: {str(e)}"

def main():
    """Função principal"""
    print("🔐 === DECIFRADOR/CIFRADOR AES INTERATIVO === 🔐")
    print("Digite 'sair' para encerrar o programa")
    print("Digite 'exemplo' para usar os dados de exemplo")
    print("Digite 'cifrar' para cifrar texto com AES-CTR")
    print("Digite 'converter' para converter entre hex e Base64")
    print("Digite 'diffie' para troca de chaves Diffie-Hellman")
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
        elif key_hex.lower() == 'cifrar':
            print("\n" + "=" * 60)
            print("🔒 CIFRAÇÃO AES-CTR")
            print("=" * 60)
            
            # Dados para cifração
            ctr_key = "33A18467DB4AF474B051523A73DDA955"
            
            print(f"🔑 Chave CTR: {ctr_key}")
            print(f"📝 Digite o texto que será cifrado:")
            plaintext = input("Texto: ").strip()
            
            if not plaintext:
                print("❌ Texto não pode estar vazio!")
                continue
            
            print(f"🔄 Gerando IV aleatório...")
            
            # Cifrar o texto
            iv_hex, ciphertext_hex = encrypt_aes_ctr(ctr_key, plaintext)
            
            if iv_hex and not ciphertext_hex.startswith("Erro"):
                print(f"\n✅ CIFRAÇÃO CONCLUÍDA!")
                print(f"🔐 IV (Counter): {iv_hex}")
                print(f"🔒 Texto cifrado: {ciphertext_hex}")
                print(f"📊 Tamanho do texto cifrado: {len(ciphertext_hex)//2} bytes")
                
                # Salvar resultado em arquivo com timestamp
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f'encrypted_text_{timestamp}.txt'
                
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                        f.write(f"Modo: AES-CTR\n")
                        f.write(f"Chave: {ctr_key}\n")
                        f.write(f"IV (Counter): {iv_hex}\n")
                        f.write(f"Texto claro: {plaintext}\n")
                        f.write(f"Texto cifrado: {ciphertext_hex}\n")
                    print(f"💾 Resultado salvo em '{filename}'")
                except Exception as e:
                    print(f"❌ Erro ao salvar arquivo: {str(e)}")
            else:
                print(f"\n❌ {ciphertext_hex}")
            
            print("\n" + "=" * 60)
            print("🔄 Pronto para próxima operação...")
            print("=" * 60)
            continue
        elif key_hex.lower() == 'converter':
            print("\n" + "=" * 60)
            print("🔄 CONVERSOR HEX ↔ BASE64")
            print("=" * 60)
            print("1. Hex → Base64")
            print("2. Base64 → Hex")
            choice = input("Escolha (1 ou 2): ").strip()
            
            if choice == '1':
                hex_input = input("Digite o valor em hexadecimal: ").strip()
                try:
                    base64_output = hex_to_base64(hex_input)
                    print(f"✅ Base64: {base64_output}")
                except Exception as e:
                    print(f"❌ Erro na conversão: {str(e)}")
            elif choice == '2':
                base64_input = input("Digite o valor em Base64: ").strip()
                try:
                    hex_output = base64_to_hex(base64_input)
                    print(f"✅ Hexadecimal: {hex_output}")
                except Exception as e:
                    print(f"❌ Erro na conversão: {str(e)}")
            else:
                print("❌ Opção inválida!")
            
            print("\n" + "=" * 60)
            print("🔄 Pronto para próxima operação...")
            print("=" * 60)
            continue
        elif key_hex.lower() == 'diffie':
            print("\n" + "=" * 60)
            print("🔑 TROCA DE CHAVES DIFFIE-HELLMAN")
            print("=" * 60)
            
            # Parâmetros Diffie-Hellman
            p = 1041607122029938459843911326429539139964006065005940226363139
            g = 10
            A = 105008283869277434967871522668292359874644989537271965222162
            
            print(f"📊 Parâmetros:")
            print(f"   p = {p}")
            print(f"   g = {g}")
            print(f"   A (de Alice) = {A}")
            print()
            
            print("🔄 Gerando valor b aleatório...")
            b = generate_diffie_hellman_b()
            print(f"✅ Valor b gerado: {b}")
            print(f"📊 Número de dígitos: {len(str(b))}")
            
            print("\n🔄 Calculando B = g^b mod p...")
            B = calculate_diffie_hellman_b(p, g, b)
            print(f"✅ Valor B calculado: {B}")
            
            print("\n🔄 Calculando v = A^b mod p...")
            v = calculate_diffie_hellman_v(p, A, b)
            print(f"✅ Valor v calculado: {v}")
            
            print("\n🔄 Gerando chave compartilhada k...")
            k = generate_shared_key(v)
            print(f"✅ Chave compartilhada k: {k}")
            
            # Salvar resultados em arquivo
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'diffie_hellman_{timestamp}.txt'
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"=== TROCA DE CHAVES DIFFIE-HELLMAN ===\n")
                    f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                    f.write(f"Parâmetros:\n")
                    f.write(f"  p = {p}\n")
                    f.write(f"  g = {g}\n")
                    f.write(f"  A (de Alice) = {A}\n\n")
                    f.write(f"Tarefa 2.1:\n")
                    f.write(f"  Valor b gerado: {b}\n")
                    f.write(f"  Número de dígitos: {len(str(b))}\n")
                    f.write(f"  Valor B calculado: {B}\n")
                    f.write(f"  Fórmula: B = g^b mod p = {g}^{b} mod {p} = {B}\n\n")
                    f.write(f"Tarefa 2.2:\n")
                    f.write(f"  Valor v calculado: {v}\n")
                    f.write(f"  Fórmula: v = A^b mod p = {A}^{b} mod {p} = {v}\n\n")
                    f.write(f"Chave compartilhada:\n")
                    f.write(f"  k (hex): {k}\n")
                    f.write(f"  Processo: SHA256({v})[:32] = {k}\n")
                print(f"💾 Resultados salvos em '{filename}'")
            except Exception as e:
                print(f"❌ Erro ao salvar arquivo: {str(e)}")
            
            print("\n" + "=" * 60)
            print("🔄 Pronto para próxima operação...")
            print("=" * 60)
            continue
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