import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iataCode(self, city : str, apikey : str) -> str:
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey" : apikey
        }
        query = {
            "term" : city,
            "location_types" : "city"
        }
        response = requests.get(url=location_endpoint, params=query, headers=headers)
        results = response.json()
        return results["locations"][0]["code"]
        