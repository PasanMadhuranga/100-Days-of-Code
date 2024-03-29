import random
from turtle import *

ALIGNMENT = "center"
FONT = ('Courier', 50, 'bold')
USER_COLOR = "red"
COMPUTER_COLOR = "blue"
WIN_COLOR = "green"
LOSE_COLOR = "orange"
DRAW_COLOR = "brown"

# x and y coordinates of the starting positions of grid lines.
GRID_POSITIONS = [(-100, -300), (100, -300), (-300, -100), (-300, 100)]
ALL_CELLS = {1: (-300, -100, 300, 100), 2: (-100, 100, 300, 100), 3: (100, 300, 300, 100),
             4: (-300, -100, 100, -100), 5: (-100, 100, 100, -100), 6: (100, 300, 100, -100),
             7: (-300, -100, -100, -300), 8: (-100, 100, -100, -300), 9: (100, 300, -100, -300)}

# To win crosses or circles should be in one of the following 3 cells set.
WIN_PATTERNS = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]

screen = Screen()
screen.setup(600, 600)

# Create the 3 * 3 grid
grid_turtle = Turtle()
grid_turtle.hideturtle()
grid_turtle.left(90)
grid_turtle.width(4)
screen.tracer(0)
for i in range(len(GRID_POSITIONS)):
    if i > 1:
        grid_turtle.setheading(0)
    grid_turtle.penup()
    grid_turtle.goto(GRID_POSITIONS[i])
    grid_turtle.pendown()
    grid_turtle.forward(600)
screen.update()

empty_cells = {1: (-300, -100, 300, 100), 2: (-100, 100, 300, 100), 3: (100, 300, 300, 100),
               4: (-300, -100, 100, -100), 5: (-100, 100, 100, -100), 6: (100, 300, 100, -100),
               7: (-300, -100, -100, -300), 8: (-100, 100, -100, -300), 9: (100, 300, -100, -300)}
all_occupied_cells = {}
user_occupied_cells = {}
computer_occupied_cells = {}
finish_game = False


def final_result(final_text_color, final_text):
    """Show final result. Draw, Win or Lose."""
    global finish_game
    write_turtle = Turtle()
    write_turtle.hideturtle()
    write_turtle.color(final_text_color)
    write_turtle.write(arg=final_text, align=ALIGNMENT, font=FONT)
    finish_game = True


def check_who_win(occupied_cells: dict, final_color, final_txt):
    """After user and computer play check if someone wins or not.
    if user wins print 'You Win!'. if computer wins print 'You Lose'."""
    for pattern in WIN_PATTERNS:
        remaining_pattern_cells = list(set(pattern) - set(occupied_cells))
        if len(remaining_pattern_cells) == 0:
            final_result(final_color, final_txt)
            break


def place_computer_input(occupied_cells: dict) -> bool:
    """Place the computer input at the best position. If there is not any best positions return False."""
    for pattern in WIN_PATTERNS:
        remaining_pattern_cells = list(set(pattern) - set(occupied_cells))
        if len(remaining_pattern_cells) == 1:
            if remaining_pattern_cells[0] not in occupied_cells:
                draw_computer_input(remaining_pattern_cells[0])
                return True
    return False


def find_best_position():
    """Find the best position to place the computer input."""
    empty_cell_nums = [key for key in empty_cells]
    if len(user_occupied_cells) == 1:
        draw_computer_input(random.choice(empty_cell_nums))
    else:
        # computer_played = place_computer_input(computer_occupied_cells)
        computer_played = False
        # Check if there are any places to win computer. If any place the computer input there.
        if not computer_played:
            for pattern in WIN_PATTERNS:
                remaining_pattern_cells = list(set(pattern) - set(computer_occupied_cells))
                if len(remaining_pattern_cells) == 1:
                    if remaining_pattern_cells[0] not in user_occupied_cells:
                        draw_computer_input(remaining_pattern_cells[0])
                        computer_played = True
                        break

        if computer_played:
            check_who_win(computer_occupied_cells, final_color=LOSE_COLOR, final_txt="You Lose")

        if not finish_game:
            check_who_win(user_occupied_cells, final_color=WIN_COLOR, final_txt="You win!")

        # Check if there are any places to block user from winning. If any place the computer input there.
        if not finish_game:
            # computer_played = place_computer_input(user_occupied_cells)
            for pattern in WIN_PATTERNS:
                remaining_pattern_cells = list(set(pattern) - set(user_occupied_cells))
                if len(remaining_pattern_cells) == 1:
                    if remaining_pattern_cells[0] not in computer_occupied_cells:
                        draw_computer_input(remaining_pattern_cells[0])
                        computer_played = True
                        break

            # If there are no any places to win or block user from winning, Place the computer input at a random place.
            if not computer_played:
                draw_computer_input(random.choice(empty_cell_nums))

            # If 8 cells are occupied, Reserve the last empty cell to user.
            if len(all_occupied_cells) == 8:
                for cell_num, cell in empty_cells.items():
                    occupied_cell = empty_cells.pop(cell_num)
                    user_occupied_cells[cell_num] = occupied_cell
                    all_occupied_cells[cell_num] = occupied_cell
                    break

                check_who_win(user_occupied_cells, final_color="green", final_txt="You win!")

                # If all the cells are occupied and no one wins, print 'Draw'.
                if not finish_game:
                    final_result(DRAW_COLOR, "Draw")


def draw_user_input(x, y):
    """Draw a circle in the cell where user clicks."""
    global user_occupied_cells, all_occupied_cells, finish_game
    for cell_num, cell in empty_cells.items():
        # Find the user clicked cell and Get the correct position at that cell.
        if (cell[0] < x < cell[1]) and (cell[3] < y < cell[2]):
            new_x = (cell[0] + cell[1]) / 2
            new_y = (cell[2] + cell[3]) / 2 - 50

            # Draw a circle in that cell.
            user_turtle.penup()
            user_turtle.goto(new_x, new_y)
            user_turtle.pendown()
            user_turtle.circle(50)

            # remove that cell from the empty cells and add it to the user_occupied_cells and all_occupied_cells.
            occupied_cell = empty_cells.pop(cell_num)
            user_occupied_cells[cell_num] = occupied_cell
            all_occupied_cells[cell_num] = occupied_cell

            # After user place his input, place the computer input.
            find_best_position()
            break

    screen.update()


def draw_computer_input(cell_num: int):
    """Draw a cross in the cell where user clicks."""
    # Get the correct x and y coordinates for the given cell number
    new_x = (ALL_CELLS[cell_num][0] + ALL_CELLS[cell_num][1]) / 2 - 40
    new_y = (ALL_CELLS[cell_num][2] + ALL_CELLS[cell_num][3]) / 2 - 40

    # Draw a cross in that cell.
    computer_turtle.penup()
    computer_turtle.goto(new_x, new_y)
    computer_turtle.pendown()
    computer_turtle.setheading(45)
    computer_turtle.forward(113.14)
    new_x += 80
    computer_turtle.penup()
    computer_turtle.goto(new_x, new_y)
    computer_turtle.setheading(135)
    computer_turtle.pendown()
    computer_turtle.forward(113.14)

    # remove that cell from the empty cells and add it to the computer_occupied_cells and all_occupied_cells.
    occupied_cell = empty_cells.pop(cell_num)
    computer_occupied_cells[cell_num] = occupied_cell
    all_occupied_cells[cell_num] = occupied_cell
    screen.update()


# Create user turtle
user_turtle = Turtle()
user_turtle.hideturtle()
user_turtle.color(USER_COLOR)
user_turtle.width(4)

# Create computer turtle
computer_turtle = Turtle()
computer_turtle.hideturtle()
computer_turtle.color(COMPUTER_COLOR)
computer_turtle.width(4)

# Listen to the mouse clicks on the screen,
screen.onclick(draw_user_input)
screen.mainloop()

