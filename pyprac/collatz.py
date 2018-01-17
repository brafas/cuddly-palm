def collatz(number):
    if number%2 == 0:
        numresult = number // 2
        print(str(numresult))
        return numresult
    else:
        numresult = 3 * number + 1
        return numresult


print('Enter number: ')
guessnum = input()
while guessnum != 1:
    guessnum = collatz(guessnum)
    print(str(guessnum))