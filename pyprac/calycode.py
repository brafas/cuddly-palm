def calyfunc(number):
    if number > 1:
        result = number / 2
        print(result)
        return result
    elif number < 1:
        number2 = 1 - number
        result = number2 + number
        print(result)
        return result
print("enter a number: ", end="")
numput = int(input())

while numput != 1:
    numput = calyfunc(numput)