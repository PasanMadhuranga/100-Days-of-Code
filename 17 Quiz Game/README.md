# Quiz Game

## Introduction
The "Quiz Game" is a Python-based trivia game that tests the player's knowledge with a series of true or false questions. This interactive game is designed to challenge players with various questions and keeps track of the player's score as they progress through the quiz.

## Features
- **True or False Questions**: A series of questions that require a simple true or false response.
- **Score Tracking**: Keeps track of the player's correct answers and displays the score after each question.
- **Dynamic Questioning**: Automatically moves to the next question after each answer.
- **End-of-Game Summary**: Provides a final score and concludes the quiz when all questions are answered.

## Requirements
- Python 3.x

## Installation
No specific installation is required other than having Python 3.x on your system. The game consists of multiple Python files (`data.py`, `question_model.py`, `quiz_brain.py`, and `main.py`) which need to be in the same directory.

## How to Play
1. **Start the Game**: Run `main.py` to begin the quiz.
2. **Answer Questions**: Respond with 'True' or 'False' to each prompted question.
3. **View Feedback**: After each answer, see if you were correct and what your current score is.
4. **Complete the Quiz**: Continue until all questions have been answered.
5. **See Your Final Score**: At the end of the quiz, your final score will be displayed.

## File Structure
- `data.py`: Contains the question dataset.
- `question_model.py`: Defines the `QuestionModel` class, handling question creation and score tracking.
- `quiz_brain.py`: Contains the `Question` class, defining the structure of a quiz question.
- `main.py`: The main script to run the quiz game.

## Example Use
```
Welcome to Quiz Game!!!
Q1. A slug's blood is green. (True/False)
> True
You got it right!
Your current score is: 1/1
...
```

## Contributing
Contributions such as adding more questions, creating different difficulty levels, or enhancing the user interface are welcome. Please ensure your code is well-documented and tested.
