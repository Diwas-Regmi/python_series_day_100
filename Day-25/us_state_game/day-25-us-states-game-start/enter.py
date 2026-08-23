from turtle import Turtle
class EnterState:
    def __init__(self):
        self.tom = Turtle
        self.tom.penup()
        self.tom.hideturtle()
        self.tom.goto()

        self.tom.enter = (screen.textinput("Input", "Enter a State:"))
