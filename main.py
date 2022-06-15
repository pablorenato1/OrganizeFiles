import os
import sys
from shutil import move

path = os.path.join(sys.path[0], "fileTransform") # Encontrando o diretorio do arquivo

# Criar a pasta para armazenar os arquivos .pdf
folder = os.path.join(path, "PDF files") # diretorio
os.makedirs(folder) # Criando pasta para armazenar os arquivos .pdf

def organize():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)): # Verificação se é um arquivo
            file = list(file.rpartition('.')) # encontrando o '.' na string (nome do arquivo)

            if file[-1] == "pdf":
                move(os.path.join(path, "".join(file)), folder) # Mover para a pasta desejada

if __name__ == "__main__":
    organize()