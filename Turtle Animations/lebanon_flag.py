import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#303030")
t.speed(20)

def draw_rectangle(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

if __name__ == '__name__':
    turtle.speed('show')

turtle.penup()
turtle.goto(-250, 120)
turtle.pendown()
draw_rectangle(500, 60, '#ff0000')
turtle.penup()
turtle.goto(-250, 60)
turtle.pendown()
draw_rectangle(500, 120, '#ffffff')
turtle.penup()
turtle.goto(-250, -60)
turtle.pendown()
draw_rectangle(500, 50, '#ff0000')

turtle.penup()
turtle.goto(-250, -150)
turtle.pendown()
turtle.color('#138808')
turtle.penup()
turtle.goto(0, 60)
turtle.pendown()
turtle.begin_fill()
turtle.right(60)
turtle.forward(120)
turtle.right(120)
turtle.forward(120)
turtle.right(120)
turtle.forward(120)
turtle.end_fill()

turtle.penup()
turtle.goto(-20, -30)
turtle.right(60)
turtle.pendown()
draw_rectangle(40, 28, '#138808')

turtle.hideturtle()
turtle.done()