import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# Create two paddles. scoreboard and the ball.
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()  # move the paddle le up when up arrow key is pressed, vise versa.
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)
    # Detect collision with wall.
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()
    # Detect collision with paddles.
    if (ball.distance(r_paddle) <= 40 and ball.xcor() > 325) or (ball.distance(l_paddle) <= 40 and ball.xcor() < -325):
        ball.paddle_bounce()
    # Detect when right paddle miss the ball and add a point to the left.
    elif ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.update_l_score()
    # Detect when left paddle miss the ball and add a point to the right.
    elif ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.update_r_score()

screen.exitonclick()
