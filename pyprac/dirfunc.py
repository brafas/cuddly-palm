from os import makedirs
from os.path import exists

def main(name):
    mk_dir(name)

def mk_dir(name):
    if exists(name):
        print("Exists, doing nothing")
    else:
        print("Making "+name)
        makedirs(name)

if __name__=="__main__":
    main("DINGUS")