#Get the subtotal and gratuity rate in percentage from the user

subtotal,gratuityRate = eval(input("Please enter the subtotal and gratuity \
rate separated by comma :"))

#change the graatuity rate to decimal

gratuityRate /= 100

#calculate the gratuity and the total

gratuity = subtotal * gratuityRate
total = subtotal + gratuity

#display the results

print("The gratuity is ",round(gratuity,2)," and the total is ",round(total,2),'.')


