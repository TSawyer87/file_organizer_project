import os

directory = 'path/to/files/'

files = os.listdir(directory)
text_files = [file for file in files if file.endswith('.txt')]

for file in text_files:
    print(file)
