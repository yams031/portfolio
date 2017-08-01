from turtle import *
import math

# Name your Turtle.
jimbo = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
jimbo.setposition(x_pos, y_pos)

### Write your code below:
jimbo.pendown()
#square
for i in range(4):
    jimbo.forward(100)
    jimbo.right(90)
#thingy
jimbo.pencolor("yellow")
for i in range(20):
    jimbo.forward(i * 10)
    jimbo.right(144)
#otherthingy
jimbo.pencolor("red")
for i in range(50):
    jimbo.forward(50)
    jimbo.left(123)

# Close window on click.
exitonclick()
