import requests
import datetime

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
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Graph",
    "unit": "Min",
    "type": "int",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

now = datetime.datetime.now()

PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date" : now.strftime("%Y%m%d"),
    "quantity" : "60",
}

# response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(response.text)

UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/{now.strftime('%Y%m%d')}"

update_pixel_config = {
    "quantity" : "110"
}

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_config, headers=headers)
# print(response.text)

response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)