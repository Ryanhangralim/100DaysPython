import requests

sheety_endpoint = "https://api.sheety.co/cba55caeefe970477a6323961e980c12/flightDeals/users"

def add_new_user(first_name, last_name, email, auth_header):
    headers = {
        "Authorization" : auth_header
    }
    params = {
        "user" : {
            "firstName" : first_name,
            "lastName" : last_name,
            "email" : email
        }
    }
    requests.post(url=sheety_endpoint, json=params, headers=headers).raise_for_status()