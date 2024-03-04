# My Workouts

My Workouts is a Python application that tracks your physical activities and posts them to a Google Sheet for easy tracking and visualization. The application utilizes the Nutritionix API to determine the exercise details from a simple text input and then uploads the activity data to a Google Sheet using the Sheety API.

## Features

- Natural language processing of exercise input.
- Calculation of exercise duration and calories burned.
- Automatic posting of workout data to a Google Sheet.

## How It Works

1. The user provides a description of the exercises they performed in natural language.
2. The application sends this data to the Nutritionix API, which returns detailed information about each exercise, including the name, duration, and calories burned.
3. The application then formats this data and sends it to a Google Sheet using the Sheety API, along with the current date and time.

## Usage

To use the application:

1. Clone the repository to your local machine.
2. Run `main.py` to start the application.
3. Input your exercises in natural language when prompted.
4. Check your Google Sheet to see your workouts logged with details.

## Customization

You can customize the types of exercises and the user's personal information such as gender, weight, height, and age within the `user_params` variable in `main.py`.

## Requirements

- Python 3
- `requests` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `requests` library using pip:
   ```
   pip install requests
   ```

## Project Structure

- `main.py`: Contains the main script to run the My Workouts application.
- `APP_ID` and `API_KEY`: Your unique identifiers for the Nutritionix API.
- `AUTHENTICATION`: Your encoded authentication key for the Sheety API.

## Contributing

Contributions to the My Workouts project are welcome. Please follow the standard fork, branch, and pull request workflow.

## Acknowledgments

- Nutritionix for providing an API to analyze and retrieve detailed exercise data.
- Sheety for providing a convenient API to manage Google Sheets data.

---

**Note**: This project is for educational purposes and is not intended for use in production.
