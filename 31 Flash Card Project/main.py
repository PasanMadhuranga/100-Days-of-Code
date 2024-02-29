import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Get the French words from the csv file as a dictionary.
try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    dataframe = pandas.read_csv("data/french_words.csv")
finally:
    words_to_learn = dataframe.to_dict(orient="records")

selected_fr_word = ""


def flip_the_card():
    """Flips the card."""
    flash_card_canvas.itemconfig(flash_card_canvas_img, image=card_back_img)
    flash_card_canvas.itemconfig(flash_card_title_text, text="English", fill="white")
    flash_card_canvas.itemconfig(flash_card_word_text, text=selected_fr_word["English"], fill="white")


def next_word():
    """Show the title as French/English and show the word."""
    global selected_fr_word, flip_timer
    window.after_cancel(flip_timer)
    selected_fr_word = random.choice(words_to_learn)
    flash_card_canvas.itemconfig(flash_card_canvas_img, image=card_front_img)
    flash_card_canvas.itemconfig(flash_card_title_text, text="French", fill="black")
    flash_card_canvas.itemconfig(flash_card_word_text, text=selected_fr_word["French"], fill="black")
    flip_timer = window.after(ms=3000, func=flip_the_card)

def is_known():
    words_to_learn.remove(selected_fr_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# Create the user interface.
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(ms=3000, func=flip_the_card)

flash_card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
flash_card_canvas_img = flash_card_canvas.create_image(400, 263, image=card_front_img)
flash_card_title_text = flash_card_canvas.create_text(400, 200, text="Title", font=("Ariel", 40, "italic"))
flash_card_word_text = flash_card_canvas.create_text(400, 300, text="Word", font=("Ariel", 40, "bold"))
flash_card_canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

next_word()

window.mainloop()
