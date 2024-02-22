import smtplib
import datetime as dt
import random

#get email and password
with open("secret.txt", "r") as file:
    data = file.readlines()

email = data[0]
password = data[1]

#get list of quotes
with open("quotes.txt", "r") as quote_file:
    quotes = quote_file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if(day_of_week == 3):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, 
                        to_addrs="rh232a@gmail.com", 
                        msg=f"Subject:Weekly Quotes\n\n{random.choice(quotes)}")