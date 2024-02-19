import tkinter as tk 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_password = f"{website} | {email} | {password}\n"

    with open("password.txt", mode="a") as password_file:
        password_file.write(new_password)
    
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

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
website_entry.focus()

#email/username row
email = tk.Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = tk.Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_entry.insert(tk.END, "hangralim.2208561030@student.unud.ac.id")

#password row
password = tk.Label(text="Password:")
password.grid(row=3, column=0)

password_entry = tk.Entry(width=32)
password_entry.grid(row=3, column=1, sticky='W')

generate_password_button = tk.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky='W')

#add button
add_button = tk.Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()