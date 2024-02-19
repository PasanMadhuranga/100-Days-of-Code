# NATO Alphabet

## Introduction
The "NATO Alphabet" project is a Python script designed to convert each letter of a user-inputted word into its corresponding NATO phonetic alphabet code. It leverages a CSV file containing the standard NATO phonetic alphabet and provides an interactive experience for the user to learn and use the phonetic codes.

## Features
- **User Input Conversion**: Converts any word entered by the user into its NATO phonetic equivalent.
- **Data Validation**: Ensures that only alphabetical characters are processed and prompts the user again if there are any non-alphabetic characters.
- **CSV Data Integration**: Utilizes a CSV file as the data source for the NATO phonetic alphabet.
- **Error Handling**: Gracefully handles incorrect inputs by using exception handling and recursion.

## Requirements
- Python 3.x
- Pandas Library

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install Pandas if not already available using `pip install pandas`.

## How to Use
1. **Start the Script**: Run `main.py` in your Python environment.
2. **Enter a Word**: Type a word when prompted.
3. **View NATO Phonetic Output**: The script will output the NATO phonetic codes corresponding to each letter of the inputted word.
4. **Handle Errors**: If non-alphabetic characters are entered, the script will prompt the user to try again.

## File Structure
- `main.py`: Contains the main script with the logic for user interaction and conversion.
- `nato_phonetic_alphabet.csv`: A CSV file containing the mapping of letters to their NATO phonetic codes.

## Contributing
Contributions are welcome to enhance the project by adding features like a graphical user interface, extended input validation, or support for non-English alphabets. Please make sure to provide test cases and documentation for your contributions.

