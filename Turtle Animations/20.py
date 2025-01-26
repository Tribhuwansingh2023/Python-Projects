from turtle import *
speed(0)
bgcolor("black")
pensize(2)
for i in range(125):
    color("#909090")
    circle(5 - i, 100)
    lt(80)
    circle(5 - i, 100)
    rt(160)
    hideturtle()
done()
