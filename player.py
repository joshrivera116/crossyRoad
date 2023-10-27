from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    # create a turtle
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(1)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # create a function for when the up arrow is pressed
    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)


