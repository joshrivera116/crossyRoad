from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = 5

    def create_car(self):
        rand_num = randint(1, 5)
        if rand_num == 1:
            new_car = Turtle('square')
            new_car.shapesize(1, 2, 0)
            new_car.color(choice(COLORS))
            new_car.penup()
            start_x = 320
            rand_y = randint(-200, 200)
            new_car.goto(start_x, rand_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def car_speed_up(self):
        self.move_distance += MOVE_INCREMENT
