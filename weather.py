import requests
from datetime import datetime
import time

# Your OpenWeatherMap API key goes here
API_KEY = "40b8c6e8711a008c203a0271f99685eb"
# The base URL for the OpenWeatherMap current weather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# This function fetches weather data from the API
def get_weather(city_name, units="metric"):
    params = {
        "q": city_name,        # City to get weather for
        "appid": API_KEY,      # API key
        "units": units         # Unit system (metric or imperial)
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract required weather information
            weather = {
                "city": data.get("name"),
                "temperature": data.get("main", {}).get("temp"),
                "humidity": data.get("main", {}).get("humidity"),
                "description": data.get("weather", [{}])[0].get("description")
            }
            return weather
        elif data.get("message"):
            return {"error": data["message"].capitalize()}
        else:
            return {"error": "Something went wrong. Please try again."}
    except requests.RequestException:
        return {"error": "Network error. Please check your connection."}

# This function prints weather information in a user-friendly format
def display_weather(weather_data, units):
    if "error" in weather_data:
        print(f"Error: {weather_data['error']}")
    else:
        unit_symbol = "C" if units == "metric" else "F"
        # Print the day, time, city, and weather details
        print(f"{get_time_and_day()} in {weather_data['city']} weather is:")
        print(f"Temperature: {weather_data['temperature']} {unit_symbol}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Condition: {weather_data['description'].capitalize()}")
        print("-" * 40)

# This function returns the current day and hour in the desired format
def get_time_and_day():
    now = datetime.now()
    return now.strftime("%A, %#I%p")  # For Windows; use "%A, %-I%p" on Linux/macOS

# Main function to run the app
def main():
    print("=== Weather App ===")

    # Ask user for preferred temperature unit
    print("Choose temperature unit:")
    print("1. Celsius (°C) [default]")
    print("2. Fahrenheit (°F)")
    unit_choice = input("Enter 1 or 2: ").strip()

    # Set unit based on user choice
    if unit_choice == "2":
        units = "imperial"
    else:
        units = "metric"

    # Loop to allow user to enter multiple cities
    while True:
        city = input("\nEnter city name (or press Enter to exit): ").strip()
        if not city:
            print("Exiting weather app. Goodbye, have a sunny day (preferably)!")
            break

        # Fetch and display weather
        weather = get_weather(city, units)
        display_weather(weather, units)
        time.sleep(1)  # Optional pause for readability

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
