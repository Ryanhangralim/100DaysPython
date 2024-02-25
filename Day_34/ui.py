import tkinter as tk

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        score_board = tk.Label(text="Score: 0", fg="White", background=THEME_COLOR, font=("Arial", 14, "bold"))
        score_board.grid(row=0, column=1)
        
        question_box = tk.Canvas(width=300, height=250)
        question_box.grid(row=1, column=0, columnspan=2, pady=20)

        question_text = question_box.create_text(150, 125, text="Question goes here", font=FONT)

        checkmark = tk.PhotoImage(file="images/true.png")
        true_choice = tk.Button(image=checkmark, highlightthickness=0, bd=0)
        true_choice.grid(row=2, column=0)

        cross = tk.PhotoImage(file="images/false.png")
        false_choice = tk.Button(image=cross, highlightthickness=0, bd=0)
        false_choice.grid(row=2, column=1)

        self.window.mainloop()



QuizInterface()