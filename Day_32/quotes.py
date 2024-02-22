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


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, 
                    to_addrs="rh232a@gmail.com", 
                    msg="Subject:Testing smtp\n\nThis email is for testing smtp purposes")