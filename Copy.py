import shutil

# Replace with the path to the source file
sourceFile = 'SkinContactMenu02102023.html'

# Destination file name
destinationFile = 'SkinContactMenu.html'

# Copy the file and give it a new name
shutil.copy(sourceFile, destinationFile)

print(f'File copied from {sourceFile} to {destinationFile}')