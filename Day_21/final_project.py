from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() 
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect the collision from the snake to the food
    if snake.head.distance(food) < 15:
        score_board.add_score()
        food.refresh()

    #detect the collision with the wall
    x_head = snake.head.xcor()
    y_head = snake.head.ycor()
    if x_head > 280 or x_head < -280 or y_head > 280 or y_head < -280:
        game_is_on = False
        score_board.game_over()


screen.exitonclick()