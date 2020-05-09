'''A program the asks the user to enter
height in inches, weight in pounds and
computes the body mass index in terms
of meters and kilograms'''


#get the height and weight from the user

heightInInches = eval(input("Enter your height in inches: "))
weightInPounds = eval(input("Enter your weight in pounds: "))

heightInMeters = heightInInches * 0.0254 #convert height to meters
weightInKilograms = weightInPounds * 0.45359237 #convert weight to kilograms

#compute the body mass index

BMI = weightInKilograms / (heightInMeters ** 2)

#display the BMI

print("Your BMI is ",round(BMI,2))

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
