import turtle

def draw_polygon(turtle, sides):
    angle = 360 / sides
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.end_fill()

sides = int(input("Введите количество вершин многоугольника: "))
window = turtle.Screen()
window.setup(width=1920, height=1080)
window.bgcolor("white")

t = turtle.Turtle()
t.right(45)
t.fd(150)
t.backward(150)
t.left(45)
t.shape("turtle")
t.penup()
t.fd(100)
t.stamp()
t.bk(100)

t.color("black", "yellow")
t.begin_fill()
t.pendown()
for i in range(3):
    t.fd(50)
    t.right(120)
t.end_fill()

draw_polygon(t, sides)

turtle.speed(0)
turtle.done()
