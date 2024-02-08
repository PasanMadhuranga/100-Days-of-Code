from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        """Create the scoreboard."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        """Show score on the scoreboard."""
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def update_l_score(self):
        self.l_score += 1
        self.show_score()

    def update_r_score(self):
        self.r_score += 1
        self.show_score()