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
    # More robust paddle collision handling:
    # - check x threshold and vertical overlap
    # - nudge the ball just outside the paddle to avoid multiple rapid collisions
    # - adjust vertical velocity based on where the ball hit the paddle
    PADDLE_HALF_HEIGHT = 50  # matches Paddle shapesize(5) * 10 (half of 100)
    MAX_Y_SPEED = 15

    # Right paddle collision
    if ball.xcor() > 320 and abs(ball.ycor() - r_paddle.ycor()) < PADDLE_HALF_HEIGHT:
        # Nudge ball outside the paddle so it won't be detected again immediately
        ball.setx(330)
        # Compute deflection based on hit position (-1..1)
        offset = ball.ycor() - r_paddle.ycor()
        normalized = max(-1, min(1, offset / PADDLE_HALF_HEIGHT))
        ball.y_move = normalized * MAX_Y_SPEED
        # Ensure ball goes left
        ball.x_move = -abs(ball.x_move)
        ball.move_speed *= 0.9  # speed up

    # Left paddle collision
    if ball.xcor() < -320 and abs(ball.ycor() - l_paddle.ycor()) < PADDLE_HALF_HEIGHT:
        ball.setx(-330)
        offset = ball.ycor() - l_paddle.ycor()
        normalized = max(-1, min(1, offset / PADDLE_HALF_HEIGHT))
        ball.y_move = normalized * MAX_Y_SPEED
        # Ensure ball goes right
        ball.x_move = abs(ball.x_move)
        ball.move_speed *= 0.9  # speed up
         

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
