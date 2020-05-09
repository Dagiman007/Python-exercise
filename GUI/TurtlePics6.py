import turtle

t = turtle.Pen()
turtle.bgcolor("antiquewhite")
t.speed(0)
t.width(2)

numberOfCircles = int(turtle.numinput("Number of circles",
                                      "How many circles do you want", 6))
for x in range(numberOfCircles):
    t.pencolor("green")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(80)
    t.pencolor("blue")
    t.circle(60)
    t.pencolor("azure")
    t.circle(40)
    t.left(360 / numberOfCircles)
