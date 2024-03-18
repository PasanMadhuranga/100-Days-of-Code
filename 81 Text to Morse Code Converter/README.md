# Text to Morse Code Converter

"Text to Morse Code Converter" is a Python script that converts alphanumeric text to Morse code and plays the corresponding sound using `pygame`.

## Features

- Converts letters and numbers to Morse code.
- Plays sound for each Morse code character.
- Supports a pause between characters and words to simulate real Morse code transmission.

## Requirements

- Python
- Pygame module for Python

## Installation

1. Ensure you have Python installed on your system.
2. Install Pygame using pip:

```sh
pip install pygame
```

## Usage

1. Run the script using Python in your terminal:

```sh
python text_to_morse_code_converter.py
```

2. When prompted, input the text you want to convert to Morse code.
3. The script will output the Morse code and play the corresponding sounds.

## Project Structure

- `text_to_morse_code_converter.py`: The main script that includes the converter and sound player.
- `dit.mp3`: Audio file for the Morse code "dit" sound.
- `dah.mp3`: Audio file for the Morse code "dah" sound.

## How It Works

The script uses a dictionary mapping each letter and number to its Morse code representation. For each character in the input text, the script plays the appropriate sound and pauses to accurately represent Morse code timing.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit and push your changes.
4. Create a pull request.

## Acknowledgments

- Morse code character mappings are based on the international Morse code standards.

