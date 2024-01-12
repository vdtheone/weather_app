import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")

def get_weather(api_key, city):
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"q": city, "key": api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        # Debugging: Print API request URL
        print("API Request URL:", response.url)

        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        location = weather_data.get('location', {})
        current = weather_data.get('current', {})

        print(f"Weather in {location['name']}, {location['region']}, {location['country']}:")
        print(f"Local Time: {location['localtime']}")
        print(f"Temperature: {current['temp_c']}°C / {current['temp_f']}°F")
        print(f"Condition: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['wind_kph']} kph, {current['wind_dir']}")
        print(f"Pressure: {current['pressure_mb']} mb")
        print(f"Cloud Coverage: {current['cloud']}%")

    else:
        print("Weather data not available.")

def main():
    api_key = API_KEY
    city = input("Enter city name: ")
    
    weather_data = get_weather(api_key, city)
    if weather_data and 'error' in weather_data:
        print(f"Error: {weather_data['error']['message']}")
    else:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
