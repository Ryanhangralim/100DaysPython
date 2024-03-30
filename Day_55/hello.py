from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrap():
        message = function()
        return f"<b>{message}</b>"
    return wrap

def make_emphasis(function):
    def wrap():
        message = function()
        return f"<em>{message}</em>"
    return wrap

def make_underlined(function):
    def wrap():
        message = function()
        return f"<u>{message}</u>"
    return wrap

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<uname>")
def greet(uname):
    return f"Hello there {uname}"

if __name__ == "__main__":
    print(say_bye())
    app.run(debug=True)