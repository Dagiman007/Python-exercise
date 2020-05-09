import turtle

t = turtle.Pen()
turtle.bgcolor("ivory")
t.speed(0)
sides = 6
colors = ["lightblue", "peru", "blue",
          "orange", "mediumseagreen", "mediumvioletred"]

for x in range(400):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(160 / sides + 1)
    t.width(x * sides / 600)
    t.left(90)
