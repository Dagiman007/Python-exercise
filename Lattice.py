# Draw a 16-by-16 lattice
import turtle

x = -80
for y in range(-80,80 + 1,10):
    if y == 30:
        continue
    turtle.penup()
    turtle.goto(x,y)    #Draw horizontal line
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80,80 + 1,10):
    turtle.penup()
    turtle.goto(x,y)    # Draw vertical line
    turtle.pendown()
    turtle.forward(160)
    
    
