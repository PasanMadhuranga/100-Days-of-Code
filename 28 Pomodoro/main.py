from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        reps = 0
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        num_of_work = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            num_of_work += "✔"
        check_marks.config(text=num_of_work)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)


check_marks = Label(fg=GREEN, bg=YELLOW, font=("Arial", 16))
check_marks.grid(column=1, row=3)

window.mainloop()
