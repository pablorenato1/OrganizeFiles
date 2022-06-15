import os
import sys
from shutil import move

path = os.path.join(sys.path[0], "fileTransform")

def organize():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file = list(file.rpartition('.'))
            folderDir = os.path.join(path, file[0])

            try:
                os.makedirs(folderDir)
            except OSError as error:
                print(error)

            if file[-1] == "pdf":
                move(os.path.join(path, "".join(file)), os.path.join(folderDir, "".join(file)))

if __name__ == "__main__":
    organize()