from turtle import Turtle
class States:
    def __init__(self):
        self.tom = Turtle()
        self.tom.penup()
        self.tom.hideturtle()

    def move(self, state,x,y):
        self.tom.goto(x,y)
        self.tom.write(f"{state}", align="center", font=("Arial", 8, "normal"))






