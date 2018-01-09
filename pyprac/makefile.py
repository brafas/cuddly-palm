def main():
    f = open("makefile.txt", "w+")
    f.write("This was written by a python module.")
    f.close()
if __name__ == "__main__":
    main()