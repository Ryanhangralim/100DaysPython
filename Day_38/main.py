import requests
import datetime

with open("secret.txt", "r") as file:
    data = file.readlines()

APP_ID = data[0].strip()
API_KEY = data[1]
GENDER = "male"
WEIGHT = 75
HEIGHT = 178
AGE = 18

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

nutritionix_config = {
    "query" : "swam for 1 hour and ran 2k",
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE
}

response = requests.post(url=NUTRI_ENDPOINT, json=nutritionix_config, headers=nutritionix_headers)
response = response.json()
print(response)

SHEETY_ENDPOINT = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/myWorkoutsPythonCourse/workouts"

for exercise in response["exercises"]:
    sheety_config = {
        "workout" : {
            "date" : 1,
            "time" : 2,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
    requests.post(url=SHEETY_ENDPOINT, json=sheety_config)