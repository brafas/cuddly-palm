import shutil, os
from send2trash import send2trash

os.chdir('F:\\pyfold') #working directory
dir = "F:\\pyfold\\" #Directory
f_name = "test" #File Name
def makefile(name):
    name += ".txt"
    if os.path.exists(dir  + name) and os.path.isfile(dir  + name):
        print("Path and File Exists, doing nothing.")
    else:
        print("Making directory and file...")
        f_open = open(name, "w+")
        f_open.write("1")
        f_open.close()

def trashfile(name):
    name += ".txt"
    send2trash(name)
makefile(f_name)
trashfile(f_name)