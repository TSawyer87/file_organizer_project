import os
import shutil

source_directory = 'path/to/source/'
destination_directory = 'path/to/destination/'

files = os.listdir(source_directory)

for file in files:
    source_path = os.path.join(source_directory, file)
    destination_path = os.path.join(destination_directory, file)
    shutil.move(source_path, destination_path)
