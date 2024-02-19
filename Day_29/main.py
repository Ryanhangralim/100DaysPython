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
canvas.grid(row=0, column=1)

#website row
website = tk.Label(text="Website:")
website.grid(row=1, column=0)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

#email/username row
email = tk.Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

#password row
password = tk.Label(text="Password:")
password.grid(row=3, column=0)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

window.mainloop()