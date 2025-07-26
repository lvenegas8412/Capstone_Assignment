import requests
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

#OPENWEATHERMAP API
load_dotenv()
api_key = os.getenv('my_api')
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"        

# Parameters for our request
parameters = {
    "q": "Oxnard,US",         # The city we want weather for
    "appid": {api_key},           # API key
    "units": "imperial"           # Get temperature 
    }

# Make the request
response = requests.get(weather_api_url, params=parameters)

# Check if request was successful and get data
if response.status_code == 200:
    weather_data = response.json()

else:
    print(f"Error: {response.status_code}")
    print(response.text)


# WEATHERBIT API
end_date = datetime.now().date()
start_date = end_date - timedelta(days=1)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
wbapi_key = os.getenv('weatherbit_api')

weatherbit_api_url = "https://api.weatherbit.io/v2.0/history/daily"

# Parameters for our request
wb_parameters = {
    "city": "New York",
    "state": "NY",
    "country": "US",
    "start_date": start_date_str,
    "end_date": end_date_str, 
    "key": wbapi_key,
    "units": "I"
}

# Make the request
wb_response = requests.get(weatherbit_api_url, params=wb_parameters)

# Check if request was successful and get data
if wb_response.status_code == 200:
    wb_weather_data = wb_response.json()

else:
    print(f"Error: {wb_response.status_code}")
    print(wb_response.text)
