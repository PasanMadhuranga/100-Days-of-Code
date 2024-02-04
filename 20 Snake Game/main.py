from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

def listen_to_user():
    """Unable arrow keys to move the snake."""
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def play_again():
    """Asks user whether he wants to play again or not"""
    want_to_play_again = screen.textinput(title="Play Again?",
                                          prompt="Do you want to play again. Type 'yes' or 'no'").lower()
    if want_to_play_again == "yes":
        scoreboard.reset()
        snake.reset_snake()
        listen_to_user()
        return True
    else:
        screen.bye()
        return False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

listen_to_user()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collisions with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        scoreboard.game_over()
        time.sleep(2)
        if not play_again():
            game_is_on = False


    # Detect collisions with tail.
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            time.sleep(2)
            if not play_again():
                game_is_on = False
            # scoreboard.reset()
            # snake.reset_snake()




screen.exitonclick()
