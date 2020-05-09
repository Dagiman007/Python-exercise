'''A program that computes an initial deposit amount
needed to reach a specified final amount in one's
account'''

finalAccountValue = eval(input("Enter final amount of account : ")) #get the final account value from the user
annualInterestRate = eval(input("Enter annual interest rate in percentage: ")) 
numberOfYears = eval(input("Enter the number of years: "))

annualInterestRate /= 100 # express the annual interest rate in decimal
monthlyInterestRate = annualInterestRate / 12 # compute the monthly interest rate
numberOfMonths = numberOfYears * 12 #find number of months in the years specified

initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate)**numberOfMonths) #calculate the initial deposite value

print("Initial deposit value is ",initialDepositAmount) #display the initial deposit value
