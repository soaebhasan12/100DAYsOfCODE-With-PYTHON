# 002 HTTP Post Requests

import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "YOUR SELF GENERATED TOKEN",
    "username": "YOUR USERNAM",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)