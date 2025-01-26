from turtle import *
tracer(30)
setposition(-40, 35)
bgcolor("black")
hideturtle()
for i in range(160):
    for c in range(5):
        color("red")
        fd(40)
        circle(160-i, 100)
        left(90)
        circle(160-i, 100)
        right(61)
done()
