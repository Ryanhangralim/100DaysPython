import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.ENDPOINT = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/flightDeals/prices"
    

    def get_data(self):
        response = requests.get(url=self.ENDPOINT)
        response.raise_for_status()
        return response.json()["prices"]
