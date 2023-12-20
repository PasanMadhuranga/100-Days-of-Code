import os
import time

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser_cipher():
    """start the Caesar Cipher."""

    def code_the_msg(msg, shift_num):
        """Encode or Decode the given msg."""
        final_msg = []
        for char in list(msg):
            temp_char = char.lower()
            if temp_char in alphabet:
                encoded_letter = alphabet[alphabet.index(temp_char) + shift_num]
                if char.isupper():
                    encoded_letter = encoded_letter.upper()
                final_msg.append(encoded_letter)
            else:
                final_msg.append(char)

        return "".join(final_msg)

    while True:
        try:  # Get user inputs: encode or decode, msg and shift number
            os.system("cls")
            print(logo)
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n")) % 26

            if direction == "encode":
                shift = abs(shift)
            elif direction == "decode":
                shift = -shift
            else:
                print("Please enter valid inputs.")
                time.sleep(1)
                continue
            break
        except:  # If user inputs invalid inputs run again.
            print("Please enter valid inputs.")
            time.sleep(1)

    print(code_the_msg(text, shift))

    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if go_again == "yes":
        caeser_cipher()


caeser_cipher()
