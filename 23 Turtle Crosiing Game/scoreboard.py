from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.level = 1
        self.show_level()

    def show_level(self):
        """Show the current level."""
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()

    def end_game(self):
        """Show 'GAME OVER' on the screen."""
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER", align="center", font=FONT)
        

