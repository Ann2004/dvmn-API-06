import os
from pathlib import Path


def delete_files_from_directory(directory):
    directory = Path(directory) 

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)