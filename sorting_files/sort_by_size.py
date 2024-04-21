# Sort files by size

import os

directory = 'path/to/files/'

files = os.listdir(directory)
sorted_files = sorted(files, key=lambda x:
# Sort files in decending order
   os.path.getsize(os.path.join(directory, x)), reverse=True)

for file in sorted_files:
    print(file)
