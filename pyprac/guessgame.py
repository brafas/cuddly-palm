import random

secretNum = random.randint(1, 20)
print("I have picked a number between 1 and 20.")

for guessesTaken in range(1, 7):
    print("take a guess.")
    guess = int(input())

    if guess < secretNum:
        print("Too low.")
    elif guess > secretNum:
        print("Too high.")
    else:
        break #correct guess

if guessesTaken == secretNum:
    print("Good job! That's correct! It took you " + str(guessesTaken) + ' guesses!')
else:
    print("Out of guesses, the number was: " + str(secretNum))