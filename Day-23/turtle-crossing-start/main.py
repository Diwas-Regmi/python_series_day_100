import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tom = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(tom.up, "Up")
    car.make_car()
    car.move_car()

    # detect car collision
    for car_list in car.all_cars:
        if car_list.distance(tom)<20:
            score.game_over()
            game_is_on = False

    # detect if level is
    if tom.ycor() > 280:
        tom.reset_position()
        car.increase_speed()
        score.increment()
screen.exitonclick()