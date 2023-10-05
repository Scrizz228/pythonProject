import turtle

def draw_brick():
    mt.begin_fill()
    for _ in range(2):
        mt.fd(40)
        mt.right(90)
        mt.fd(20)
        mt.right(90)
    mt.end_fill()

mt = turtle.Turtle()
mt.color("#928C8C")
mt.fillcolor("#904D30")
mt.speed(999)
mt.penup()
mt.setpos(-150, 100)
mt.pendown()
turtle.bgcolor('dark green')

direction = 1

for _ in range(7):
    for _ in range(10):
        draw_brick()
        mt.penup()
        mt.fd(40 * direction)
        mt.pendown()

    mt.penup()
    mt.goto(mt.xcor(), mt.ycor() - 20)
    mt.pendown()

    direction *= -1

turtle.done()
