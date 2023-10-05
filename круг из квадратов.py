import turtle 

mt = turtle.Turtle()


for i in range(24):
    for _ in range(4):
        mt.fd(20)
        mt.left(90)

    mt.fd(30)
    mt.left(15)

turtle.done()
