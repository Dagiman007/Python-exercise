'''A program the computes an area of triangle
for three points specified by the user'''

import math

#Get the three points from the user

x1,y1 = eval(input("Enter the coordinates of the first point separated by comma: "))
x2,y2 = eval(input("Enter the coordinates of the second point: "))
x3,y3 = eval(input("Enter the coordinates of the third point: "))

#define distance function

def distanceFunc(x,y) :
    return (x**2 + y**2)**0.5

#compute the side length

side1 = distanceFunc(x2-x1,y2-y1) #length between point one and two
side2 = distanceFunc(x3-x1,y3-y1) #length between point one and three
side3 = distanceFunc(x2-x3,y2-y3) #length between point three and two

s = (side1 + side2 + side3)/2

#compute area of the triangle

area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))

#display the result

print("The area of the triangle is ",round(area,2))





