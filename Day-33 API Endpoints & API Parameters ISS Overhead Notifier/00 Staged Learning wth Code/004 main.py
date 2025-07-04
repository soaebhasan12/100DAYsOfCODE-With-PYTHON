import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json") 

# Handling response code through Exceptions:
if response.status_code == 404:
    raise Exception("Resource Not Exist.")
elif response.status_code == 401:
    raise Exception("Not Fount")

# Handling response code through requests module:
response.raise_for_status()


# Getting Actual data from API:
# data = response.json()

# data = response.json()["iss_position"]
data = response.json()
print(f"ISS Position: {data}")

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)