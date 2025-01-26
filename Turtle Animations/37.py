from turtle import *
from colorsys import *
tracer(60)
bgcolor("black")
h = 0
pensize(1)
for i in range(240):
    h += 0.0015
    color(hsv_to_rgb(h, 1, 1))
    goto(0, 0)
    fd(i)
    rt(100)
    circle(70, 50)
    rt(60)
    lt(50)
    hideturtle()
done()
