import smtplib

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