import turtle as t
from random import *
t.Screen().colormode(255)
t.speed(0)
t.bgcolor((0, 0, 0))
for i in range(333):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.left(70)
    t.forward(i)
t.done()
