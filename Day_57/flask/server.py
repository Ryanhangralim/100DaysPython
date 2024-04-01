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

@app.route("/guess/<name>")
def guess(name):
    AGIFY_ENDPOINT = "https://api.agify.io"
    GENDERIZE_ENDPOINT = "https://api.genderize.io"

    PARAMS = {
        "name" : name
    }
    agify_response = requests.get(url=AGIFY_ENDPOINT, params=PARAMS).json()
    genderize_response = requests.get(url=GENDERIZE_ENDPOINT, params=PARAMS).json()
    return render_template("guess.html", name=name, gender=genderize_response["gender"], age=agify_response["age"])

if __name__ == "__main__":
    app.run(debug=True)