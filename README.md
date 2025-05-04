
# Weather App (Python + OpenWeatherMap API)

## Description
This is a command-line weather application written in Python. It fetches and displays current weather information for any city using the OpenWeatherMap API.

---

## Features

- Ask user for temperature unit (Celsius or Fahrenheit)
- Input any city name to retrieve real-time weather
- Shows:
  - Day and time, City (e.g. Monday, 1AM)
  - Temperature
  - Humidity
  - Condition (e.g. "Few clouds")
- Handles invalid cities or network errors gracefully
- Keeps asking for new cities until Enter is pressed

---

## Requirements

- Python 3.7+
- Internet connection
- `requests` library (install with `pip install requests`)

---

## How to Use

1. Open terminal/command prompt.
2. Run the app:
   	python weather.py
   
3. Follow on-screen instructions.

---

## Code Explanation

# Import Statements
'''python
import requests
from datetime import datetime
import time

- `requests`: for making HTTP requests to the API.
- `datetime`: to get the current day and time.
- `time`: for a short delay after each request.

### API Setup
'''python
API_KEY = "40b8c6e8711a008c203a0271f99685eb"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

- Replace `API_KEY` with your OpenWeatherMap key.

### get_weather()
- Sends a request to the API with city and unit.
- Returns a dictionary with weather info or an error message.

### display_weather()
- Displays formatted weather results if successful.
- Handles and shows any error if the request failed(connection lost error).

### get_time_and_day()
- Returns the current weekday and hour in format like `Monday, 1AM`.

### main()
- Selection between Celsius or Fahrenheit as temperature units appears as the initial step in the app.
- The application will change the unit measurement to "imperial" with Fahrenheit scale when the user selects "2".
- Users will automatically receive "metric" units (Celsius) unless they provide an input of "2".
- The application uses this logical method to maintain system stability when users provide unusual input.
- Enters a city (or presses Enter to exit).
- Weather is fetched and displayed.
- Repeats until user exits with pressing Enter.

### while True (Input loop)
- This is an infinite loop (while True) that keeps running until the user decides to exit.
- It prompts the user to enter a city name.
- If the input is empty (the user just presses Enter), the loop breaks and the program exits with a goodbye message.

# If a city name is provided, it:
	- Calls get_weather() to fetch weather data for the entered city.
	- Calls display_weather() to print the results.
	- Pauses for 1 second with time.sleep(1) to make the output more readable.

---

## Example Output

=== Weather App ===
Choose temperature unit:
1. Celsius (°C) [default]
2. Fahrenheit (°F)
Enter 1 or 2: 1

**
Enter city name (or press Enter to exit): Tashkent

Monday, 1AM in Tashkent weather is:

Temperature: 18.5 C

Humidity: 45%

Condition: Clear sky

----------------------------------------

---

## License

Ravshanbek Zokirjonov
