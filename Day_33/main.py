import requests
from datetime import datetime

MY_LAT = 36.204823
MY_LONG = 138.252930

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_latitude = float(data["iss_possition"]["latitude"])
iss_longitude = float(data["iss_possition"]["longitude"])


parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()


print(sunrise)
print(sunset)