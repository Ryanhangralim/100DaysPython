import requests

#get token
with open("secret.txt", "r") as file:
    token = file.readline()

ENDPOINT = "https://pixel.la/v1/users"
user_params = {
    "token" : token,
    "username" : "RyanHangralim",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}