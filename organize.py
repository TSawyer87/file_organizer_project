import os
import shutil

# directory paths
source_directory = 'path/to/files/'
image_directory = 'path/to/images/'
document_directory = 'path/to/documents/'
music_directory = 'path/to/music/'

# gather the list of files from the source directory
files = os.listdir(source_directory)

# iterate through the files in the source directory
for file in files:
    # move images to the image directory
    if file.endswith(('.jpg', '.png', '.gif')):
        shutil.move(os.path.join(source_directory, file), image_directory)

    # move documents to the document directory
    elif file.endswith(('.pdf', '.doc', '.txt')):
        shutil.move(os.path.join(source_directory, file), document_directory)

    # move music to the music directory
    elif file.endswith(('.mp3','.wav', '.flac')):
        shutil.move(os.path.join(source_directory, file), music_directory)
