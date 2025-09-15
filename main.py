# Author: PRLabwork, Date: 2024-06-19, Description: Pong Game
#

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Constants
STARTY = 200
STARTX = 500
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.title(TITLE)
screen.setup(width=WIDTH, height=HEIGHT, starty=STARTY, startx=STARTX)
screen.bgcolor(BGCOLOR)
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # Detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Move the ball
    ball.move()
    screen.update()
    

screen.exitonclick()
 