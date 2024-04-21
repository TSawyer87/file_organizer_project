# Sort files by date of creation

import os

directory = 'path/to/files/'

files = os.listdir(directory)
sorted_files = sorted(files, key=lambda x:
    # retrieve creation time of each file
    os.path.getctime(os.path.join(directory, x)))

for file in sorted_files:
    print(file)
