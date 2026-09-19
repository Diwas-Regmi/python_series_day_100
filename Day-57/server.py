from flask import Flask
from flask import render_template
import random
import datetime
import requests
now = datetime.datetime.now()

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_num = random.randint(1,10)
    current_year = now.year
    full_name = "Diwas Regmi"
    return render_template("index.html", num = random_num, name = full_name, current_year = current_year)

@app.route("/guess/<name>")
def guess(name):
    response_gender = requests.get("https://api.genderize.io", params={"name": name})
    response_age = requests.get("https://api.agify.io", params={"name": name})
    respo_dict_age = response_age.json()
    respo_dict_gender = response_gender.json()
    return render_template("guess.html", name = name, age = respo_dict_age["age"],
                           gender = respo_dict_gender["gender"])

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/8e27568a5a48443c2568"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)