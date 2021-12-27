import os
import requests
from twilio.rest import Client
api_key = os.environ['api_key']
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
#Account SID from twilio.com/console
account_sid = os.environ['account_sid']
#Auth Token from twilio.com/console
auth_token  = os.environ['auth_token']





#ev konum
MY_LAT = 40.983148
MY_LONG = 28.715770


weather_params = {
    # "q": "istanbul",
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,daily,minutely"
}

weather_info = ""
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_slice = response.json()["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if 500 <= condition_code < 700:
        weather_info = "Bring an umbrella"
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+90537999999",
        from_="+18043748512",
        body="Bugün yağış var diyorlar ☂️")
    print(message.sid)
    print(message.status)