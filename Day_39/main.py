#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

with open("secret.txt", "r") as file:
    data = file.readlines()

KIWI_APIKEY = data[0]

sheet_data = DataManager()
flight_price_data = sheet_data.get_data()
flight_search = FlightSearch()

for city in flight_price_data:
    if(city["iataCode"] == ""):
        city["iataCode"] = flight_search.get_iataCode("bob")

sheet_data.update_data(flight_price_data)