from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Create a turtle player that starts at the bottom of the screen"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Move the turtle north."""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """Move the turtle south."""
        self.backward(MOVE_DISTANCE)

    def reset_position(self):
        """Move the turtle to starting position."""
        self.goto(STARTING_POSITION)
