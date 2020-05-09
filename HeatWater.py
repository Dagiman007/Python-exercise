''' This program calculates the energy needed to
heat water from its initial temperature to a specified
temperature'''

#Get the amount of water in kilogram, the initial and final temperature

amountOfWater = eval(input("Please enter the amount of water in kilograms :"))
initialTemp = eval(input("Enter the initial temperature :"))
finalTemp = eval(input("Enter the final temperature :"))

#compute the heat energy

heatEnergyNeeded = amountOfWater * (finalTemp - initialTemp) * 4184

#display the result

print("The energy needed is ",heatEnergyNeeded)
                   
