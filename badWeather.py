import os
from dotenv import load_dotenv
import requests

# Load environmental variables from .env file
load_dotenv()

# Retrieve API key from environmental variables
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
UNITS = "imperial"  # Use "metric" for Celsius


# Function to fetch location details using a city name
def get_location(city_name):
    location_api_url = (
        f"https://api.openweathermap.org/"
        f"geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    )
    response = requests.get(location_api_url)
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            city_result = location_data[0]["name"]
            state_result = location_data[0].get("state", None)
            country_result = location_data[0]["country"]
            return city_result, state_result, country_result
        else:
            print("No location data found for the given city name.")
            return None, None, None
    else:
        print(f"Error fetching location data: {response.status_code}")
        return None, None, None


# Function to fetch weather data
def get_weather(city_name, state_code=None, country_code=None):
    # Construct the query parameter
    query = city_name
    if state_code:
        query += f",{state_code}"
    if country_code:
        query += f",{country_code}"

    # Build the request URL
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units={UNITS}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city_name}: ")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°F")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} mph")
    else:
        print(
            f"\nError fetching weather data for {city_name}. "
            f"Please ensure the city, state, or country codes are correct."
        )


# Main program
if __name__ == "__main__":
    while True:
        print("\nEnter city details (or type 'quit' to exit):")
        city = input("City name: ").strip()
        if city.lower() == "quit":
            print("Goodbye!")
            break

        state = input("State code (optional, e.g., 'CA' for California): ").strip()
        country = input(
            "Country code (optional, e.g., 'US' for United States): "
        ).strip()

        if city:
            get_weather(city, state, country)
        else:
            print("Please enter a valid city name.")
