# Hangman Game

## Introduction
The Hangman Game is an interactive Python implementation of the classic word-guessing game. Players try to guess a randomly selected word by suggesting letters within a certain number of guesses. This script brings the traditional hangman experience to the command line, complete with visual representations of the hangman as the game progresses.

## Features
- **Random Word Selection**: Words are randomly chosen from a predefined list.
- **Visual Hangman Stages**: Displays hangman's stages graphically as the player makes incorrect guesses.
- **Guess Tracking**: Keeps track of the player's guessed letters.
- **Win and Lose Conditions**: Indicates whether the player wins or loses, along with the correct word if lost.
- **Replayability**: Option to play again after each game.

## Requirements
- Python 3.x
- Additional modules: `hangman_art` for ASCII art, `hangman_words` for the word list.

## Installation
No specific installation is required other than having Python 3.x. Ensure that `hangman_art.py` and `hangman_words.py` are in the same directory as the main script.

## How to Play
1. **Run the Script**: Start the game by running the script in a Python environment.
2. **Guess Letters**: Input single letters to guess parts of the word.
3. **Keep Track of Lives**: The number of incorrect guesses is limited.
4. **View Hangman Stages**: The state of the hangman updates with each incorrect guess.
5. **Win or Lose**: The game ends when the player guesses the word or runs out of lives.
6. **Play Again**: After the game ends, choose to play another round or exit.

## Example Playthrough
```
[Hangman ASCII Art]
___
|   |
|   O
|  /|\
|  / \
|
-+-+-+-
Guess a letter: a
You have 5 lives left.
```
