# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json") 

# # Handling response code through Exceptions:
# if response.status_code == 404:
#     raise Exception("Resource Not Exist.")
# elif response.status_code == 401:
#     raise Exception("Not Fount")

# # Handling response code through requests module:
# response.raise_for_status()


# # Getting Actual data from API:
# # data = response.json()

# # data = response.json()["iss_position"]
# data = response.json()
# print(f"ISS Position: {data}")

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)








import requests
import datetime

MY_LATITUDE = 29.852970  
MY_LONGITUDE = 77.875450    

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0  # Use 0 to get the time in UTC
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0] # Extracting hour from sunrise time
sunset = data["results"]["sunset"].split("T")[1].split(":")[0] # Extracting hour from sunrise time

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now)