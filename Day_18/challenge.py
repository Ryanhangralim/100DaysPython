from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Black")

#Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Draw dotted line
#for _ in range(25):
    # tim.pendown()
    # tim.forward(10)
    # tim.penup()
    # tim.forward(10)

#draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
degree = 360
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for sides in range(3, 11):
    angle = degree/sides
    tim.color(random.choice(colours))
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()