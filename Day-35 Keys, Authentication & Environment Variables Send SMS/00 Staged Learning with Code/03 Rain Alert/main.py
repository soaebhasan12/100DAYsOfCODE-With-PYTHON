import requests
import json

api_key = "asdfasdfasdfasdfasdfasdf"                    # this a dummy key, replace with your own
# You can get your own API key from https://openweathermap.org/api/one-call-

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"            

weather_params = {
    "lat": 00.000000,
    "lon": 00.000000,
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())