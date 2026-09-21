from flask import Flask, render_template
import requests

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

@app.route("/contact")
def contact():
    return render_template("contact.html")

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