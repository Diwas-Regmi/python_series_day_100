from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
screen = Screen()
screen.title("Welcome to Game")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen.listen()
# def movement
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
