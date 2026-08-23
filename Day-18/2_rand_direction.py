import turtle as t
import random

tim = t.Turtle()
direction = [0,90,180,270]
colours = ["aquamarine", "dark sea green", "dark green", "dark slate blue", "dark red",
           "yellow", "royal blue", "light green", "saddle brown"]
tim.pensize(15)
tim.speed(0)
def select_direction():
    tim.forward(30)
    tim.setheading(random.choice(direction))


for i in range(200):
    tim.color(random.choice(colours))
    select_direction()

my_screen = t.Screen()
my_screen.screensize()
my_screen.exitonclick()