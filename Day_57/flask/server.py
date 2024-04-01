from flask import Flask, render_template 
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)