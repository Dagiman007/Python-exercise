import turtle

t = turtle.Pen()
turtle.bgcolor("white")
t.speed(0)
colors = ["blueviolet", "cornflowerblue", "darkgreen", "maroon"]

for x in range(230):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
