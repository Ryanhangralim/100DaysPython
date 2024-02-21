import tkinter as tk
import pandas
import random

#global variable
generated_word = None

# ---------------------------- IMPORT DATA (WORDS) ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_words.csv")
    data_dict = data.to_dict(orient="records")


# ---------------------------- FLIP CARD ------------------------------- #
def flip():
    #get current language
    canvas.itemconfig(flashcard, image=back_card_img)
    canvas.itemconfig(word, text=generated_word["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white") 

# ---------------------------- UI SETUP ------------------------------- #
def new_word():
    global generated_word, flip_timer
    window.after_cancel(flip_timer)
    generated_word = random.choice(data_dict)
    japanese = generated_word["Japanese"]

    canvas.itemconfig(flashcard, image=front_card_img)
    canvas.itemconfig(language, text="Japanese", fill="black") 
    canvas.itemconfig(word, text=japanese, fill="black")
    flip_timer = window.after(3000, func=flip)

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Japanese Words Flash Cards")
flip_timer = window.after(3000, func=flip)

#import all images needed for UI
front_card_img = tk.PhotoImage(file="images/card_front.png")
back_card_img = tk.PhotoImage(file="images/card_back.png")
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

#flashcard config
canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 150, text="Japanese", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="watashi", font=("Arial", 60, "bold"))

#right and wrong button
wrong_button = tk.Button(image=wrong_img, command=new_word, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(image=right_img, command=new_word, highlightthickness=0, bd=0)
right_button.grid(row=1, column=1)

new_word()
window.mainloop()