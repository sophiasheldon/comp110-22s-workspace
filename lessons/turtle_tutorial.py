"""Tutorial drawing with turtle."""


from turtle import Turtle, colormode, done
colormode(255)
side_length: float = 300.0

leo: Turtle = Turtle()
leo.penup()
leo.goto(0, 0)
leo.pendown()
leo.color(254, 101, 190)
leo.begin_fill()
leo.speed(50)
leo.hideturtle()
# code for shape to be filled 
i: int = 0 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
colormode(255)


bob.goto(0, 0)
bob.color(36, 200, 255)
bob.begin_fill()
bob.speed(75)
bob.hideturtle()
i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(122)
    i += 1
    side_length = side_length * 0.97
bob.end_fill
done()
