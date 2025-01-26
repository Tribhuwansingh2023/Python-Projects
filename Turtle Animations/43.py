import turtle as t
from colorsys import *
t.speed(0)
t.bgcolor('black')
t.pensize(2)
R = 0
for i in range(250):
    t.color(hsv_to_rgb(R, 1, 1))
    R += 0.0035
    t.forward(i)
    t.left(59)
    t.hideturtle()
t.done()
