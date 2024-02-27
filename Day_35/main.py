import requests

parameters = {
    "lat" : -8.670458,
    "lon" : 115.212631,
    "cnt" : 4,
    "appid" : "05085e0a1c7026f86e153ebaed0e3d59"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]

#list of weather in the next 12 hours
weather = [weather_code["weather"][0]["id"] for weather_code in weather_data]

#check if it will rain 
is_raining = False

for code in weather:
    if code < 700:
        is_raining = True
    
if is_raining:
    print("Bring an umbrella☔")