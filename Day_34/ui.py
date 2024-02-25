import tkinter as tk

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = tk.Label(text="Score: 0", fg="White", background=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score_board.grid(row=0, column=1)
        
        self.question_box = tk.Canvas(width=300, height=250)
        self.question_box.grid(row=1, column=0, columnspan=2, pady=20)

        self.question_text = self.question_box.create_text(150, 125, text="Question goes here", font=FONT)

        self.checkmark = tk.PhotoImage(file="images/true.png")
        self.true_choice = tk.Button(image=self.checkmark, highlightthickness=0, bd=0)
        self.true_choice.grid(row=2, column=0)

        self.cross = tk.PhotoImage(file="images/false.png")
        self.false_choice = tk.Button(image=self.cross, highlightthickness=0, bd=0)
        self.false_choice.grid(row=2, column=1)

        self.window.mainloop()


    def next_question(self, question):
        self.question_box.itemconfig(self.question_text, text=question)