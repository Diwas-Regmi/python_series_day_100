import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
direction = [0,90,180,270]
tim.speed(0)
tim.width(1)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        current_heading = tim.heading()
        tim.setheading(current_heading+size_of_gap)
        tim.color(random_color())
        tim.circle(100)

draw_spirograph(10)
my_screen = t.Screen()
my_screen.screensize()
my_screen.exitonclick()