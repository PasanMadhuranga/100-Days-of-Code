import time
import pygame

letters_to_morse_dict = {
    "A": "• —",
    "B": "— • • •",
    "C": "— • — •",
    "D": "— • •",
    "E": "•",
    "F": "• • — •",
    "G": "— — •",
    "H": "• • • •",
    "I": "• •",
    "J": "• — — —",
    "K": "— • —",
    "L": "• — • •",
    "M": "— —",
    "N": "— •",
    "O": "— — —",
    "P": "• — — •",
    "Q": "— — • —",
    "R": "• — •",
    "S": "• • •",
    "T": "—",
    "U": "• • —",
    "V": "• • • —",
    "W": "• — —",
    "X": "— • • —",
    "Y": "— • — —",
    "Z": "— — • •",
    "0": "— — — — —",
    "1": "• — — — —",
    "2": "• • — — —",
    "3": "• • • — —",
    "4": "• • • • —",
    "5": "• • • • •",
    "6": "— • • • •",
    "7": "— — • • •",
    "8": "— — — • •",
    "9": "— — — — •",
}


def play_mp3(filename: str):
    """Play the given mp3 file."""
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def morse_code_converter(text):
    """Convert the given text to morse code. Then play and return the morse code"""
    words_in_text = text.upper().split()
    morse = ""
    for word in words_in_text:
        for letter in list(word):
            morse += letters_to_morse_dict[letter] + "   "
            morse_list = letters_to_morse_dict[letter].split(" ")
            for char in morse_list:
                if char == "•":
                    play_mp3("dit.mp3")
                elif char == "—":
                    play_mp3("dah.mp3")
                time.sleep(0.1)
            time.sleep(0.3)
        morse += "       "
        time.sleep(0.7)

    return morse[:-10]


morse_code = morse_code_converter(input("Input the sentence you want to convert to morse code:\n"))
print(morse_code)
