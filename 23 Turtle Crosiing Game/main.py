import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_is_on = True
car_index = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a car every sixth time the loops runs.
    car_index += 1
    created_the_car = car_manager.create_car(car_index)
    if created_the_car:
        car_index = 0

    car_manager.move_cars()

    for car in car_manager.all_cars:  # Detect collisions with cars.
        if player.distance(car) <= 30:
            scoreboard.end_game()
            game_is_on = False

    if player.ycor() > 280:  # Reset the player position, increase the level and cars' speed when player reach the top.
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.exitonclick()
