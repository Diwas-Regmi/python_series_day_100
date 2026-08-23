
from scoreboard import ScoreBoard
from snake import Snake
from turtle import Screen
import time
import random
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Nokia Inspired Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()


    for turtle in snake.turtles[1:]:

        if snake.head.distance(turtle) < 10:
            score.reset()



screen.exitonclick()
