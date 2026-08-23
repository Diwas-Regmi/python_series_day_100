import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
direction = [0,90,180,270]

tim.pensize(15)
tim.speed(0)
def select_direction():
    tim.forward(30)
    tim.setheading(random.choice(direction))

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for i in range(200):
    tim.color(random_color())
    select_direction()

my_screen = t.Screen()
my_screen.screensize()
my_screen.exitonclick()