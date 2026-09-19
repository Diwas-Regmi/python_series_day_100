from flask import Flask, render_template
from post import Post

post = Post()
all_data = post.get_data()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = all_data)

@app.route("/post/<num>")
def get_post(num):
    return render_template("post.html", all_posts = all_data, num = num)




if __name__ == "__main__":
    app.run(debug=True)
