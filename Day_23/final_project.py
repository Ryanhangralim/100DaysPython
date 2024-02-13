import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Road Game")

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create car
    cars.create_car()
    cars.move(scoreboard.level)

    #detect collision with finishline
    if(player.ycor() > FINISH_LINE_Y):
        scoreboard.add_level()
        player.go_to_start()

    #detect collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()