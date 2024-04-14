from tkinter import *
from tkinter import messagebox

import requests

BACKGROUND_COLOR = "#ffeaa7"
FONT = "Ariel"
TITLE_COLOR = "#663300"
HIGHLIGHT_COLOR = "#C4E538"
INSTRUCTION_COLOR = "#b71540"

# Get 70 random English words.
response = requests.get(url="https://random-word-api.herokuapp.com/word?number=70")
response.raise_for_status()
text_list = response.json()
text = " ".join(text_list)

word_num = 0
starting_pos = 0
ending_pos = len(text_list[word_num])
correctly_typed_words = 0
start_timer = None


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    global start_timer
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    instruction_lbl.config(text=f"time left: {count_min}:{count_sec}")
    if count > 0:
        start_timer = window.after(1000, count_down, count - 1)
    else:
        messagebox.showinfo(title="Typing Speed", message=f"Your Typing speed is {correctly_typed_words} WPM.")
        window.after_cancel(start_timer)


def highlight_next_word(event):
    global word_num, starting_pos, ending_pos, correctly_typed_words

    user_typed_word = type_entry.get().strip()
    text_to_type.config(state=NORMAL)

    try:
        # if the user typed the word correctly change that word color to green else change it to red.
        if user_typed_word == text_list[word_num]:
            text_to_type.tag_config(f"highlight{word_num}", foreground="green")
            correctly_typed_words += 1
        else:
            text_to_type.tag_config(f"highlight{word_num}", foreground="red")

        text_to_type.tag_config(f"highlight{word_num}", background=BACKGROUND_COLOR)
        word_num += 1
        starting_pos = ending_pos + 1

        ending_pos += len(text_list[word_num]) + 1
    except IndexError:
        pass
    else:
        text_to_type.tag_add(f"highlight{word_num}", f"1.{starting_pos}", f"1.{ending_pos}")
        text_to_type.tag_config(f"highlight{word_num}", background=HIGHLIGHT_COLOR)
        text_to_type.config(state=DISABLED)
        type_entry.delete(0, END)


def start_test(event):
    count_down(60)


window = Tk()
window.title("Typing Speed Test")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=40)

title_lbl = Label(text="Test Your Typing Speed", bg=BACKGROUND_COLOR, font=(FONT, 35, "bold"), fg=TITLE_COLOR)
title_lbl.pack()

instruction_lbl = Label(text="Press Enter to Start.", bg=BACKGROUND_COLOR, font=(FONT, 14, "bold"),
                        fg=INSTRUCTION_COLOR)
instruction_lbl.pack(pady=10)

# the text that user should type.
text_to_type = Text(window, bg=BACKGROUND_COLOR, font=(FONT, 15), bd=0, height=12, spacing2=5, wrap=WORD, width=80)
text_to_type.insert(INSERT, text)

# Highlight the first word.
text_to_type.tag_add(f"highlight{word_num}", f"1.{starting_pos}", f"1.{ending_pos}")
text_to_type.tag_config(f"highlight{word_num}", background=HIGHLIGHT_COLOR)

text_to_type.config(state=DISABLED)
text_to_type.pack(pady=20)

# entry bos to type words.
type_entry = Entry(font=(FONT, 15), width=80)
type_entry.focus()
type_entry.pack()

# when user press enter start the test.
type_entry.bind("<Return>", start_test)
# when user press space check the word is correctly typed and highlight the next word.
type_entry.bind("<space>", highlight_next_word)

window.mainloop()
