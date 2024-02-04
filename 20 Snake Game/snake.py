from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        """Create a snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add parts to the snake."""
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_list.append(snake_part)

    def extend(self):
        """Extend the snake by one square."""
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        """Move the snake."""
        for snake_part_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_part_num - 1].xcor()
            new_y = self.snake_list[snake_part_num - 1].ycor()
            self.snake_list[snake_part_num].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def reset_snake(self):
        """Remove the dead snake and create a new snake on the position (0,0)."""
        for snake_part in self.snake_list:
            snake_part.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
