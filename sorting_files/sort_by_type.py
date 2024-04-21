# Sort files in dir based on file type

import os

directory = 'path/to/files/'
# retrieve list of files in dir
files = os.listdir(directory)
# sort files based on extensions & extract
sorted_files = sorted(files, key=lambda x: os.path.splitext(x)[1])
# iterate through sorted files and print their names
for file in sorted_files:
    print(file)
