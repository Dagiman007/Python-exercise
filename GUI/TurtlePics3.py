import turtle

t = turtle.Pen()
turtle.bgcolor("midnightblue")
t.speed(0)
sides = 4 # variable for the number of sides 6 color
colors = ["antiquewhite", "burlywood", "dodgerblue", "darkblue", "indianred", "mediumslateblue"]
for x in range(300):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
