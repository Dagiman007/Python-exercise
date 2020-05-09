#A program that calculate the day of the week given a year,month and date

import math

#prompt the user to enter the year,month and the date
year = eval(input("Enter year: (e.g. 2018)"))
month = eval(input("Enter month, 1-12: "))
date = eval(input("Enter the day of the month, 1-31: "))

if month == 1 or month == 2:   #January and February are counted as 13 and 14 of the previous year
    month += 12
    year -= 1 

century = math.floor(year/100) # calculates the century of the year
yearOfCentury = year % 100



dayOfWeek = (date + math.floor((26*(month + 1)/10)) + yearOfCentury + math.floor(yearOfCentury/4) 
             + math.floor(century/4) + 5*century )%7

if dayOfWeek == 0:
    print("Day of the week is Saturday")
elif dayOfWeek == 1:
    print("Day of the week is Sunday")
elif dayOfWeek == 2:
    print("Day of the week is Monday")
elif dayOfWeek == 3:
    print("Day of the week is Tuesday")
elif dayOfWeek == 4:
    print("Day of the week is Wednesday")
elif dayOfWeek == 5:
    print("Day of the week is Thursday")
else:
    print("Day of the week is Friday")
