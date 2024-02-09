from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_axis = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    turtles.append(new_turtle)
    y_axis += 35

winner = None
is_race_on = True
if user_bet:
    while is_race_on:
        for turtle in turtles:
            if(turtle.xcor() > 230):
                winner = turtle.pencolor()
                is_race_on = False
            turtle.forward(random.randint(0, 10))

              
if user_bet == winner:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")


screen.exitonclick()