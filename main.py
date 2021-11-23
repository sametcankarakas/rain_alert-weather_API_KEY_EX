import requests
from twilio.rest import Client
api_key = "419a6ce745579aa39083ca60d22150ac"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# Your Account SID from twilio.com/console
account_sid = "AC1d88f63d13fa8b97a9dc07cfd6484b28"
# Your Auth Token from twilio.com/console
auth_token  = "32fc675509cc938c6d9def563b3f70bc"





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
        to="+905375167270",
        from_="+18043748512",
        body="Bugün yağış var diyorlar ☂️")
    print(message.sid)
    print(message.status)