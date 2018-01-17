print("Enter your total price: ", end="")
endPrice=float(input())
print("Enter your initial payment: ", end="")
initPay = float(input())
installTotal = endPrice - initPay
monthlyPay = installTotal / 4

print("Your payments monthly, for the next 4 months, will be: "+str(monthlyPay))
totalPay = monthlyPay*4 + initPay
print("Your total is: "+str(totalPay))
