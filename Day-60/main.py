from sys import path

from flask import Flask, render_template
import requests
from flask import request


app = Flask(__name__)

@app.route("/")
def get_all_posts():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f"<h1>Username:{username} password:{password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)