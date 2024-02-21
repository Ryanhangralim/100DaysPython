import tkinter as tk
import pandas
import random

# ---------------------------- IMPORT DATA (WORDS) ------------------------------- #
data = pandas.read_csv("data/japanese_words.csv")
data_dict = data.to_dict(orient="records")

# ---------------------------- GENERATE WORDS ------------------------------- #
def generate_word():
    return random.choice(data_dict)


# ---------------------------- UI SETUP ------------------------------- #
def new_word():
    generated_word = generate_word()
    japanese = generated_word["Japanese"]
    english = generated_word["English"]

    canvas.itemconfig(word, text=japanese)
# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Japanese Words Flash Cards")

#import all images needed for UI
front_card_img = tk.PhotoImage(file="images/card_front.png")
back_card_img = tk.PhotoImage(file="images/card_back.png")
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

#flashcard config
canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="watashi", font=("Arial", 60, "bold"))

#right and wrong button
wrong_button = tk.Button(image=wrong_img, command=new_word, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(image=right_img, command=new_word, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

window.mainloop()