from turtle import Turtle
# Constants
BALLCOLOR = "white"
BALLSHAPE = "circle"
BALLSPEED = 0.1
BALLSIZE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALLSHAPE)
        self.color(BALLCOLOR)
        self.penup()
        self.speed(BALLSPEED)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = BALLSPEED
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = BALLSPEED
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
