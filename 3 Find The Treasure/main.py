import os

steps = [
    {
        "Q": 'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n',
        "R": "left",
        "W": ["right", "Fall into a hole."],
    },
    {
        "Q": 'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type '
             '"swim" to swim across.\n',
        "R": "wait",
        "W": ["swim", "Attacked by trout."],
    },
    {
        "Q": 'You met a giant bear. Type "fight" to fight with it. Type "climb" to climb to a tree.\n',
        "R": "climb",
        "W": ["fight", "Oh no! The bear killed you."]
    }
]


def start_game():
    """Start the game."""
    stop_game = False

    def check_answer(question, user_answer, right_answer, wrong_answer):
        """Check the user answer and return whether it is right, wrong or invalid."""
        if user_answer == right_answer:
            return True
        elif user_answer == wrong_answer:
            return False
        else:
            print("Invalid input")
            user_answer = input(question)
            return check_answer(question, user_answer, right_answer, wrong_answer)

    def play_again():
        """Ask the user whether they want to play again or not. if they want then restart the game."""
        is_play_again = input('Do you want to play again? Type "Yes" or "No"\n').lower()
        if is_play_again == "no":
            return None
        elif is_play_again == "yes":
            os.system('cls')
            start_game()
        else:
            print("Invalid input")
            play_again()

    def final_step():
        """Final Step of the Game."""
        final_decision = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow "
                               "and one blue. Which color do you choose?\n").lower()

        if final_decision == "red":
            print("Burned by fire.\nGame Over!")
        elif final_decision == "blue":
            print("Eaten by beasts.\nGame Over")
        elif final_decision == "yellow":
            print("You Win!!!")
        else:
            print("Invalid input")
            final_step()

    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    for step in steps:
        # Ask the questions step by step and check the user's answer.
        user_decision = input(step["Q"]).lower()
        is_correct = check_answer(question=step["Q"],
                                  user_answer=user_decision,
                                  right_answer=step["R"],
                                  wrong_answer=step["W"][0])
        if not is_correct:
            print(f'{step["W"][1]}\nGame Over!')
            if not play_again():
                stop_game = True
                break

    if not stop_game:
        final_step()


start_game()
