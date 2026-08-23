from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-280)
        self.shape("turtle")
        self.setheading(90)



    def reset_position(self):
        self.goto(0,-280)

    def up(self):
        self.forward(20)


