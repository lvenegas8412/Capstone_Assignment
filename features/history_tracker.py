# features/weatherbit_api.py
import requests
from datetime import datetime, timedelta
from config import wbapi_key

def fetch_weather_history(city: str, days: int) -> list:
    """
    Fetch past weather data using Weatherbit API.

    Returns:
        List of dicts: [{'date': str, 'temp': float}, ...]
    """
    if not wbapi_key:
        raise ValueError("Missing API key")

    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)

    url = "https://api.weatherbit.io/v2.0/history/daily"

    params = {
        'city': city,
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
        'key': wbapi_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        history = [
            {'date': entry['datetime'], 'temp': entry['temp']}
            for entry in data.get('data', [])
        ]
        return history
    except Exception as e:
        print(f"Error fetching weather history: {e}")
        return []
