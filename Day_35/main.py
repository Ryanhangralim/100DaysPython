import requests
import smtplib

#import email and key
with open("secret.txt", "r") as file:
    data = file.readlines()

EMAIL = data[0]
PASSWORD = data[1]

parameters = {
    "lat" : -8.670458,
    "lon" : 115.212631,
    "cnt" : 6,
    "appid" : "05085e0a1c7026f86e153ebaed0e3d59"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]

#list of weather in the next 12 hours
weather = [weather_code["weather"][0]["id"] for weather_code in weather_data]

#check if it will rain 
is_raining = False

for code in weather[1:]:
    if code < 700:
        is_raining = True
    
if is_raining:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, 
                            to_addrs=EMAIL, 
                            msg=f"Subject:Rain Alert!\n\nIt will rain today, don't forget to bring an umbrella!")
    print("Bring an umbrella☔")