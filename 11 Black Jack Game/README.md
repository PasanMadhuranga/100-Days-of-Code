# Black Jack Game

## Introduction
The 11 Black Jack Game is a Python implementation of the classic card game Blackjack. This script offers a virtual Blackjack experience where the player competes against a computer dealer. The game follows standard Blackjack rules and is designed for a single player.

## Features
- **Standard Blackjack Rules**: Incorporates the basic rules of Blackjack, including card values and dealer behavior.
- **Dynamic Ace Values**: Handles the Ace card's variable value (either 1 or 11) based on the player's current hand.
- **User Choice for Card Drawing**: Players can choose to draw another card or hold their current hand.
- **Computer Dealer Logic**: The computer dealer automatically draws cards following standard Blackjack guidelines.
- **Clear Game Display**: Outputs the player's and dealer's hands and scores for easy tracking.

## Requirements
- Python 3.x

## Installation
No specific installation required. Ensure Python 3.x is installed on your system.

## How to Play
1. **Start the Game**: Run the script to initiate the game.
2. **View Initial Hand**: Review your initial two cards and the dealer's first card.
3. **Choose to Hit or Stand**: Decide whether to draw another card ('y') or hold your hand ('n').
4. **End of Round**: The game automatically ends the round when the player stands or exceeds 21 points.
5. **View Results**: The final hands are displayed along with the game outcome (win, lose, or draw).
6. **Play Again Option**: Choose to start a new game or exit after each round.

## Example Playthrough
```
Do you want to play a game of Blackjack? Type 'y' or 'n': y
Your cards: [10, 5], current score: 15
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: n
Your final hand: [10, 5], final score: 15
Computer's final hand: [8, 10], final score: 18
You Loose
```

## Contributing
Contributions to enhance the game, such as adding multiplayer functionality, graphical interface, or advanced dealer AI, are welcome. Please ensure that you update tests as appropriate.
