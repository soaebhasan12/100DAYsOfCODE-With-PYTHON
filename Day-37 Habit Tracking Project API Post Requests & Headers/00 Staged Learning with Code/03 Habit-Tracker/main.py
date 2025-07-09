# 003 Advanced Authentication using an HTTP Header

import requests

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
