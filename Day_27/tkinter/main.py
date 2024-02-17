import tkinter as tk
FONT = ("Arial", 24, "bold")

#setup
window = tk.Tk()
window.minsize(width=500, height=300)
window.title('My First GUI Program')

my_label = tk.Label(text="New Label", font=FONT)
my_label.pack()

#run
window.mainloop()