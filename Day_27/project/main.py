import tkinter as tk 

def convert():
    miles = input.get()
    result["text"] = int(miles) * 1.61 

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)

input = tk.Entry()
miles = tk.Label(text="Miles")
km = tk.Label(text="Km")
equal_to = tk.Label(text="is equal to")
button = tk.Button(text="Calculate", command=convert)
result = tk.Label(text="0")

input.grid(row=0, column=1)
miles.grid(row=0, column=2)
equal_to.grid(row=1, column=0)
result.grid(row=1, column=1)
km.grid(row=1, column=2)
button.grid(row=2, column=1)


window.mainloop()
