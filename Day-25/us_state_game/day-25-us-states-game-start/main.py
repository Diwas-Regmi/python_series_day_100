from turtle import Turtle, Screen
from states import States
import pandas as pd

screen = Screen()
turtle = Turtle()
states = States()
enter_state = Screen()
timer = Turtle()

timer.hideturtle()
timer.penup()
timer.goto(250, 250)

added_state = []
turtle.penup()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")

state = data["state"]
x = data["x"]
y = data["y"]

game_is_on = True
while len(added_state) < 50:
    value = enter_state.textinput(f"{len(added_state)}/50 correct", "Enter a State:").title()
    if value == "Exit":
        break


    elif value in state.values and value not in added_state:
        index = state[state == value].index[0]

        states.move(state[index], int(x[index]), int(y[index]))
        added_state.append(value)




# generate the states to learn csv which user have missed
missed_state = []
for item in state:
    if item not in added_state:
        missed_state.append(item)
with open("states_to_learn.csv", "w") as file:
    for item in missed_state:
        file.write(item + "\n")

screen.exitonclick()