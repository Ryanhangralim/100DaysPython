import tkinter as tk 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#window config
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#logo config
canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()