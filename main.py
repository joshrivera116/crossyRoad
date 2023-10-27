import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, 'Up')
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    if player.ycor() > 280:
        time.sleep(1)
        car.car_speed_up()
        player.reset()
        scoreboard.add_point()
        if car.move_distance == 35:
            continue
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
