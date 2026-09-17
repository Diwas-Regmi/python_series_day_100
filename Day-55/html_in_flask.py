
from flask import Flask

app = Flask(__name__)
# print(__name__)
@app.route("/")
def hello_world():
    return (' <h1 style="text-align:center">Hello, World!</h1>'
            '<p><h3>This is a paragraph</h3></p>'
            '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTRwN3c3c3IxeWFlMmpoZXVoaWpvd2JycXI5eXdyNWJmZTNlNmkwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oxHQfvDzo7VhSRy8M/giphy.gif" width = 500, height = 500 draggable = "true">')

def make_bold(func):
    def wrapper(*args, **kwargs):
        # Call the original function to get its string result ("Bye")
        result = func(*args, **kwargs)
        # Wrap the result in HTML <b> tags
        return f"<b>{result}</b>"
    return wrapper



@app.route("/bye")
@make_bold
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