import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        """Create a random car along the right edge of the screen"""
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self, index):
        """Create a car add it into the car list."""
        if index == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
            return True
        return False

    def move_cars(self):
        """Move the car -x direction."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Increase the moving speed of the car."""
        self.car_speed += MOVE_INCREMENT
