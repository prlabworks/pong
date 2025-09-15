from turtle import Turtle

class Net (Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)  # Point downwards
        self.draw_net()

    def draw_net(self):
        for _ in range(15):  # Draw 15 dashes
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)