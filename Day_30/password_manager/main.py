import tkinter as tk 
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if(len(website) == 0 or len(email) == 0 or len(password) == 0):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        try:
            with open("password.json", mode="r") as password_file:
                #reading old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("password.json", mode="w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("password.json", mode="w") as password_file:
                json.dump(data, password_file, indent=4)
        
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    #check for website to be searched
    website = website_entry.get()
    if(len(website) == 0):
        messagebox.showinfo(title="Oops", message="Please don't leave the website field empty")
    else:
        try:
            with open("password.json", mode="r") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
        #Add exception when file doesn't exist
            messagebox.showinfo(title="Error", message="No Data File Found")
        else:
            if(website in data.keys()):
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No details for the website exists") 

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

website_entry = tk.Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky='W')
website_entry.focus()

search_button = tk.Button(text="Search", command=find_password, width=14)
search_button.grid(row=1, column=2, sticky='W')


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

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky='W')

#add button
add_button = tk.Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()