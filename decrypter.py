import os
from cryptography.fernet import Fernet as fer

# chave de criptografia

key = open("key.txt", "rb").read()
fernet = fer(key)

# abrir o arquivo a ser criptografado

file_name = "teste.txt"
new_file = file_name + ".ransomwaretroll"
file_data = open(new_file, "rb").read()

# Descriptografia da mensagem

decrypted_message = fernet.decrypt(file_data)

# criar o arquivo descriptografado

open(file_name, "wb").write(decrypted_message)

# remover o arquivo
os.remove(new_file)

print('decrypted done...')