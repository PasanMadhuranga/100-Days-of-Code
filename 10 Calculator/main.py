import os
import time
from art import logo


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}


def clear():
    """Clear the screen and print the logo."""
    time.sleep(1)
    os.system("cls")
    print(logo)


def calculator():
    should_continue = "y"
    print(logo)
    while True:  # Get the first number
        try:
            first_num = float(input("What's the first number?: "))
            break
        except ValueError:
            print("Please enter a valid number")
            clear()

    while should_continue == "y":
        while True:  # Get the operation
            try:
                print("+\n-\n*\n/")
                operation = input("Pick an operation: ")
                calculation = operations[operation]
                break
            except KeyError:
                print("Invalid Operation.")
                clear()

        while True:
            try:  # Get the second number
                second_number = float(input("What's the second number?: "))

                try:  # Do the calculation
                    result = calculation(first_num, second_number)
                    print(f"{first_num} {operation} {second_number} = {result}")
                    should_continue = input(
                        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new "
                        f"calculation: ")
                    first_num = result
                except KeyError:
                    print("Invalid Operation")
                    clear()
                except ZeroDivisionError:
                    print("Math Error")
                    time.sleep(1)
                    os.system("cls")
                    calculator()
                break
            except ValueError:
                print("Please enter a valid number")
                clear()

        os.system("cls")
        print(logo)

    os.system("cls")
    calculator()


calculator()
