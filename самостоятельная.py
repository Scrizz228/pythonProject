import turtle
import random

def draw_square():
    turtle.speed(1)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()


def check_password(password):
    while True:
        user_input = input("Введите пароль: ")
        if user_input == password:
            return True


def main():
    password = "123"
    if not check_password(password):
        print("Неверный пароль. Попробуйте снова.")
        return

    turtle.bgcolor("white")
    screen = turtle.Screen()

    num_similar_figures = int(input("Сколько  квадратов нарисовать? "))

    for _ in range(num_similar_figures):
        turtle.color(random.random(), random.random(), random.random())
        draw_square()
        turtle.forward(120)

    screen.exitonclick()

if __name__ == "__main__":
    main()
