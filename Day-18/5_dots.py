color_list = [(222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]
import turtle as t
import random
t.colormode(255)
from turtle import Screen, Turtle
tim = t.Turtle()
tim.hideturtle()

tim.speed(0)
y = -250
x = -250
for _ in range(10):
    tim.penup()

    tim.goto(x, y)
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    y += 50


my_screen = Screen()
my_screen.exitonclick()