# challenge: print "Bring Umbrella" if any of the next 12 hourly weather condition codes is less than 700
# HINTS:
# 1) Practice printing out the weather id for the weather in the 0th hour.
# 2) Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
# 3) Using the above try to create a list of only the next 12 weather condition codes.





import requests
import json

api_key = "000000000000000000000"                    # this a dummy key, replace with your own
# You can get your own API key from https://openweathermap.org/api/one-call-

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"            

weather_params = {
    "lat": 000000000,
    "lon": 000000000,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# solution 1) Practice printing out the weather id for the weather in the 0th hour.
print(weather_data["hourly"][0]["weather"][0]["id"])



# solution 2) Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
weather_slice = weather_data["hourly"][:12]



# solution 3) Using the above try to create a list of only the next 12 weather condition codes.

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")