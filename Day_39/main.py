#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

with open("secret.txt", "r") as file:
    data = file.readlines()

KIWI_APIKEY = data[0].strip()
EMAIL = data[1].strip()
PASSWORD = data[2].strip()

ORIGIN_CITY_IATA = "DPS"

sheet_data = DataManager()
flight_price_data = sheet_data.get_data()
flight_search = FlightSearch()
notification = NotificationManager()

for city in flight_price_data:
    if(city["iataCode"] == ""):
        city["iataCode"] = flight_search.get_iataCode(city=city["city"], apikey=KIWI_APIKEY)
sheet_data.update_data(flight_price_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_now = datetime.now() + timedelta(days=(6 * 30))

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
            notification.send_email(flight_data=flight, email=EMAIL, password=PASSWORD)