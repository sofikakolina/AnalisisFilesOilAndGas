import shutil
from os import path

def move(filemame):
    if path.exists(filemame):
        destination_path='fireFiles'
        shutil.copy(filemame, destination_path)