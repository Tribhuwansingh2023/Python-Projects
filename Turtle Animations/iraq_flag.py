import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("#303030")
t.speed(1000)

def draw_tectangle(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range (2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

if __name__ == '__name__':
    turtle.speed('show')
turtle.penup()
turtle.goto(-250, 150)
turtle.pendown()
draw_tectangle(500, 100, '#ff0000')

turtle.penup()
turtle.goto(-250, 50)
turtle.pendown()
draw_tectangle(500, 100, '#ffffff')

turtle.penup()
turtle.goto(-250, -50)
turtle.pendown()
draw_tectangle(500, 100, "#000000")
turtle.end_fill()

turtle.color("green")
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
style = ("adwa-assalaf", 60, "bold")
turtle.write("الله أكبر", font=style, align="center")
turtle.hideturtle()
turtle.done()
