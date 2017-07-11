import turtle

turtle.setup(650, 350, 200, 200)

turtle.up()
turtle.seth(270)
turtle.fd(10)
turtle.pendown()
turtle.seth(0)
turtle.pensize(3)
turtle.pencolor("red")
for i in range(50):
    turtle.circle(2 * i, 1 * i)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pencolor("blue")
for i in range(1000):
    turtle.seth(90 * i)
    turtle.fd(i * 2)
turtle.done()
