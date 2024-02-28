import json
import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password."""

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 5)

    password_list = []
    password_list += [random.choice(string.ascii_letters) for _ in range(nr_letters)]
    password_list += [random.choice(string.punctuation) for _ in range(nr_symbols)]
    password_list += [random.choice(string.digits) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Save the given details to the 'data.txt' file."""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "Email": email,
        "Password": password,
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                messagebox.showinfo(title="Success", message="Data added successfully!")

            # Angela's Method
            # try:
            #     with open("data.json", "r") as data_file:
            #         data = json.load(data_file)
            # except FileNotFoundError:
            #     with open("data.json", "w") as data_file:
            #         json.dump(new_data, data_file, indent=4)
            # else:
            #     data.update(new_data)
            #     with open("data.json", "w") as data_file:
            #         json.dump(data, data_file, indent=4)
            #
            # finally:
            #     website_entry.delete(0, END)
            #     password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Find the password and email to the relevant website."""
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_lbl = Label(text="Website:")
website_lbl.grid(column=0, row=1, pady=2)

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2, pady=2)

password_lbl = Label(text="Password")
password_lbl.grid(column=0, row=3, pady=2)

# Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_entry.insert(0, "pasan1234@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, pady=2)

# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, pady=2)

add_btn = Button(text="Add", width=44, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, pady=2)

search_btn = Button(text="Search", width=14, command=find_password)
search_btn.grid(column=2, row=1, pady=2)

window.mainloop()
