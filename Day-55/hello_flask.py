
from flask import Flask

app = Flask(__name__)
# print(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"
@app.route("/curse")
def say_curse():
    return "Dumbass"

# Renamed to 'show_number' and fixed variable 'a' -> 'num'
@app.route("/number/<num>")
def show_number(num):
    return f"your number is {num}"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name + "12"}!"

if __name__ == "__main__":
    app.run(debug=True)