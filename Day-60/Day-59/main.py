from flask import Flask, render_template
import requests
from flask import request
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


@app.route("/")
def get_all_posts():
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url=url)
    all_posts = response.json()
    name = "Diwas"
    return render_template("index.html", posts=all_posts, name=name)


@app.route("/about")
def about():
    return render_template("about.html")


# SOLUTION to Challenge:
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        sender = os.environ["SENDER"]
        receiver = os.environ["RECEIVER"]
        password = os.environ["PASSWORD"]
        message = f"Subject:You've got a message\n\n\nName = {data["username"]}\nEmail={data["email"]}\nPhone={data["phone"]}\nMessage={data["message"]}"
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(user = sender, password= password)
            smtp.sendmail(sender, receiver, message)
        return render_template("contact.html", message="Successfully Sent Your Message")

    return render_template("contact.html", message="Contact Me")


@app.route("/post/<int:num>")
def posts(num):
    url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(url=url)
    all_posts = response.json()

    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == num:
            requested_post = blog_post
            break

    name = "Diwas"
    return render_template("post.html", post=requested_post, name=name)


if __name__ == "__main__":
    app.run(debug=True)
