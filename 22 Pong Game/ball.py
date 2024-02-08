from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        """Move the ball up right corner."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.x_move *= -1


