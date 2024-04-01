from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route("/post/<page>")
def get_blog(page):
    return render_template("post.html", posts=response, page=int(page))

if __name__ == "__main__":
    app.run(debug=True)
