#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

sheet_data = DataManager().get_data()
flight_search = FlightSearch()

for city in sheet_data:
    if(city["iataCode"] == ""):
        city["iataCode"] = flight_search.get_iataCode("bob")

print(sheet_data)