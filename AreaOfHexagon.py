'''A program that calculates the area of hexagon
with side length s'''
import math

#get the length of a side

side = eval(input("Enter the length of a side: "))

#compute the area

area = (3 * math.sqrt(3)/2) * math.pow(side,2)

#display the result

print("The area of the hexagon is ",round(area,2))
