from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

x_axis = 0
segments = []
for _ in range(3):
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(x_axis, 0)
    x_axis -= 20
    segments.append(segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_cor = segments[seg_num-1].pos()
        segments[seg_num].goto(new_cor)
    segments[0].forward(20)
    segments[0].left(90)



screen.exitonclick()