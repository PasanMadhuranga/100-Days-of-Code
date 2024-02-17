import turtle
import pandas


def name_state():
    """Put the player's guess on to the map."""
    state_data = data[data["state"] == answer_state]
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.goto(int(state_data.x), int(state_data.y))
    state_name.write(answer_state)
    # Method 2 -> state_name.write(state_data.state.item())


def missing_states():
    """Create a csv file which contains all the missing states."""
    # missed_states = [state for state in all_states if state not in correct_guesses]
    # new_data = pandas.DataFrame(missed_states)
    # new_data.to_csv("states_to_learn.csv")

    missed_data = data[~data["state"].isin(correct_guesses)]
    missed_data.to_csv("states_to_learn.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_guesses = []

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states()
        break

    if answer_state in all_states:  # Check whether answer is a state or not. And if a state put the answer on the map.
        correct_guesses.append(answer_state)
        name_state()


