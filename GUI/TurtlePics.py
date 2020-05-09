import turtle

t = turtle.Pen()
turtle.bgcolor("tomato")
t.speed(0)

colors = ["red", "yellow", "blue", "green"]
for x in range(350):
    t.pencolor(colors[x % 4])
    t.forward(2 * x)
    t.left(100)
