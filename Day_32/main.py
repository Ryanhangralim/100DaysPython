##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random 
import pandas

birthday = None
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

def get_letter(name):
    letter = random.choice(letters)
    with open(letter, "r") as file:
        lines = file.readlines()
    
    #replace [name] with person's name
    letter = ""
    for line in lines:
        line = line.replace("[NAME]", name)
        letter += line
    
    return letter

#import names and dates from birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")
print(birthday_data)

#get current date
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# #check through list of names
# for person in birthday_data:
#     if(person["month"] == current_month and person["day"]):


#send email
# with open("secret.txt", "r") as file:
#     data = file.readlines()

# email = data[0]
# password = data[1]

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, 
#                     to_addrs="rh232a@gmail.com", 
#                     msg="Subject:Testing smtp\n\nThis email is for testing smtp purposes")