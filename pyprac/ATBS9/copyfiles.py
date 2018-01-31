import shutil, os
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

def copyfile(name):
    name += ".txt"
    shutil.copy(dir + name, dir + "delicious") #If the folder F:\pyfold\delicious doesn't exist, it will just make a blank file. IF the folder exists, it will copy the file into that folder.

def copyfiletree():
    shutil.copytree(dir + "bacon", "bacon_backup") #Returns an error if bacon_backup exists
    #copies all of the files/folders recursively, and places them in a new folder, dst.

def movefile(name):
    name += ".txt"
    shutil.move(name, "delicious\\delicious.txt") #it's easy to overwrite files so be careful with move()
    # If the folder doesn't exist it will throw an error. If you just specify the foldername it will think it's a new file, if the folder is nonexistant

def delfile(name):
    name += ".txt"
    os.unlink(dir + name)
    #Deletes a file at (path)

def deltree(dirname):
    shutil.rmtree(dirname)

makefile(f_name) #Create initial file
#copyfile(f_name) #Copy the file to delicious
#copyfiletree() #Seperate thing with Bacon, and Bacon_Backup
#movefile("test") #move the file to delicious/delicious.txt
delfile(f_name) # Delete initial file
#deltree("bacon_backup") #Deletes the folder created with copyfiletree()