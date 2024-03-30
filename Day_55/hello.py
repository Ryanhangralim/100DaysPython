from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<uname>")
def greet(uname):
    return f"Hello there {uname}"

if __name__ == "__main__":
    app.run(debug=True)