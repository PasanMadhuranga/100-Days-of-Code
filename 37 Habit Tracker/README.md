# Habit Tracker

Habit Tracker is a Python application that interacts with the [Pixela](https://pixe.la/) web service to track your daily habits. This application allows you to create a user, generate a graph to track a particular habit, and add or update data points to your habit graph.

## Features

- User creation with terms of service agreement.
- Graph creation for habit tracking.
- Addition of new data points (pixels) to the graph.
- Update and deletion of existing data points.

## How It Works

1. **User Creation**: A POST request is sent to create a new user with a unique token, username, and agreement to the terms of service.
2. **Graph Creation**: A new graph is created with a unique ID, name, unit of measure, type, and color.
3. **Add New Pixel**: The user can add a new pixel to the graph representing the completion of the habit for the day.
4. **Update Pixel**: Existing pixels can be updated with new values.
5. **Delete Pixel**: Pixels can also be deleted if entered incorrectly.

## Usage

To use the application:

1. Clone the repository to your local machine.
2. Run `main.py` to start interacting with the application.
3. Follow the command-line prompts to track your habits.

## Customization

You can customize the habit you want to track by modifying the graph configuration in `main.py`. You can also set the date for which you want to track or update a habit.

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

- `main.py`: Contains the main script to run the Habit Tracker.
- `USERNAME`: Your username on Pixela.
- `TOKEN`: Your unique and secure token for the Pixela API.
- `GRAPH_ID`: The ID of your habit tracking graph.

## Contributing

Contributions to the Habit Tracker project are welcome. Please follow the standard fork, branch, and pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Pixela for providing a simple and powerful API for habit tracking.

---

**Note**: This project is for educational purposes and is not intended for use in production.
