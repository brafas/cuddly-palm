def collatz(number):
    if number%2 == 0:
        numresult = number // 2
        print(str(numresult))
        return numresult
    else:
        numresult = 3 * number + 1
        return numresult

print("Enter an integer: ", end="")
guessnum = ""

while guessnum == "":
    try:
       # print("Please Enter an Integer: ", end="")
        guessnum = int(input()) #Without converting into an int, this caused an error.
    except ValueError:
        print("You must enter an integer: ", end="")

while guessnum != 1:
    guessnum = collatz(guessnum)
   # print(str(guessnum))