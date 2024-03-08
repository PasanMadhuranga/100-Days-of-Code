# Music Time Machine

The Music Time Machine is a Python application that allows you to travel back in time and rediscover the top 100 songs from a specific date on the Billboard Hot 100 chart. It uses BeautifulSoup to scrape song data from the Billboard website and the Spotify Web API to create a Spotify playlist including all 100 songs from that date.

## Features

- Input a date in the past.
- Scrape Billboard's website for the top 100 songs on that date.
- Create a Spotify playlist with those 100 songs.

## How It Works

1. The user inputs a date in the format `YYYY-MM-DD`.
2. The program scrapes Billboard's Hot 100 chart for the top 100 songs on that date.
3. It then uses the Spotify API to search for those songs and creates a playlist in the user's Spotify account.

## Usage

To use the application:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Run `main.py` and follow the on-screen prompt to input the date.
4. Log in to your Spotify account when prompted.
5. The application will create a Spotify playlist titled "Top 100 songs on [date]".

## Customization

You can modify the `main.py` file to change the Spotify playlist name and description or to search for songs from different charts or sources.

## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library
- `spotipy` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip:
   ```
   pip install requests beautifulsoup4 spotipy
   ```
3. Set up the Spotify API credentials as environment variables or directly in the script.

## Project Structure

- `main.py`: The main script to run the application.
- `TopSongs` class: Contains all the methods to scrape the Billboard website and interact with the Spotify API.

## Contributing

Contributions to the Music Time Machine project are welcome. Please follow the standard fork, branch, and pull request workflow.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Billboard for providing the chart data.
- Spotify for the Web API to interact with Spotify's data.

---

**Note**: This project is for educational purposes and is not intended for commercial use.
