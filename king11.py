import turtle, datetime


def draw(dra):
    turtle.pendown() if dra else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def dig(d):
    draw(True) if d in [2, 3, 4, 5, 6, 8, 9] else draw(False)
    draw(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw(False)
    draw(True) if d in [0., 2, 3, 5, 6, 8, 9] else draw(False)
    draw(True) if d in [0, 2, 6, 8] else draw(False)
    turtle.left(90)
    draw(True) if d in [0, 4, 5, 6, 8, 9] else draw(False)
    draw(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else draw(False)
    draw(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else draw(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def date(dat):
    for i in dat:
        dig(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(10)
    turtle.pencolor("black")

    date(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
    turtle.done()


main()
