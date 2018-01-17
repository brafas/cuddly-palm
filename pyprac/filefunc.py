from os import makedirs
from os.path import isfile
from os.path import exists

def main(dname, fname):
    file_mk(fname)
    dir_mk(dname)

def file_mk(fname):
    if isfile(fname):
        print('file exists, aborting')
    else:
        print('making file: '+fname)
        f = open(fname, "w+")
        f.close()

def dir_mk(dname):
    if exists(dname):
        print("folder exists, aborting")
    else:
        print("Creating folder: "+dname)
        makedirs(dname)

if __name__=="__main__":
    main("dingus", "dingus/dongus")