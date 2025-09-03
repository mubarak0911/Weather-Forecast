import requests

API_KEY = "7acf788a1b9853d11babf39c60b06310"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # You can change to "imperial" for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    display_weather(weather)