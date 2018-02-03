import os, shutil

sevzip_Path = 'F:\\AndEmu'

for (dirPath, dirNames, fileNames) in os.walk(sevzip_Path):
    print('Path is: ' + dirPath)
    print('Subfolds: ' + str(dirNames))
    print("Files: " + str(fileNames))

shutil.rmtree(sevzip_Path)