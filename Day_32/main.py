import smtplib

#get email and password
with open("secret.txt", "r") as file:
    data = file.readlines()

email = data[0]
password = data[1]

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs="rh232a@gmail.com", msg="Testing smtp")
connection.close()