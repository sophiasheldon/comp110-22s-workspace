"""Drawing a Barbie Dream House!"""

__author__ = "730330800"

from turtle import Turtle, colormode, done
colormode(255)

roof: Turtle = Turtle()
roof.penup()
roof.goto(-150.0, 100.0)
roof.pendown()
roof.pencolor("pink")
roof.fillcolor(198, 3, 167)
roof.begin_fill()
roof.speed(50)
roof.hideturtle()
i: int = 0 
while (i < 3): 
    roof.forward(300)
    roof.left(120)
    i += 1 
roof.end_fill()

square: Turtle = Turtle()
square.penup()
square.goto(-150.0, -200.0)
square.pendown()
square.pencolor("pink")
square.fillcolor(255, 119, 233)
square.begin_fill()
square.speed(50)
square.hideturtle()
i: int = 0 
while (i < 4): 
    square.forward(300)
    square.left(90)
    i += 1
square.end_fill()

window_one: Turtle = Turtle()
window_one.penup()
window_one.goto(-100.0, -25.0)
window_one.pendown()
window_one.pencolor("pink")
window_one.fillcolor(162, 67, 159)
window_one.begin_fill()
window_one.speed(50)
window_one.hideturtle()
i: int = 0
while (i < 4): 
    window_one.forward(50)
    window_one.left(90)
    i += 1 
window_one.end_fill()

window_two: Turtle = Turtle()
window_two.penup()
window_two.goto(50.0, -25.0)
window_two.pendown()
window_two.pencolor("pink")
window_two.fillcolor(162, 67, 159)
window_two.begin_fill()
window_two.speed(50)
window_two.hideturtle()
i: int = 0
while (i < 4): 
    window_two.forward(50)
    window_two.left(90)
    i += 1 
window_two.end_fill()

door: Turtle = Turtle()
door.penup()
door.goto(-50.0, -200.0)
door.pendown()
door.pencolor("pink")
door.fillcolor(232, 226, 79)
door.begin_fill()
door.speed(50)
door.hideturtle()
i: int = 0 
while (i < 4): 
    door.forward(100)
    door.left(90)
    i += 1 
door.end_fill()
done()