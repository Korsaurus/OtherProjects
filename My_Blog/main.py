import random
from datetime import datetime

import requests as requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():

    current_year = datetime.now().year
    random_number = random.randint(0, 10)

    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def api_thing(name):

    r = requests.get(f"https://api.agify.io?name={name}")
    r_data = r.json()
    age_guess = r_data["age"]

    return render_template("api_pract.html", name=name, age=age_guess)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(blog_url)
    all_posts = r.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
