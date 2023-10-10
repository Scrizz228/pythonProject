from turtle import * 
from random import randint 
import numpy as np

MINX = -330 
MAXX = 500 
MINY = -300 
MAXY = 300 
DELTA = 50 
NUM = 4 
 
class Racer(Turtle): 
    def __init__(self, clr, spd, i): 
        super().__init__() 
        self.speed = spd 
        self.clr = clr
        super().color(self.clr) 
        super().shape('turtle') 
        self.x = MINX + DELTA + ((MAXX-MINX-2*DELTA) / NUM) * i 
        self.y = 0 
        self.x_icon_coordinates = (self.x - 20, self.x + 20)

    def draw(self): 
        self.penup() 
        self.goto(self.x, self.y) 
        self.showturtle() 
 
    #def startRace(self, x, y): 
    #    print(self.color) 
 
def startRace(x, y): 
    global mt, window, t
    print("click") 
    window.reset()              #удаляем все объекты с экрана при нажатии
    mt.reset()
    for i in range(NUM):
        t[i].onclick(None)


    mt.penup()                  #рисуем старт
    mt.hideturtle()
    mt.setpos(-250, -250)
    mt.pendown()
    mt.setheading(90)
    mt.forward(500)

                                   #рисуем финиш
    mt.penup()
    mt.right(90)
    mt.forward(500)
    mt.setheading(270)
    mt.pendown()
    mt.forward(500)

    y = 200
    for i in t:                 #расставляем черепашек на старте
        i.color(i.clr)
        i.penup()
        i.setpos(-270, y)
        y -= 130

    game = 'start'
    win_color = 'unknown'
    win_turtle = 'unknown'
    for i in range(200):
        for j in t:
            j.fd(j.speed)
            if j.xcor() >= 230:
                win_color = j.clr
                win_turtle = j
                game = 'over'
                break
        if game == 'over':
            break
    mt.reset()
    window.reset()
    end_race(win_color, win_turtle, x)


def end_race(win_color, win_turtle, x):                #рисуем экран результатов
    mt.hideturtle()
    mt.penup()
    mt.setpos(0, 220)
    mt.shape('turtle')
    mt.color(win_color)
    mt.stamp()

    position = 0
    angle = 60

    for i in range(4):
        t[i].hideturtle()
    for i in range(2):
        t[i].color(win_color)
        t[i].penup()
        t[i].setpos(-60, 170 + position)
        t[i].right(0 + angle)
        t[i].showturtle()
        position += 95
        angle += 270

    position = 0
    angle = 60  
    for i in range(2, 4):
        t[i].color(win_color)
        t[i].penup()
        t[i].setpos(60, 170 + position)
        t[i].left(-60 - angle)
        t[i].showturtle()
        position += 95
        angle -= 270
    
    end1_text = Turtle()
    end1_text.hideturtle()
    end1_text.penup()
    end1_text.setpos(0, 300)
    end1_text.color(win_turtle.clr)
    end1_text.write(f'{clrs1_rus[win_turtle.clr]} черепашка победила!', True, align="center", font=('Arial', 20, 'normal')) 

    if x in np.arange(win_turtle.x_icon_coordinates[0], win_turtle.x_icon_coordinates[1], 0.5):
        print(f'Вы победили. {clrs_rus[win_turtle.clr]} черепашке удалось прийти на финиш первой!')
        end_text = Turtle()
        end_text.hideturtle()
        end_text.penup()
        end_text.setpos(0, -150)
        end_text.color(win_turtle.clr)
        end_text.write(f'Вы победили. {clrs_rus[win_turtle.clr]} черепашке удалось прийти на финиш первой!', True, align="center", font=('Arial', 20, 'normal')) 
    else:
        for i in range(len(t)):
            if x in np.arange(t[i].x_icon_coordinates[0], t[i].x_icon_coordinates[1], 0.5):
                end_text = Turtle()
                end_text.hideturtle()
                end_text.penup()
                end_text.setpos(0, -150)
                end_text.color(t[i].clr)
                end_text.write(f'Вы проиграли. {clrs_rus[t[i].clr]} черепашке не удалось прийти на финиш первой!', True, align="center", font=('Arial', 20, 'normal')) 



 
#задать начальные настройки экрана 
clrs = ['red', 'blue', 'green', 'yellow'] 
clrs_rus = {'red':'Красной', 'blue':'Голубой', 'green':'Зеленой', 'yellow':'Желтой'}
clrs1_rus = {'red':'Красная', 'blue':'Голубая', 'green':'Зеленая', 'yellow':'Желтая'}

t = [] 
for i in range(NUM): 
    t.append(Racer(clrs[i], randint(5,15), i)) 
    t[i].draw() 
    t[i].onclick(startRace)
 
 
mt = Turtle()
mt.hideturtle()                                                    #Вставляем картинку
window = mt.getscreen() 
image = r"C:\Picture\puck.gif"

mt.penup() 
window.register_shape(image) 
mt.setpos(0, 250) 
mt.shape(image) 
mt.stamp() 



mt.hideturtle()                                                      #Убираем картинку
mt.shape('arrow')
mt.setpos(0, -200)
mt.write("Выберите фаворита и кликните по нему мышкой", True, align="center", font=('Arial', 20, 'normal')) 



 
done()
