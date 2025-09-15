# Author: PRLabwork, Date: 2024-06-19, Description: Pong Game
#

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time

# Constants
STARTY = 200
STARTX = 500
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"
winning_score = 5

screen = Screen()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
net = Net()

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
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 325) or (ball.distance(l_paddle) < 50 and ball.xcor() < -325):
         ball.move_speed *= 0.9  # Increase speed on paddle hit
         ball.bounce_x()
         

    # Detect if ball goes out of bounds for right paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        if scoreboard.l_score == winning_score:
            scoreboard.goto(0, 0)
            scoreboard.write("Left Player Wins!", align="center", font=("Courier", 30, "normal"))
            game_is_on = False
        else:
            ball.reset_position()
    
    # Detect if ball goes out of bounds for left paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        if scoreboard.r_score == winning_score:
            scoreboard.goto(0, 0)
            scoreboard.write("Right Player Wins!", align="center", font=("Courier", 30, "normal"))
            game_is_on = False
        else:
            ball.reset_position()

    # Move the ball
    ball.move()
    screen.update()


screen.exitonclick()
