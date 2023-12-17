import os
import random
import time
from hangman_art import stages, logo
from hangman_words import word_list


def start_game():
    """Start the hangman Game."""
    def want_to_play_again():
        """Ask the user whether he wants to play again or not."""
        play_again = input('Do you want to play again? Type "yes" or "no".\n').lower()
        if play_again == "yes":
            return True
        else:
            return False

    num_of_lives_left = 6
    chosen_word = random.choice(word_list)
    filled_word = ["_" for _ in range(len(chosen_word))]
    user_guesses = []
    while True:
        os.system("cls")
        # print(chosen_word) <- uncomment to test
        print(logo)
        print(stages[num_of_lives_left])
        print(" ".join(filled_word))

        if "_" not in filled_word: # If word is complete, ask user does he want to play again.
            print("You win!!!")
            if want_to_play_again():
                start_game()
            else:
                break

        elif not num_of_lives_left:  # If user is out of lives, Asks him whether he wants to play again or not.
            print("You are out of your lives.\nGame Over!!!")
            print(f"Word is: {chosen_word}\n")
            if want_to_play_again():
                start_game()
            else:
                break

        print(f"You have {num_of_lives_left} lives left.")
        guess = input("Guess a letter: ").lower()

        if guess in user_guesses:  # Check Whether user guessed that letter earlier or not.
            print("You've already guessed that letter.")
            time.sleep(1)
            continue
        elif guess in chosen_word:  # if guessed letter is in the word, Fill the word with user's guess.
            list_chosen_word = list(chosen_word)
            for index in range(len(list_chosen_word)):
                if guess == list_chosen_word[index]:
                    filled_word[index] = guess
        else:  # if guessed letter is not in the word, reduce number of lives.
            print("The letter you chose isn't in the word")
            num_of_lives_left -= 1
            time.sleep(1)

        user_guesses.append(guess)


start_game()
