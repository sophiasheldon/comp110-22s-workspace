
from turtle import Turtle, colormode, done
colormode(255)


pen: Turtle = Turtle()

def curve() -> None: 
    for i in range(200): 
        pen.right(1)
        pen.forward(1)


def heart() -> None: 
    pen.fillcolor("red")
    pen.speed(100)
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

heart()
done()