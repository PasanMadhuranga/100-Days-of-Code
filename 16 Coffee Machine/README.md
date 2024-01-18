# Coffee Machine

## Introduction
The "Coffee Machine" script is a Python-based simulation of a coffee vending machine. This interactive program allows users to order different types of coffee, handle transactions, and manage the machine's resources. It provides a simple yet effective demonstration of object-oriented programming and file handling in Python.

## Features
- **Multiple Coffee Choices**: Offers a selection of espresso, latte, and cappuccino.
- **Dynamic Resource Management**: Tracks and updates the machine's resources like water, milk, and coffee.
- **Transaction Handling**: Processes coin payments and calculates change.
- **Resource and Profit Reporting**: Generates reports on current resources and total profit.
- **File-Based Data Storage**: Utilizes text files (`profit.txt` and `resources.txt`) to persistently store machine data.

## Requirements
- Python 3.x
- Text files: `profit.txt` and `resources.txt` for storing machine data.

## Installation
Ensure Python 3.x is installed on your system. Place `profit.txt` and `resources.txt` in the same directory as the scripts.

## How to Use
1. **Run the Main Script**: Start the Coffee Machine program.
2. **Select a Coffee**: Choose from the available coffee options displayed.
3. **Insert Coins**: Follow the prompts to insert coins for payment.
4. **Receive Coffee and Change**: The machine dispenses the selected coffee and returns change if applicable.
5. **Resource and Profit Reports**: Access reports on current resources and profits.
6. **Refill Resources**: Update `resources.txt` to refill machine resources.

## File Structure
- `menu.py`: Defines the `Menu` and `MenuItem` classes for coffee options.
- `coffee_maker.py`: Contains the `CoffeeMaker` class for managing coffee making and resources.
- `money_machine.py`: Includes the `MoneyMachine` class for handling transactions.
- `profit.txt`: Stores the total profit of the machine.
- `resources.txt`: Keeps track of the machine's current resources.

## Example Use
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 
...
```

## Contributing
Contributions are welcome, particularly in expanding the menu options, enhancing the user interface, or optimizing the resource management system. Please ensure that your code is well-documented and tested.

