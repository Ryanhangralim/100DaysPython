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

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Learning Graph",
    "unit": "Min",
    "type": "int",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)