import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, auth):
        self.ENDPOINT = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/flightDeals/prices"
        self.USER_ENDPOINT = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/flightDeals/users"
        self.AUTH = auth

    def get_data(self):
        headers = {
            "Authorization" : self.AUTH
        }
        response = requests.get(url=self.ENDPOINT, headers=headers)
        response.raise_for_status()
        return response.json()["prices"]
    
    def get_user(self):
        headers = {
            "Authorization" : self.AUTH
        }
        response = requests.get(url=self.USER_ENDPOINT, headers=headers)
        response.raise_for_status()
        emails = [user["email"] for user in response.json()["users"]]
        return emails
    
    def update_data(self, sheet_data):
        for city in sheet_data:
            endpoint = f"{self.ENDPOINT}/{city['id']}"
            params = {
                "price":{
                    "city" : city["city"],
                    "iataCode" : city["iataCode"],
                    "lowestPrice" : city["lowestPrice"]
                }
            }
            response = requests.put(url=endpoint, json=params)
            response.raise_for_status()