from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0,
                               fg="white", font=("Courier", 16, "bold"))
        self.score_lbl.grid(column=1, row=0)

        self.quiz_canvas = Canvas(width=400, height=350, bg="white")
        self.question = self.quiz_canvas.create_text(200, 176, width=380, text="Some Question text",
                                                     font=("Arial", 20, "italic"))
        self.quiz_canvas.grid(column=0, row=1, columnspan=2, pady=25)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=lambda: self.check_answer("true"))
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=lambda: self.check_answer("false"))
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.quiz_canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.quiz_canvas.itemconfig(self.question, text=question_text)
        else:
            self.quiz_canvas.itemconfig(self.question, text="The End.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_answer(self, player_answer):
        is_right = self.quiz.check_answer(player_answer)
        if is_right:
            self.quiz_canvas.configure(bg="green")
        else:
            self.quiz_canvas.configure(bg="red")
        self.window.after(500, func=self.get_next_question)


