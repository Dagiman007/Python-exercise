import turtle
turtle.showturtle()

PI = 3.14

centerX,centerY = eval(input("Enter the coordinates of the center separated by comma: "))
radius = eval(input("Enter the radius of the cicle: "))

area = PI * (radius**2)

turtle.penup()
turtle.goto(centerX,centerY)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(centerX,centerY)
turtle.write(area)
