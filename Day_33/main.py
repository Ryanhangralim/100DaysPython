import requests
from datetime import datetime
import smtplib

MY_LAT = -8.340539
MY_LONG = 115.091949

def is_dark(current_hour, sunrise, sunset):
    return current_hour < sunrise and current_hour > sunset

def is_near(latitude, longitude):
    return (latitude in range(MY_LAT - 5, MY_LAT + 6)) and (longitude in range(MY_LONG -5, MY_LONG + 6))

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
current_hour = time_now.hour

if(is_near(iss_latitude, iss_longitude) and is_dark(current_hour, sunrise, sunset)):
    with open("secret.txt", "r") as file:
        data = file.readlines()

        email = data[0]
        password = data[1]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, 
                            to_addrs=data, 
                            msg=f"Look Up")