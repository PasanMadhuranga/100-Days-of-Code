# Guess the Number Game

"Guess the Number Game" is a web application built with Flask that challenges the user to guess the correct number.

## Features

- A simple Flask route to accept guesses.
- Dynamic responses based on user input.
- Fun and interactive GIFs that respond to each guess.

## How It Works

- The application generates a random number between 0 and 9.
- The user is prompted to guess a number within the range.
- The server processes the guess and provides feedback through a web page.

## Requirements

- Python
- Flask

## Installation

1. Ensure Python is installed on your system.
2. Install Flask using pip:

```sh
pip install Flask
```

## Running the Application

To run the application, execute the following command in your terminal:

```sh
python main.py
```

The server will start, and you can access the application by navigating to `localhost:5000` in your web browser.

## Usage

- Visit the main page and read the instructions.
- Type in your guess in the URL (e.g., `localhost:5000/5`).
- The page will tell you whether your guess is too high, too low, or correct.

## Project Structure

- `main.py`: The Flask application with all the routes and game logic.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Clone your forked repository.
3. Make changes and test them.
4. Submit a pull request.

## Screenshot

![Guess the number game](screenshots/home.png)

_The screenshot shows the main interface of the "Guess the Number Game" with an example guess._
