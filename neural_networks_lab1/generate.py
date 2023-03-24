from turtle import *
import random
from PIL import Image
from PIL import ImageTk
import turtle as tur
import tkinter

d = {2: 'circle', 3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon'}
colors = {0: 'yellow', 1: 'red', 2: 'green', 3: 'brown', 4: 'purple'}


# Генерация датасета


def generate(tur1, a, b, c):
    tur1.fillcolor('white')
    tur1.begin_fill()

    if a != 2:
        if a <= 4:
            cb = 50
            for n in range(a):
                tur1.forward(cb)
                tur1.left(360.0 / a)
        else:
            for n in range(a):
                tur1.forward(c)
                tur1.left(360.0 / a)
    else:
        tur1.circle(c)
    tur1.end_fill()

    tur1.penup()
    tur1.goto(-50, -50)
    tur1.pendown()

    tur1.begin_fill()
    if b != 2:
        if b <= 4:
            cb = 50
            for n in range(b):
                tur1.forward(cb)
                tur1.left(360.0 / b)
        else:
            for n in range(b):
                tur1.forward(c)
                tur1.left(360.0 / b)
    else:
        tur1.circle(c)
    tur2.end_fill()


for i in range(1000):
    a1 = random.randint(2, 7)
    b1 = a1
    while b1 == a1:
        b1 = random.randint(2, 7)
    c = 30
    c1 = 30
    d1 = random.randint(1, 5)
    tur.bgpic("dataset/backgrounds/" + str(d1) + ".png")
    tur2 = Turtle()
    tur2.color('black')
    tur2.speed(0)
    tur2.hideturtle()
    screen1 = Screen()
    screen1.setup(200, 200)
    generate(tur2, a1, b1, c)
    screen = tur2.getscreen()
    canvas = screen.getcanvas()
    filename = str(i) + d[a1] + "_" + d[b1] + "_"
    canvas.postscript(file=filename + ".eps")
    img = Image.open(filename + ".eps")
    img.save("dataset/train/" + filename + ".png")
    tur2.clear()