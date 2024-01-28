# import colorgram
#
# colors = colorgram.extract('Damien Hist.jpg', 35)
# rgb_colors = []
# for color in colors:
#     r, g, b = color.rgb[0], color.rgb[1], color.rgb[2]
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
import math
import random
from turtle import Turtle, Screen

colors = [(222, 76, 57), (223, 145, 77), (39, 93, 150), (22, 27, 40), (218, 62, 82), (234, 220, 94), (42, 19, 13),
          (151, 63, 95), (40, 21, 29), (108, 169, 204), (154, 65, 54), (26, 135, 91), (73, 167, 91), (196, 134, 162),
          (238, 221, 7), (117, 183, 135), (163, 181, 48), (96, 45, 73), (233, 166, 182), (16, 40, 27), (22, 171, 207),
          (54, 55, 102), (110, 43, 38), (236, 173, 156), (165, 211, 193), (148, 209, 224), (98, 123, 169), (82, 64, 27),
          (31, 83, 48), (177, 187, 214), (11, 89, 112)]
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.setpos(-250, -250)
turtle.pendown()
turtle.speed(0)


def move_the_turtle(direction, pixels):
    "Move the turtle to the given direction by given pixels."
    turtle.penup()
    if direction == "x":
        turtle.setx(-250 + pixels * 40)
    else:
        turtle.sety(-250 + pixels * 40)
    turtle.pendown()


def create_damien_hist(num_of_dots):
    lines = int(math.sqrt(num_of_dots))
    for pixels_y in range(0, lines):
        move_the_turtle("y", pixels_y)
        for pixels_x in range(0, lines):
            move_the_turtle("x", pixels_x)
            turtle.dot(20, random.choice(colors))


create_damien_hist(169)

screen.exitonclick()
