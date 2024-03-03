#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import sheety

with open("secret.txt", "r") as file:
    data = file.readlines()

KIWI_APIKEY = data[0].strip()
EMAIL = data[1].strip()
PASSWORD = data[2].strip()
SHEETY_AUTH = data[3].strip()

ORIGIN_CITY_IATA = "DPS"

sheet_data = DataManager(SHEETY_AUTH)
flight_price_data = sheet_data.get_data()
flight_search = FlightSearch()
notification = NotificationManager()

for city in flight_price_data:
    if(city["iataCode"] == ""):
        city["iataCode"] = flight_search.get_iataCode(city=city["city"], apikey=KIWI_APIKEY)
sheet_data.update_data(flight_price_data)

#user input
print("Welcome to Ryan's Flight Club\nWe find the best flight deals and emmail you.")
user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")
email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.add_new_user(first_name=user_first_name, last_name=user_last_name, email=email1, auth_header=SHEETY_AUTH)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))
emails = sheet_data.get_user()

for destination in flight_price_data:
    flight = flight_search.search_flight(
        origin_city=ORIGIN_CITY_IATA,
        destination_city=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_now,
        apikey=KIWI_APIKEY
    )
    if flight:
        if flight.price < destination["lowestPrice"]:
            for email in emails:
                notification.send_email(flight_data=flight, email=EMAIL, password=PASSWORD, desti_email=email)