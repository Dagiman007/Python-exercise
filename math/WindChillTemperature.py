'''A program for computing the wind chill temperature by
the National Weather Service(NWS) to measure coldness
using temperature and wind speed'''

import math #For mathematical functions like power

#get the outside temperature and the wind speed from the user

outsideTemperature = eval(input("Please enter a temperature between -58 and 41 degree fahrenheit :"))
windSpeed = eval(input("Enter the wind speed greater or equal to 2 mph :"))

#compute the wind chill temperature

windChillTemperature = 35.74 + 0.6215 * outsideTemperature - 35.75 * math.pow(windSpeed,0.16) + \
                       0.4275 * outsideTemperature * math.pow(windSpeed,0.16)

#display the wind chill temperature for the specified temperature and wind speed

print("The wind chill index is ",windChillTemperature)



