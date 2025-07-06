import requests
import json

api_key = "6c53fd9deaa27688ad3a2ccfebf78263"                    # this a dummy key, replace with your own
# You can get your own API key from https://openweathermap.org/api/one-call-

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"            

weather_params = {
    "lat": 29.852970,
    "lon": 77.875450,
    "appid": api_key,
}


response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())