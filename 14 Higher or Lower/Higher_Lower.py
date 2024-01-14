import random
import art
from Game_data import data
import os


def print_to_console_return_count(selected_one, letter):
    """Print the chosen one to the console. 
    'Compare A/B: name, description, from country.'
    And return their follower count."""
    name = selected_one["name"]
    description = selected_one["description"]
    country = selected_one["country"]
    print(f"Compare {letter}: {name}, a {description}, from {country}.")
    return selected_one["follower_count"]


def print_results(count_A, count_B):
    """Print if user won and repeat again."""
    global score
    score += 1
    os.system("cls")
    print(art.logo)
    print(f"You are right! Current score: {score}")
    recursion()


def recursion():
    global A
    count_A = print_to_console_return_count(A, "A")
    print(art.vs)
    B = random.choice(data)
    data.remove(B)
    count_B = print_to_console_return_count(B, "B")
    user_desicion = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user_desicion == 'A' and count_A > count_B:
        print_results(count_A, count_B)
    elif user_desicion == 'B' and count_B > count_A:
        A = B
        print_results(count_A, count_B)
    else:
        print(f"Sorry that's wrong. Final score: {score} A:{count_A} B:{count_B}")


print(art.logo)
score = 0
A = random.choice(data)
data.remove(A)
recursion()
