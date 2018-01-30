import shutil, os
os.chdir('F:\\pyfold') #working directory
dir = "F:\\pyfold\\" #Directory
f_name = "dingus" #File Name
def makefile(name):
    name += ".txt"
    if os.path.exists(dir  + name) and os.path.isfile(dir  + name):
        print("Path and File Exists, doing nothing.")
    else:
        print("Making directory and file...")
        f_open = open(name, "w+")
        f_open.write("1")
        f_open.close()

def copyfile(name):
    name += ".txt"
    shutil.copy(dir + name, dir + "delicious") #If the folder F:\pyfold\delicious doesn't exist, it will just make a blank file. IF the folder exists, it will copy the file into that folder.

makefile(f_name)
copyfile(f_name)