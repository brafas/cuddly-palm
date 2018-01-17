import os

def main():
    dirtxt = open("dirtext.txt", "w+")
    dirls = os.listdir()
    dirls = ", ".join(x for x in dirls) #use str(x) for non string lists.
    dirtxt.write(dirls)
    dirtxt.close()

if __name__ == "__main__":
    main()