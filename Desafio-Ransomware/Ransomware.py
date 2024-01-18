import os
import pyaes

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "rb") as file:
        return file.read()

def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "wb") as file:
        file.write(dados)

def criptografar_arquivo(nome_arquivo, chave):
    file_data = ler_arquivo(nome_arquivo)
    aes = pyaes.AESModeOfOperationCTR(chave)
    encrypted_data = aes.encrypt(file_data)
    return encrypted_data

def descriptografar_arquivo(nome_arquivo, chave):
    file_data = ler_arquivo(nome_arquivo)
    aes = pyaes.AESModeOfOperationCTR(chave)
    decrypted_data = aes.decrypt(file_data)
    return decrypted_data

def remover_arquivo(nome_arquivo):
    os.remove(nome_arquivo)

def menu():
    print("Escolha uma opção:")
    print("1. Criptografar arquivo")
    print("2. Descriptografar arquivo")
    return input("Opção: ")

def main():
    opcao = menu()

    if opcao == "1":
        arquivo_original = input("Digite o nome do arquivo a ser criptografado: ")
        chave = input("Digite a chave de criptografia: ").encode('utf-8')
        arquivo_criptografado = f"{arquivo_original}.encrypted"

        dados_criptografados = criptografar_arquivo(arquivo_original, chave)

        escrever_arquivo(arquivo_criptografado, dados_criptografados)

        print(f"Arquivo criptografado salvo como {arquivo_criptografado}")
    
    elif opcao == "2":
        arquivo_criptografado = input("Digite o nome do arquivo a ser descriptografado: ")
        chave = input("Digite a chave de descriptografia: ").encode('utf-8')
        arquivo_descriptografado = f"{arquivo_criptografado.replace('.encrypted', '')}.decrypted"

        dados_descriptografados = descriptografar_arquivo(arquivo_criptografado, chave)
        
        escrever_arquivo(arquivo_descriptografado, dados_descriptografados)

        print(f"Arquivo descriptografado salvo como {arquivo_descriptografado}")
    
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
