import tkinter as tk
FONT = ("Arial", 24, "bold")

#setup
window = tk.Tk()
window.minsize(width=500, height=300)
window.title('My First GUI Program')

my_label = tk.Label(text="New Label", font=FONT)
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    text = input.get()
    my_label["text"] = text

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

#entry
input = tk.Entry(width=10)
input.pack()
text = input.get()

#run
window.mainloop()