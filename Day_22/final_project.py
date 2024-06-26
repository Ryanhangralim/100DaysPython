from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

#add middle line
line_maker = Turtle()
line_maker.hideturtle()
line_maker.penup()
line_maker.goto(0, 300)
line_maker.setheading(270)
line_maker.pencolor("white")
line_maker.width(5)

gap = 10
height = 560
while height > 0:
    line_maker.forward(gap * 1.5)
    line_maker.pendown()
    line_maker.forward(gap)
    height -= (2.5 * gap)
    line_maker.penup()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect collision with the wall
    #detect right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()