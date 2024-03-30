from flask import Flask
from random import *

random_number = randint(0, 9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
           
@app.route("/<int:num>")
def check_num(num):
    if num == random_number:
        return f"<h1 style='color:rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif num < random_number:
        return f"<h1 style='color:rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1 style='color:rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)})'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)