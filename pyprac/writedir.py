import os

def main():
    dirtxt = open("dirtext.txt", "w+")
    dirls = os.listdir()
    dirls = ", ".join(str(x) for x in dirls)
    dirtxt.write(dirls)
    dirtxt.close()

if __name__ == "__main__":
    main()