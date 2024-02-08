from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Black")

#Challenge 1 : Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Challenge 2 : Draw dotted line
#for _ in range(25):
    # tim.pendown()
    # tim.forward(10)
    # tim.penup()
    # tim.forward(10)

#Challenge 3 : draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# degree = 360
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for sides in range(3, 11):
#     angle = degree/sides
#     tim.color(random.choice(colours))
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)

#Challenge 4 : random walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pensize(8)
# tim.speed("fastest")
# angles = [0, 90, 180, 270]
# while True:
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(angles))

#Challenge 5 : Draw a spirograph
# angle = 0
# tim.speed("fastest")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# while angle < 360:
#     tim.color(random.choice(colours))
#     tim.setheading(angle)
#     tim.circle(100)
#     angle += 5


screen = Screen()
screen.exitonclick()