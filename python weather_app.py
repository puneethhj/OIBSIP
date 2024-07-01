import requests

def get_weather(api_key, location):
    """Fetch the weather data from the OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(weather_data):
    """Display the weather data."""
    if weather_data:
        city = weather_data['name']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        conditions = weather_data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions.capitalize()}")
    else:
        print("Unable to fetch weather data. Please check the location and try again.")

def main():
    """Main function to run the weather app."""
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    print("Welcome to the Weather App")
    location = input("Please enter a city name or ZIP code: ")
    
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
