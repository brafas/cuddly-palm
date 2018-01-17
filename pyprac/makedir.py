from os.path import exists
from os.path import pardir
from os import makedirs

def create_directory(name):
    if exists(pardir+"\\"+name):
        print("Already exists")
    else:
        makedirs(pardir+"\\"+name)

def main():
    dirname=input("Enter a folder to make: ")
    create_directory(dirname)

def delete_directory(name):
    removedirs(name)

if __name__ == "__main__":
    main()