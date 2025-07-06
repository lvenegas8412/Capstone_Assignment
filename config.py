import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

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
# print(response.json())

# Check if request was successful and get data
if response.status_code == 200:
    weather_data = response.json()

else:
    print(f"Error: {response.status_code}")
    print(response.text)