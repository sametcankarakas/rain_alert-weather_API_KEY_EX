import requests
api_key = "419a6ce745579aa39083ca60d22150ac"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

MY_LAT = 40.983148
MY_LONG = 28.715770

weather_params = {
    # "q": "istanbul",
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,daily,minutely"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)