"""Creating a scene: Home is where the heart is, with the attempt of using a defined heart function."""

__author__ = "730330800"

from turtle import Turtle, colormode, done
colormode(255)


def draw_square(square: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a square of given width that is located at coordinates (x, y)."""
    square.penup()
    square.goto(x, y)
    square.pendown()
    square.setheading(0.0)
    # define fill color
    square.fillcolor(198, 3, 167)
    square.begin_fill()
    # set speed
    square.speed(50)
    square.hideturtle()
    i: int = 0 
    while (i < 4): 
        square.forward(width) 
        square.right(90)
        i = i + 1
    square.end_fill()


def draw_triangle(roof: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a triangle of given width that is located at coordinates (x, y)."""
    roof.penup()
    roof.goto(x, y)
    roof.setheading(0.0)
    # change marker color
    roof.pencolor("blue")
    roof.pendown()
    # define fill color
    roof.fillcolor(248, 146, 219)
    roof.begin_fill()
    # set speed
    roof.speed(50)
    roof.hideturtle()
    i: int = 0 
    while (i < 3): 
        roof.forward(width)
        roof.left(120)
        i += 1
    roof.end_fill()


# Define variable 'pen' to use within curve() and draw_heart(). 
pen: Turtle = Turtle()


def curve() -> None:
    """Draw a curved line."""
    for i in range(200):
        # set speed
        pen.speed(50) 
        pen.right(1)
        pen.forward(1)


def draw_heart(heart: Turtle, x: float, y: float, z: float) -> None:
    """Draw a heart in the center of the screen with given x, y, z color."""
    # input fill color
    pen.fillcolor(x, y, z)
    # set speed
    pen.speed(50)
    pen.begin_fill()
    # left line
    pen.left(140)
    pen.forward(113)
    # left curve
    curve()
    pen.left(120)
    # right curve 
    curve()
    # right line
    pen.forward(112)
    pen.hideturtle()
    pen.end_fill()


def draw_rectangle(door: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a rectangle of given width that is located at the coordinates (x, y)."""
    door.penup()
    door.goto(x, y)
    door.setheading(0.0)
    door.pendown()
    # define fill color
    door.fillcolor(239, 232, 167)
    door.begin_fill()
    # set speed
    door.speed(50)
    door.hideturtle()
    i: int = 0
    while (i < 4): 
        door.forward(width)
        door.left(90)
        i += 1
    door.end_fill()


def main() -> None: 
    """The entrypoint of my scene."""
    # Turtle variables declared. 
    square: Turtle = Turtle()
    door: Turtle = Turtle()
    roof: Turtle = Turtle()
    heart: Turtle = Turtle()
    # Calling previously defined procedures. 
    draw_square(square, -150, -50, 300)
    draw_square(square, -100, -100, 50)
    draw_square(square, 50, -100, 50)
    draw_rectangle(door, -50, -350, 100)
    draw_triangle(roof, -150, -50, 300)
    draw_heart(heart, 255, 1, 1)

# Curve() is used within the draw_heart function in order to achieve the curved lines in the shape. 


if __name__ == "__main__": 
    main()
done()