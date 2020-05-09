import turtle
import colorsys

t = turtle.Pen()
turtle.bgcolor("ivory")
t.speed(0)
turtle.width(3)

numberOfCircles = int(turtle.numinput("show it to your friends!",
                                      "How many circles do you want?", 25))

for x in range(numberOfCircles):
    t.pencolor(colorsys.hsv_to_rgb(x / numberOfCircles, 1, 1))
    t.circle(150)
    t.left(360 / numberOfCircles)
