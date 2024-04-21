import os

directory = 'path/to/files/'
min_size = 1024  # Minimum file size in bytes

files = os.listdir(directory)
filtered_files = [file for file in files if 
   os.path.getsize(os.path.join(directory, file)) > min_size]

for file in filtered_files:
    print(file)
