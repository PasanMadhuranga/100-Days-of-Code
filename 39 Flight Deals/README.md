# Flight Deals

Flight Deals is a Python application that tracks flight prices for your chosen destinations and notifies you when the price falls below a certain threshold. It uses the Tequila API to search for flight data and a Google Sheet to manage the list of destinations and desired prices.

## Features

- Tracks flight prices for multiple destinations.
- Updates IATA codes in a Google Sheet.
- Sends an email notification for deals below a certain price.

## How It Works

1. The application first checks if the Google Sheet containing the destinations has IATA codes; if not, it populates them using the Tequila API.
2. It then checks the flight prices for the next six months and compares them with the desired prices listed in the Google Sheet.
3. If a flight price is found below the desired price, the application sends an email notification with the flight details.

## Usage

To use the application:

1. Clone the repository to your local machine.
2. Run `main.py` to start the application.
3. The application will automatically update the Google Sheet with IATA codes.
4. It will then check for flight deals and notify you via email if any are found.

## Customization

You can customize the Google Sheet with your desired destinations and price thresholds. The application will check the prices accordingly and send notifications for any matching deals.

## Requirements

- Python 3.x
- `requests` library
- Amadeus and Sheety API keys

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `requests` library using pip:
   ```
   pip install requests
   ```

## Project Structure

- `main.py`: Contains the main logic to initiate the application.
- `data_manager.py`: Contains logic to manage the Google Sheet data.
- `flight_search.py`: Contains logic to search for flight prices.
- `notification_manager.py`: Contains logic to send email notifications.

## Contributing

Contributions to the Flight Deals project are welcome. Please follow the standard fork, branch, and pull request workflow.

## Acknowledgments

- Tequila API for providing an extensive API to search for flight data.
- Sheety for providing a simple interface to manage Google Sheets data.

---

**Note**: This project is for educational purposes and is not intended for use in production.
