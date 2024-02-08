from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """Create the paddle."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def up(self):
        """Move the paddle up by 20 pixels."""
        new_y_coordinate = self.ycor() + 20
        if new_y_coordinate < 280:
            self.sety(new_y_coordinate)

    def down(self):
        """Move the paddle down by 20 pixels."""
        new_y_coordinate = self.ycor() - 20
        if new_y_coordinate > -280:
            self.sety(new_y_coordinate)
