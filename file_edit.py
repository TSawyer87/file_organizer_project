import os

file_path = 'path/to/file.txt'

# Get file type
file_type = os.path.splitext(file_path)[1]

# Get file size in bytes
file_size = os.path.getsize(file_path)

# Get date of creation
creation_date = os.path.getctime(file_path)

print(f"File Type: {file_type}")
print(f"File Size: {file_size} bytes")
print(f"Creation Date: {creation_date}")
