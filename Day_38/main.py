import requests
import datetime

with open("secret.txt", "r") as file:
    data = file.readlines()

APP_ID = data[0].strip()
API_KEY = data[1].strip()
AUTH_HEADER = data[2]

GENDER = "male"
WEIGHT = 75
HEIGHT = 178
AGE = 18

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

nutritionix_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(
    url=NUTRI_ENDPOINT, json=nutritionix_config, headers=nutritionix_headers
)
response.raise_for_status()
response = response.json()

SHEETY_ENDPOINT = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/myWorkoutsPythonCourse/workouts"

today = datetime.datetime.now()
today_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S")

sheety_headers = {"Authorization": AUTH_HEADER}

for exercise in response["exercises"]:
    sheety_config = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    requests.post(
        url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_headers
    ).raise_for_status()
