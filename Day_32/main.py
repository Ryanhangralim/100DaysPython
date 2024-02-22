##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt

#get email and password
with open("secret.txt", "r") as file:
    data = file.readlines()

email = data[0]
password = data[1]

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, 
                    to_addrs="rh232a@gmail.com", 
                    msg="Subject:Testing smtp\n\nThis email is for testing smtp purposes")