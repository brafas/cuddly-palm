import os

# Let's just figure out how to return extensions with file sizes, and work with that data
# rewrite yo code

actDir = os.path.abspath(os.curdir)
# Returns the current directory.


def getFileSize(path): # Get the size of every file recursively in the active folder.
    for root, folders, files in os.walk(path):
        for filename in files:
            curPath = os.path.abspath(root) + os.sep + filename
            rawSize = os.path.getsize(curPath)
            print('File: ' + curPath + ' Size: ' + str(rawSize))
            # return rawSize

def getFileExt(path):
    for root, folders, files in os.walk(path):
        for filename in files:
            curPath = os.path.abspath(root) + os.sep + filename
            ext = os.path.splitext(curPath)[1]
            print(ext)


#getFileSize(actDir)
getFileExt(actDir)