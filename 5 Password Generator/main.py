import random
import string
import os
import time


def password_generator():
    """Generate a password according to user inputted num of letters, symbols and numbers."""
    try:
        num_of_letters = int(input("How many letters would you like in your password?\n"))
        num_of_symbols = int(input("How many symbols would you like in your password?\n"))
        num_of_numbers = int(input("How many numbers would you like in your password?\n"))

        password = []
        password += [random.choice(string.ascii_letters) for _ in range(num_of_letters)]
        password += [random.choice(string.punctuation) for _ in range(num_of_symbols)]
        password += [random.choice(string.digits) for _ in range(num_of_numbers)]

        random.shuffle(password)
        final_password = ''.join(password)
        print(f"Here is your password: {final_password}")

    except ValueError:
        print("Invalid Input")
        time.sleep(0.7)
        os.system("cls")
        password_generator()


password_generator()
