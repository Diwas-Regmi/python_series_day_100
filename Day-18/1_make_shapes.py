import turtle as t
import random
tim = t.Turtle()
tim.pensize(1)
tim.speed(8)
colours = ["aquamarine", "dark sea green", "dark green", "dark slate blue", "dark red",
           "yellow", "royal blue", "light green", "saddle brown"]
def make_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colours))
    make_shape(i)




myscreen = t.Screen()
myscreen.exitonclick()


