# Amazon Price Tracker

Amazon Price Tracker is a Python script that helps you track the price of a specific product on Amazon. When the price drops below a target price, the script will send you an email notification.

## Features

- Price tracking for a specific Amazon product.
- Email alerts when the product price falls below the target.

## How It Works

1. The script takes an Amazon product URL and a target price as input.
2. It sends a request to Amazon to retrieve the current price of the product.
3. If the current price is less than the target price, it sends an email alert.

## Usage

To use the script:

1. Replace `self.amazon_url` with the URL of the Amazon product you want to track.
2. Set the `TARGET_PRICE` to your desired price point.
3. Replace `MY_EMAIL` and `MY_PASSWORD` with your email and a password or app-specific password.
4. Run `main.py`.

## Requirements

- Python 3
- `requests` library
- `lxml` library
- `beautifulsoup4` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip:
   ```
   pip install requests lxml beautifulsoup4
   ```
3. Configure your email credentials within the script.

## Project Structure

- `main.py`: The main script that initializes the price tracking process.

## Contributing

Contributions to improve the Amazon Price Tracker are welcome. Please ensure to follow good coding practices and submit pull requests for any enhancements.

### License

This project is released under the MIT License.

## Acknowledgments

- Amazon for providing product details and pricing.
- BeautifulSoup and requests libraries for enabling web scraping capabilities.

---

**Note**: This project is intended for educational purposes only, and should not be used to violate Amazon's Terms of Service or pricing policies.
