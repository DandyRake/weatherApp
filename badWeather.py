import requests

API_KEY = "f0b41db6ac4ed2353de5dbddeb0f71f1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=imperial"
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
        print(f"\nError fetching weather data.  Please check the city name or API key.")


while True:
    city = input("\nEnter a city name (or type 'quit' to exit): ").strip()
    if city.lower() == "quit":
        print("See you later!")
        break
    elif city:
        get_weather(city)
    else:
        print("Please enter a valid city name.")
