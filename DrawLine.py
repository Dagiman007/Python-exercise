import turtle

def drawLine(p1, p2):
    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.goto(p2[0], p2[1])

p1 = [150, 60]
p2 = [-20, -112]

drawLine(p1, p2)
