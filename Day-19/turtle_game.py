import turtle
from turtle import Turtle,Screen
is_race_on = False
import random
turtle.title("Welcome To Turtle Racing Game.")
screen = Screen()
screen.setup(width=500, height= 400)
user_input = screen.textinput(title="Make Your Bet", prompt= "Which Turtle will win the race. Enter Your Bet: ")

color_list = ["red", "purple", "blue", "green", "orange", "yellow"]
all_turtles = []



x = -230
y = -180
for i in range(0,6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x,y)
    new_turtle.speed(0)
    all_turtles.append(new_turtle)
    y += 50
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            output_color = turtle.pencolor()
            is_race_on = False
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

if output_color == user_input:
    print(f"Your Pick: {user_input}")
    print(f"Winning Turtle: {output_color}")
    print("Congratulations! You Won")
else:
    print(f"Your Pick: {user_input}")
    print(f"Winning Turtle: {output_color}")
    print("You've lost :(")
screen.exitonclick()



