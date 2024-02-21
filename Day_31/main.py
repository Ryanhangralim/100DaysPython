import tkinter as tk

# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

#import all images needed for UI
front_card_img = tk.PhotoImage(file="images/card_front.png")
back_card_img = tk.PhotoImage(file="images/card_back.png")
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

#flashcard config
canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

#right and wrong button
wrong = tk.Button(image=wrong_img, highlightthickness=0, bd=0)
wrong.grid(row=1, column=0)

right = tk.Button(image=right_img, highlightthickness=0, bd=0)
right.grid(row=1, column=1)

window.mainloop()