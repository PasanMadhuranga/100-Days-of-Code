import os
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


def compare_choices(user, computer):
    """Compare the choices and return the result. Win, Draw or Lose"""
    win = "You win"
    draw = "It's a draw."
    lose = "You Lose"
    if user == computer:
        return draw
    elif (user + 1) == computer:
        return lose
    elif (computer + 1) == user:
        return win
    elif user < computer:
        return win
    else:
        return lose


def start_game():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)

    try:
        result = compare_choices(user_choice, computer_choice)
        print(f"\nYou chose:{choices[user_choice]}\nComputer chose:{choices[computer_choice]}\n{result}")
    except IndexError:
        print("Invalid Input")
        start_game()

    want_to_play = input('\nDo you want to play again. Type "Yes" or "No".\n').lower()

    if want_to_play == "yes":
        os.system('cls')
        start_game()


start_game()
