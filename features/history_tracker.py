# features/weatherbit_api.py
import requests
from datetime import datetime, timedelta
from config import wbapi_key

def fetch_weather_history(city: str, days: int) -> list:
    
            # Check if the city is 'New York' and adjust it to 'New York City' for the API
    if city.lower() == "new york":
        city = "New York City"

    if not wbapi_key:
        raise ValueError("Missing API key")

    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)

    url = "https://api.weatherbit.io/v2.0/history/daily"

    params = {
        'city': city,
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'key': wbapi_key,
        'units': 'I'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "data" not in data or not data["data"]:
            raise ValueError("No weather data returned — likely invalid city.")

        # Optional: Double-check city match in response
        if "city_name" in data and data["city_name"].lower() != city.lower():
            raise ValueError(f"City not recognized: {city}")
        
        history = [
            {'date': entry['datetime'], 'temp': entry['temp']}
            for entry in data.get('data', [])
        ]
        return history
    except Exception as e:
        print(f"Error fetching weather history: {e}")
        return []
