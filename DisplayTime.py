seconds = eval(input("Please enter seconds : "))

minutes = seconds//60 #only the minutes in the seconds
remainingSeconds = seconds%60 #fraction of minutes remaining

print(seconds," is ",minutes," minutes and ",remainingSeconds," seconds")
