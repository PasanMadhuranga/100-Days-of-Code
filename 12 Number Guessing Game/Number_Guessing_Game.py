import random

logo = """
 _____           _              _____                 _            _____               
|   | |_ _ _____| |_ ___ ___   |   __|_ _ ___ ___ ___|_|___ ___   |   __|___ _____ ___ 
| | | | | |     | . | -_|  _|  |  |  | | | -_|_ -|_ -| |   | . |  |  |  | .'|     | -_|
|_|___|___|_|_|_|___|___|_|    |_____|___|___|___|___|_|_|_|_  |  |_____|__,|_|_|_|___|
                                                           |___|                       
"""
print(logo)
CHOSEN_NUMBEER = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'easy':
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts to guess the number.")

def check(guess):
    """Check whether the gussed number is equal, greater than or less than to the chosen number."""
    global CHOSEN_NUMBEER
    global attempts
    if guess == CHOSEN_NUMBEER:
        attempts = -1
        return f"You got it. The answer is {guess}."
    elif guess > CHOSEN_NUMBEER:
        attempts -= 1
        return "Too High."
    else:
        attempts -= 1
        return "Too Low."


while attempts > 0: # Get inputs until attempts are over
    guessed_number = int(input("Make a guess: "))
    result = check(guessed_number)
    print(result)
    if attempts > 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.\n")

if attempts == 0:
    print(f"You've run out of guesses, you lose. The number is {CHOSEN_NUMBEER}")

