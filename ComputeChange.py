#prompt the user to enter the amount of money in decimals

amountOfMoney = eval(input("Please enter the amount of money : "))
remainingAmount = int(amountOfMoney * 100)

#compute number of one dollars

numberOfOneDollars = remainingAmount // 100
remainingAmount %= 100

#find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount %= 25

#compute the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount %= 10
#find the number of nickels in the remaining money
numberOfNickels = remainingAmount // 5
remainingAmount %= 5
#find the number of pennies in the remaining money
numberOfPennies = remainingAmount

#display the money in dollars, quarters,dimes,nickel and pennies

print(amountOfMoney,"is ",numberOfOneDollars," dollars,",numberOfQuarters," quarters,",numberOfDimes,
      " dimes,",numberOfNickels," nickels,",numberOfPennies," pennies")
      
