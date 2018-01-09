def main():
    with open("makefile.txt", "r") as f:
       lines = f.readlines()
    print(lines[1])
    print(lines[5])
if __name__ == "__main__":
    main()