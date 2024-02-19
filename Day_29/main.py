import tkinter as tk 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#window config
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#logo config
canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#website row
website = tk.Label(text="Website:")
website.grid(row=1, column=0)

website_entry = tk.Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2, sticky='W')

#email/username row
email = tk.Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = tk.Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')

#password row
password = tk.Label(text="Password:")
password.grid(row=3, column=0)

password_entry = tk.Entry(width=32)
password_entry.grid(row=3, column=1, sticky='W')

generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky='W')

#add button
add_button = tk.Button(text="Add", width=43)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()