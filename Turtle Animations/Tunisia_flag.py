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
draw_tectangle(600, 300, "red")
color("white")
up()
goto(0, -100)
down()
begin_fill()
circle(100, 360)
right(10)
end_fill()
color("red")
left(130)
up()
goto(70, 40)
down()
begin_fill()
circle(80, 300)
right(7)
circle(64, -265)
end_fill()
up()
goto(-30, 0)
down()
setheading(0)
left(15)
begin_fill()
for i in range(5):
    forward(100)
    right(144)
end_fill()
up()
left(15)
goto(-500, 185)
down()
hideturtle()
done()
