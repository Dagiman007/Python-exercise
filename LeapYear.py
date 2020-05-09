'''A program that determines if a year
specified is a leap year or not'''

year = eval(input("Enter a year: "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
             (year % 400 == 0)
print(year," is a leap year? ",isLeapYear)
