import turtle

mt = turtle.Turtle()
mt.penup()
mt.goto(-turtle.window_width() / 2, -turtle.window_height() / 2)
mt.pendown()
mt.speed(90)
mt.pensize(10)
mt.color('grey')

for _ in range(24):

    mt.left(90)
    mt.fd(900)
    mt.right(90)
    mt.fd(20)

    mt.right(90)
    mt.fd(900)
    mt.left(90)
    mt.fd(20)

turtle.done()
