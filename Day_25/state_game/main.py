import turtle
from writer import Writer
import pandas

#screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#turtle writer
writer = Writer()

#gets data from csv file
data = pandas.read_csv("50_states.csv")
print(data.x)

#Loops while there is a chance to answer
game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)