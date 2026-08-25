import requests
from datetime import datetime
import smtplib


my_email = "n8434109@gmail.com"
my_password = "Testemail1234!"

app_password = "gkyyoacmurxwodep"

receive_test = "nicktestctest@yahoo.com"


MY_LAT = 41.051922
MY_LNG = -73.539482

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# iss_latitude = 44.45
# iss_longitude = -69.987

def overhead():
    return(abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LNG) <= 5)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_utc = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_utc = int(data["results"]["sunset"].split("T")[1].split(":")[0])

sunrise = sunrise_utc - 5
sunset = sunset_utc - 5

time_now = datetime.now()

def dark():
    return(time_now.hour > sunset or time_now.hour < sunrise)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if overhead() and dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email, 
            o_addrs=receive_test, 
            msg="Subject: ISS \n\nLook up"
            )

