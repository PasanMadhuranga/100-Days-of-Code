############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
import os
import random


def change_ace(chosen_cards):
    """Change Ace value to 1 if score > 20"""
    score = sum(chosen_cards)
    if 11 in chosen_cards and score > 20:
        chosen_cards[chosen_cards.index(11)] = 1
    return chosen_cards


def add_new_card(hand):
    """Add a new card to the hand."""
    new_card = random.choice(cards)
    if new_card == 11 and (sum(hand) + 11) > 20:
        hand.append(1)
    else:
        hand.append(new_card)
    return hand


def computer_hand():
    """Prepare computer's hand."""
    computer_hand = change_ace([random.choice(cards), random.choice(cards)])
    while sum(computer_hand) < 17:
        computer_hand = add_new_card(computer_hand)
    return computer_hand


def print_cards(user_cards, computer_cards):
    """Print cards and scores."""
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")


def final_print_cards(user_cards, computer_cards):
    """Print final hands, score and win/lose."""
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score > 20:
        print("You went over. You Loose")
    elif computer_score > 20:
        print("Opponent went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score == computer_score:
        print("Draw")
    else:
        print("You Loose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    os.system("cls")
    user_cards = change_ace([random.choice(cards), random.choice(cards)])
    computer_cards = computer_hand()
    print_cards(user_cards, computer_cards)
    want_another_card = "y"
    while want_another_card != "n":
        want_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if want_another_card == "y":
            user_cards = add_new_card(user_cards)
            print_cards(user_cards, computer_cards)
            if sum(user_cards) > 20:
                final_print_cards(user_cards, computer_cards)
                want_another_card = "n"
        else:
            final_print_cards(user_cards, computer_cards)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != "n":
    # clear()
    play_game()

print("Good Bye!")
