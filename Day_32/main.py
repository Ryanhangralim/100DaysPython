import smtplib

#get email and password
with open("secret.txt", "r") as file:
    data = file.readlines()

print(data[0])
#GMAIL : 100daypythonday32@gmail.com
