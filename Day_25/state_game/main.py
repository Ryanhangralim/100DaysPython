import turtle
from writer import Writer
import pandas

def export():
    #gets list of state not answered by the user
    unanswered_state = {
        "state" : [],
        "x" : [],
        "y" : []
    }
    for state in states_list:
        if state not in answered_state:
            state_info = data[data["state"] == state]
            unanswered_state["state"].append(state)
            unanswered_state["x"].append(state_info.x.iloc[0])
            unanswered_state["y"].append(state_info.y.iloc[0])

    states = pandas.DataFrame(unanswered_state)
    states.to_csv("learn.csv")

#screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#turtle writer
writer = Writer()

#gets data from csv file
data = pandas.read_csv("50_states.csv", index_col=False)
states_list = data["state"].to_list()

#Loops while there is a chance to answer
game_is_on = True
answered_state = []

while len(answered_state) < 50:
    answer_state = screen.textinput(title=f"{len(answered_state)}/50 States Correct", prompt="What's another state's name?")

    if answer_state:
        answer_state = answer_state.title()

    if answer_state == "Exit":
        export()
        break

    #checks if answer is in list
    if((answer_state in states_list) and (answer_state not in answered_state)):
        state_info = data[data["state"] == answer_state]
        writer.write_text(answer_state, state_info.x.iloc[0], state_info.y.iloc[0])
        answered_state.append(answer_state)