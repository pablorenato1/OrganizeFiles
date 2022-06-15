import os
import sys
from shutil import move

# Esse aquivo vai criar pasta de mesmo nome para cada arquivo, independente da extensão,
# porém só será movido os arquivos com extensão .pdf para sua respectiva pasta
# exemplo: caso tenha 10 arquivos .txt, será criado 10 pastas e o arquivo não será movido

path = os.path.join(sys.path[0], "fileTransform") # Encontrando o diretorio do arquivo

def organize():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file = list(file.rpartition('.')) # encontrando o '.' na string (nome do arquivo)
            folderDir = os.path.join(path, file[0]) # Diretorio para cada pasta

            try:
                os.makedirs(folderDir) # Criando pasta
            except OSError as error:
                print(error)

            if file[-1] == "pdf":
                # Movendo o arquivo com extensão .pdf para a pasta recem criada com o mesmo nome
                move(os.path.join(path, "".join(file)), os.path.join(folderDir, "".join(file)))

if __name__ == "__main__":
    organize()