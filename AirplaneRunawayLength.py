'''A program to find the minimum runawat lenght
needed by an airplane to take off'''

speed = eval(input("Enter the speed of the plane in meters per second :")) #Get the speed from the user
acceleration = eval(input("Enter the acceleration in meters per second squared :")) # get the acceleration

minimumRunawayLength = (speed**2)/(2 * acceleration) # compute the minimum runaway length

print("The minimum runaway length needed is :",minimumRunawayLength) #display the result
              
                   
