from turtle import *
bgcolor("#303030")
def draw_tectangle(width, height, Color):
    color(Color)
    begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()
if __name__ == '__name__':
    speed('show')
penup()
goto(-300, 150)
pendown()
draw_tectangle(600, 300, "#ff0000")
color("green")
pensize(12)
up()
goto(-85, 20)
down()
for i in range(5):
    forward(160)
    right(180*4/5)
up()
goto(-500, 300)
down()
hideturtle()
done()
