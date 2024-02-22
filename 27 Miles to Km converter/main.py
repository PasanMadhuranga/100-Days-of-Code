from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# window.minsize(width=300, height=100)


def mile_to_km():
    """Convert miles to kilometers."""
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    label2.config(text=km)


label1 = Label(text="is equal to", font=("Arial", 12))
label1.grid(column=0, row=1)

label2 = Label(text=0, font=("Arial", 12))
label2.grid(column=1, row=1)

label3 = Label(text="Km", font=("Arial", 12))
label3.grid(column=2, row=1)

label4 = Label(text="Miles", font=("Arial", 12))
label4.grid(column=2, row=0)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

calculate = Button(text="Calculate", command=mile_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
