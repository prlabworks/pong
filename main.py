# Author: PRLabwork, Date: 2024-06-19, Description: Pong Game
#

from turtle import Screen
from paddle import Paddle

# Constants
STARTY = 200
STARTX = 500
BGCOLOR = "black"
WIDTH = 800
HEIGHT = 600
TITLE = "Pong"

screen = Screen()
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))


screen.title(TITLE)
screen.setup(width=WIDTH, height=HEIGHT, starty=STARTY, startx=STARTX)
screen.bgcolor(BGCOLOR)
screen.tracer(0)

screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()

    
    


screen.exitonclick()