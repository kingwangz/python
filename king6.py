import turtle
turtle.setup(650,350,200,200)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor("blue")
for i in range(1000):
    turtle.seth(90*i)
    turtle.fd(i*2)
turtle.done()