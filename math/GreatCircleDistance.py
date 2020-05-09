''' A program that computes the distance
between two distinct points on the surface
of the earth '''

import math

EARTH_RADIUS = 6371.01

#prompt the user to enter
x1,y1 = eval(input("Enter point 1 in degrees(latitude and longitude): "))
x2,y2 = eval(input("Enter point 2(latitude and longitude): "))

#change degrees to radians
x1,y1 = math.radians(x1),math.radians(y1)
x2,y2 = math.radians(x2),math.radians(y2)

#calculate the distance
distance = EARTH_RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

#Display the result
print("The distance between the two point is ",distance," km")
