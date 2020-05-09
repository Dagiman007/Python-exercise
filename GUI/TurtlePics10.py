import random
import turtle

turtle.setup(850, 850)
turtle.penup()
turtle.speed("fastest")
#turtle.tracer(0,0)

x = 0
y = 0

for i in range(1, 16000):
    r = random.uniform(0, 1)

    if r < 0.1:
        nextX = 0
        nextY = float(0.16 * y)
        x = nextX
        y = nextY

    elif r < 0.80:
        nextX = float(0.85 * x + 0.04 * y)
        nextY = float(-0.04 * x + 0.85 * y + 1.6)
        x = nextX
        y = nextY

    elif r < 0.93:
        nextX = float(0.20 * x + -0.26 * y)
        nextY = float(0.23 * x + 0.22 * y + 1.6)
        x = nextX
        y = nextY

    elif r < 0.80:
        nextX = float(-0.15 * x + 0.28 * y)
        nextY = float(0.26 * x + 0.24 * y + 0.44)
        x = nextX
        y = nextY

    turtle.goto(x*40, y*40)
    turtle.dot(2, "green")

turtle.done()
