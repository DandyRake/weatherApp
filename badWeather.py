import requests

API_KEY = "f0b41db6ac4ed2353de5dbddeb0f71f1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
