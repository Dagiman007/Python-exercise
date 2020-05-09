#Get the loan amount, annual interest rate and the number of years the payment will be made from the user

loanAmount = float(input("Please enter the loan amount : "))
annualInterestRate = float(input("Enter the annual interest rate in percentage : "))
numberOfYears = int(input("Enter the number of years the payment will be made : "))

#Represent the annual interest rate in decimal and compute the monthly interest rate

annualInterestRate /= 100
monthlyInterestRate = annualInterestRate / 12

#compute monthly payment and total payment

monthlyPayment = (loanAmount * monthlyInterestRate) / (1 -(1 / (1 + monthlyInterestRate)**(numberOfYears * 12)))
totalPayment = monthlyPayment * numberOfYears * 12

#Display monthly payment and total payment

print("The monthly payment is ",int(monthlyPayment*100)/100)
print("The total Patment is ",int(totalPayment*100)/100)

