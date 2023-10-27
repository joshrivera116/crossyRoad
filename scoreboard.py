from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pencolor('black')
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(arg=f'Level: {self.level}', align='center', font=FONT)

    # create a level counter at the top of the game
    def add_point(self):
        self.clear()
        self.level += 1
        self.write(arg=f'Level: {self.level}', align='center', font=FONT)

    # write game over when the turtle hits a car
    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over', align='center', font=("Courier", 18, 'normal'))
