import requests

USERNAME = "ryanhangralim"

#get token
with open("secret.txt", "r") as file:
    token = file.readline()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token" : token,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
