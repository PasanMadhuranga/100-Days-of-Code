# Find Rental Places

The "Find Rental Places" project is a Python script that scrapes rental property data from Zillow and then automates the process of filling in a Google form with the rental information.

## Features

- Web scraping with BeautifulSoup to extract rental property data.
- Browser automation with Selenium to input data into a Google Form.
- Collection of rental properties' addresses, prices, and links.

## How It Works

1. The script makes a GET request to Zillow's rental properties page and collects the HTML content.
2. Using BeautifulSoup, it parses the HTML content to extract the relevant information (prices, addresses, and URLs).
3. The script utilizes Selenium with Chrome WebDriver to fill a Google Form with the extracted data for each property.

## Usage

To use the script:

1. Set the `rental_places_url` to the Zillow page containing the rental listings.
2. Replace the `google_form_url` with the URL of your Google Form.
3. Replace `chrome_driver_path` with the path to your ChromeDriver.
4. Run `main.py`.

## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library
- `selenium` library
- ChromeDriver

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip:
   ```
   pip install requests beautifulsoup4 selenium
   ```
3. Download ChromeDriver and note the path to its executable.

## Project Structure

- `main.py`: Contains the script to scrape Zillow and fill out the Google Form.

## Contributing

Contributions are welcome. If you would like to contribute to the project, please make sure to:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to your branch.
5. Create a new Pull Request.

## Disclaimer

This script is for educational purposes only. Always make sure to comply with Zillow's terms of service when scraping their website. Do not scrape their website excessively or in a way that disrupts their services.
