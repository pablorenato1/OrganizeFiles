import os
import sys
from shutil import move

path = os.path.join(sys.path[0], "fileTransform")
# Criar a pasta para armazenar os arquivos .pdf
folder = os.path.join(path, "PDF files") # diretorio
os.makedirs(folder) # Criando

def organize():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file = list(file.rpartition('.')) # encontrando o '.' na string (nome do arquivo)
            folderDir = os.path.join(path, file[0])

            if file[-1] == "pdf":
                move(os.path.join(path, "".join(file)), folder) # Mover para a pasta desejada

if __name__ == "__main__":
    organize()