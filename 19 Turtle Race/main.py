import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
while True:
    user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Pick a color:").lower()
    if user_bet in colors:
        break
turtles_list = []


def create_set_turtles():
    """Create and Set the positions of the turtles."""
    for y in range(6):
        tim = Turtle(shape="turtle")
        tim.color(colors[y])
        tim.penup()
        tim.goto(x=-230, y=(-90 + y * 40))
        turtles_list.append(tim)


def create_finishline():
    """Draw the finishline."""
    finishline_colors = ["black", "#bdc3c7"]
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(230, -190)
    finish_line.pendown()
    finish_line.left(90)
    finish_line.width(8)
    position_y = finish_line.pos()[1]
    while position_y <= 200.0:
        for color in finishline_colors:
            finish_line.color(color)
            finish_line.forward(20)
        position_y = finish_line.pos()[1]


create_set_turtles()
create_finishline()
winner = ""
should_stop = False
while not should_stop:
    for turtle in turtles_list:  # Get the winner of the race.
        turtle_position = turtle.pos()
        # print(turtle_position[0])
        if turtle_position[0] >= 210.0:
            winner = turtle.pencolor()
            should_stop = True
            break
        else:  # Move the turtle forward randomly
            turtle.forward(random.randint(0, 10))

if user_bet == winner:
    print(f"You win!")
else:
    print(f"You lose!")

print(f"{winner.title()} is the winner.")
screen.exitonclick()
