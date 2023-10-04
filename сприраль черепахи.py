import turtle

def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)

sides = int(input("Введите количество вершин многоугольника: "))

window = turtle.Screen()
window.setup(width=1920, height=1080)
window.bgcolor("white")


num_turtles = int(input("Введите количество черепашек спирали: "))

turtles = []
angle_increment = 360 / num_turtles
for i in range(num_turtles):
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.goto(0, 0)
    t.setheading(i * angle_increment)
    turtles.append(t)

for t in turtles:
    t.pendown()

step = 1
for i in range(360):
    for t in turtles:
        t.forward(step)
        t.right(5)
    step += 1


window.exitonclick()
