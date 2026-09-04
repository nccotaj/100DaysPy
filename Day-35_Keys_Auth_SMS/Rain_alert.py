import requests
import os
from twilio.rest import Client


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ["OWM_API_KEY"]
MY_LAT = 41.051922
MY_LNG = -73.539482
CNT = 5




account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]




#### Weather API ###
weather_params = {
    "lat": 43.598110,
    "lon": -84.767570,
    "appid": API_KEY,
    "cnt": 5
}
#body="Rain Today 🌧️ - Bring Umbrella",
weather_response = requests.get(OWM_ENDPOINT, params=weather_params)
weather_response.raise_for_status()

weather_data = weather_response.json()

## Parsing Weather IDs ##
weather_ids = []
for n in range(CNT):
    weather_ids.append(int(weather_data["list"][n]["weather"][0]["id"]))

WILL_RAIN = False

if any(id < 600 for id in weather_ids):
    WILL_RAIN = True
else:
    WILL_RAIN = False

if WILL_RAIN:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="sms_appointment_reminders",
        to="+12037214481",
        from_="+17372583742",
    )

    print(message.status)

