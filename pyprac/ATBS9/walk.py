import os


walkpath = 'F:\\pyfold\\tree'
for folderName, subfolders, filenames in os.walk(walkpath): #os.walk returns a string of current folder name, list of folders in current folder, list of files in current foldere
    print('the current folder is ' + folderName)

    for subfolder in subfolders:
        print('subfolder of ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('file inside ' + folderName + ': ' + filename)
    print('')