import requests
from datetime import datetime
import smtplib
import time

MY_LATITUDE = 29.852970  # Your latitude
MY_LONGITUDE = 77.875450    # Your longitude

my_email = "soaebhasan22@gmail.com"
password = "wdbw wysh trmg aupu"  

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5) and (MY_LATITUDE-5 <= iss_longitude <= MY_LATITUDE+5):
        return True



def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset and time_now.hour <= sunrise:
         return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(
                        from_addr=my_email,
                        to_addrs="soaebhasan04@gmail.com",
                        msg="Subject:ISS Overhead \n\nInternational Space Station is on your Head, See Above."
                )