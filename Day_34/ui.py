import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    ## quiz_brain's data type must be QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0

        self.score_board = tk.Label(text=f"Score: {self.score}", fg="White", background=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score_board.grid(row=0, column=1)
        
        self.question_box = tk.Canvas(width=300, height=250, highlightthickness=0, bd=0)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.question_box.create_text(150, 125, text="Question goes here", font=FONT, width=280)

        self.checkmark = tk.PhotoImage(file="images/true.png")
        self.true_choice = tk.Button(image=self.checkmark, command=self.true_pressed, highlightthickness=0, bd=0)
        self.true_choice.grid(row=2, column=0)

        self.cross = tk.PhotoImage(file="images/false.png")
        self.false_choice = tk.Button(image=self.cross, command=self.false_pressed, highlightthickness=0, bd=0)
        self.false_choice.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()


    def next_question(self):
        self.question_box.configure(background="white")
        self.true_choice["state"] = "active"
        self.false_choice["state"] = "active"

        if(self.quiz.still_has_questions()):
            self.question_box.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.true_choice["state"] = "disabled"
            self.false_choice["state"] = "disabled"
            self.question_box.itemconfig(self.question_text, text=f"Final Score: {self.score}")


    def true_pressed(self):
        if(self.quiz.check_answer("True")):
            self.add_score()
            self.give_feedback(True)
        else:
            self.give_feedback(False)


    def false_pressed(self):
        if(self.quiz.check_answer("False")):
            self.add_score()
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    
    def add_score(self):
        self.score += 1
        self.score_board["text"] = f"Score: {self.score}"


    def give_feedback(self, is_right):
        if is_right:
            self.question_box.configure(background="green")
        else:
            self.question_box.configure(background="red")
        self.true_choice["state"] = "disabled"
        self.false_choice["state"] = "disabled"
        self.feedback = self.window.after(1000, self.next_question)