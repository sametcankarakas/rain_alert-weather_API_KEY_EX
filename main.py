api_key = "419a6ce745579aa39083ca60d22150ac"
import requests

parameters = {
    "q": "istanbul",
    "appid": api_key,
}

connection = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
connection.raise_for_status()
data = connection.json()
print(data)
