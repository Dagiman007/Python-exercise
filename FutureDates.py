#prompt the user to enter today's day of the week and number of days after today for the future
today = int(input("Enter today's day (0:sunday,1:monday...6:saturday): " ))
numberOfDays = int(input("Enter the number of days elapsed since today: "))

futureDay = (today + numberOfDays)%7

def dayOfWeek(day):
    if day == 0:
        return 'Sunday'
    if day == 1:
        return 'Monday'
    if day == 2:
        return 'Tuesday'
    if day == 3:
        return 'Wednesday'
    if day == 4:
        return 'Thursday'
    if day == 5:
        return 'Friday'
    if day == 6:
        return 'Saturday'
    
print("Today is ",dayOfWeek(today)," and the future day is ",dayOfWeek(futureDay))
     
