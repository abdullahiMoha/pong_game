from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# setting up screen related things
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# creating paddle turtle
r_paddle = Paddle(350, 0)
l_paddle = Paddle(x_cor = -350, y_cor = 0)

# creating the ball
ball = Ball()

# Making the ScoreBoard
scoreboard.Y_COR = 220
l_score = ScoreBoard(-100)
r_score = ScoreBoard(100)

# making the paddle(s) movable
screen.listen()

screen.onkey(fun = r_paddle.go_up, key = "Up")
screen.onkey(fun = r_paddle.go_down, key = "Down")
screen.onkey(fun = l_paddle.go_up, key = "w")
screen.onkey(fun = l_paddle.go_down, key = "s")

# running the game
game_is_on = True
while game_is_on:
	time.sleep(ball.ball_speed)
	screen.update()
	ball.move_ball()

	# Detecting ball collision with the Up and Down walls
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detecting collision between ball and right paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(
			l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# Detecting the ball when right_paddle misses
	if ball.xcor() > 380:
		l_score.score_point()
		ball.reset_ball_position()

	# Detecting the ball when left_paddle misses
	if ball.xcor() < -380:
		r_score.score_point()
		ball.reset_ball_position()

# exiting screen when clicked
screen.exitonclick()
