import turtle
from UsefulTurtleFunctions import *

count = 1
for x in range(-140,140+1,40):
    for y in range(-140,140+1,40):
        if count%2 == 0:
            turtle.begin_fill()
            turtle.color('black')
            drawRectangle(x,y,40,40)
            turtle.end_fill()
        else:
            drawRectangle(x,y,40,40)
        count += 1
    count += 1
            
    
        
    
    
