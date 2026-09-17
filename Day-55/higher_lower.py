import random
from flask import Flask

app = Flask(__name__)
target = random.randint(0,9)

# print(__name__)
@app.route("/")
def hello_world():
    return ('<h1>Guess a Number Between 0 and 9!</h1>'
            '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHd1cnVvOG9pMThkYmRzZnpsaXlxcHM0czJ5Yzd3b3U2MHprN3p1eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ojn1S7BTXUry8elNi/giphy.gif">')


@app.route("/url/<int:num>")
def say_bye(num):
    if num < target:
        return ('<h1 style="color: red;">Too low, try Again!</h1>'
                '<img src ="https://i.giphy.com/jD4DwBtqPXRXa.webp">')
    elif num > target:
        return ('<h1 style="color: blue;">Too High, try Again!</h1>'
                '<img src ="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExODZhMDZxM2U5YzdldDZqczh1ZGV5ZzB0OTl0aDQ5eTQ1c2pkaHV2eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="color: green;">You Found Me!</h1>'
                '<img src = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGNnZjV5OGduNG9saXloYjcyeGp1YXNwNmdlOXpnNXdiOXVjOXpjeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T7e4DmcrP9du/giphy.gif">')



if __name__ == "__main__":
    app.run(debug=True)
