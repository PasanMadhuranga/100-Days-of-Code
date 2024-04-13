from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlopen
import tkinter

FONTS = ["Montserrat", "Ubuntu", "Courier", "EduSABeginner", "IbarraRealNova"]
COLORS = ["Silver", "Black", "Orange", "Green", "Red", "Blue"]

FONTS_DICT = {
    "Montserrat": "Montserrat-VariableFont_wght.ttf",
    "Ubuntu": "Ubuntu-Bold.ttf",
    "Courier": "CourierPrime-Bold.ttf",
    "EduSABeginner": "EduSABeginner-VariableFont_wght.ttf",
    "IbarraRealNova": "IbarraRealNova-VariableFont_wght.ttf"
}

COLORS_DICT = {
    "Silver": (189, 195, 199),
    "Black": (44, 62, 80),
    "Orange": (243, 156, 18),
    "Green": (39, 174, 96),
    "Red": (231, 76, 60),
    "Blue": (0, 151, 230)
}


def add_watermark():
    """Add watermark to the given picture."""

    # Get user input values.
    img_location = image_entry.get()
    url_or_path = image_variable.get()
    watermark_text = watermark_entry.get()
    font_size = int(size_spinbox.get())
    font = font_variable.get()
    place_the_watermark_to = (int(x_cor_entry.get()), int(y_cor_entry.get()))
    save_the_image_as = save_name_entry.get()
    save_the_final_image_to = save_to_entry.get()
    font_color = color_variable.get()

    # Open the image
    if url_or_path == "url":
        user_img = Image.open(urlopen(img_location))
    else:
        user_img = Image.open(img_location)

    # Change the font to user's choice
    watermark_font = ImageFont.truetype(f"fonts/{FONTS_DICT[font]}", font_size)

    image_editable = ImageDraw.Draw(user_img)

    # Add text to tha image.
    image_editable.text(place_the_watermark_to, watermark_text, COLORS_DICT[font_color], font=watermark_font)
    user_img.show()

    # Save the water marked image in user inputted name, to user inputted path
    user_img.save(f"{save_the_final_image_to}\\{save_the_image_as}")


window = tkinter.Tk()
window.title("Water Mark Adder")
window.config(padx=40, pady=10)

# Title
title_lbl = tkinter.Label(text="Water Mark Adder", font=("Roman", 35, "bold"))
title_lbl.grid(column=0, row=0, pady=10, columnspan=5)


# ---------------------------- image ----------------------------------- #
# Image Label
image_lbl = tkinter.Label(text="Image         : ")
image_lbl.grid(column=0, row=1, pady=2, sticky="W")
# Image Entry
image_entry = tkinter.Entry(width=45)
image_entry.grid(column=1, row=1, sticky="W", columnspan=2)
image_entry.focus()
# url, path dropdown
image_variable = tkinter.StringVar(window)
image_variable.set("url")  # default value
image_dropdown = tkinter.OptionMenu(window, image_variable, "url", "path")
image_dropdown.config(width=5)
image_dropdown.grid(column=3, row=1, sticky="W", columnspan=2)

# ---------------------------- watermark ----------------------------------- #
# watermark label
watermark_lbl = tkinter.Label(text="Watermark : ")
watermark_lbl.grid(column=0, row=2, pady=2, sticky="W")
# watermark entry
watermark_entry = tkinter.Entry(width=57)
watermark_entry.grid(column=1, row=2, columnspan=4, pady=5, sticky="W")

# ---------------------------- font size ----------------------------------- #
# size label
size_lbl = tkinter.Label(text="Size              : ")
size_lbl.grid(column=0, row=3, pady=2, sticky="W")
# size spinbox
size_spinbox = tkinter.Spinbox(from_=10, to=200, width=5)
size_spinbox.grid(column=1, row=3, pady=5, sticky="W")

# ------------ place that water mark should add (x cor , ycor) ------------- #
# where label
where_lbl = tkinter.Label(text="Where      : ")
where_lbl.grid(column=2, row=3, pady=2, sticky="E")
# X coordinate
x_cor_entry = tkinter.Entry(width=5)
x_cor_entry.grid(column=3, row=3, pady=2, sticky="W")
x_cor_entry.insert(0, "x")
# Y coordinate
y_cor_entry = tkinter.Entry(width=5)
y_cor_entry.grid(column=4, row=3, pady=2, sticky="W")
y_cor_entry.insert(0, "y")

# ---------------------------- Font Type ----------------------------------- #
# font label
font_lbl = tkinter.Label(text="Font             : ")
font_lbl.grid(column=0, row=4, pady=2, sticky="W")
# font dropdown
font_variable = tkinter.StringVar(window)
font_variable.set(FONTS[0])  # default value
font_dropdown = tkinter.OptionMenu(window, font_variable, *FONTS)
font_dropdown.config(width=13)
font_dropdown.grid(column=1, row=4, pady=5, sticky="W")

# ---------------------------- Font Color ----------------------------------- #
# color label
color_lbl = tkinter.Label(text="Font Color : ")
color_lbl.grid(column=2, row=4, pady=2, sticky="E")
# color dropdown
color_variable = tkinter.StringVar(window)
color_variable.set(COLORS[0])  # default value
color_dropdown = tkinter.OptionMenu(window, color_variable, *COLORS)
color_dropdown.config(width=5)
color_dropdown.grid(column=3, row=4, pady=5, sticky="W", columnspan=2)

# --------------- Name that watermarked image should save ------------------- #
# save name label
size_lbl = tkinter.Label(text="Save name  : ")
size_lbl.grid(column=0, row=5, pady=2, sticky="W")
# save name entry
save_name_entry = tkinter.Entry(width=57)
save_name_entry.grid(column=1, row=5, pady=2, columnspan=4, sticky="W")

# ---------------- Place where watermaked image should save --------------------- #
# Save to label
save_lbl = tkinter.Label(text="Save to        : ")
save_lbl.grid(column=0, row=6, pady=2, sticky="W")
# Save to entry
save_to_entry = tkinter.Entry(width=57)
save_to_entry.grid(column=1, row=6, pady=2, columnspan=4, sticky="W")

# ------------------------------- Add Button ------------------------------------- #
add_btn = tkinter.Button(text="Add", width=59, command=add_watermark)  # command=add_watermark
add_btn.grid(column=0, row=7, columnspan=5, pady=10)

window.mainloop()
