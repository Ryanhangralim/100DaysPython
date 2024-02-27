import requests

parameters = {
    "lat" : -8.340539,
    "lon" : 115.091949,
    "appid" : "05085e0a1c7026f86e153ebaed0e3d59"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
print(response.status_code)