from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.create_margin()

    def create_margin(self):
        self.goto(-300, 265)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(0, 270)

    def update_scoreboard(self):
        """Show score on the scoreboard."""
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.create_margin()

    def increase_score(self):
        """When snake eats the food, add 1 point to the score."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Update the high score and set the score to 0."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """Print Game Over at the middle of the screen."""
        self.goto(0, 0)
        self.write(arg="Game Over!!!", align=ALIGNMENT, font=FONT)
        self.goto(0, 270)
