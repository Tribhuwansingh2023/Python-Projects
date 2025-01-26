from turtle import *
bgcolor('black')
speed(0)
pencolor('gold')
def draw(x):
    right(10)
    for i in range(4):
        forward(x)
        right(90)
        forward(x)
x = 120
for i in range(8):
    for j in range(36):
        draw(x)
    x -= 10
hideturtle()
done()
