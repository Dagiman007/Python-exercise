import turtle

t = turtle.Pen()
turtle.bgcolor("palevioletred")
t.speed(0)
t.width(2)
numberOfCircles = int(turtle.numinput("Number of circles", "How many circles in your rosette?",6))
for x in range(numberOfCircles):
    t.pencolor("darkolivegreen")
    t.circle(100)
    t.pencolor("darkred")
    t.circle(50)
    t.left(360 / numberOfCircles)
