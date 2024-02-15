import turtle
from writer import Writer

#screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#turtle writer
writer = Writer()
writer.write_text("Alabama", 139, -77)

#Loops while there is a chance to answer
game_is_on = True
score = 0
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)