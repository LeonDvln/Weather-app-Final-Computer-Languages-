
# Weather App (Python + OpenWeatherMap API)

## Description
This is a simple command-line weather application written in Python. It fetches and displays current weather information for any city using the OpenWeatherMap API.

---

## Features

- Ask user for temperature unit (Celsius or Fahrenheit)
- Input any city name to retrieve real-time weather
- Shows:
  - Day and time (e.g. Monday, 1AM)
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

1. Replace `"your_api_key_here"` in `weather.py` with your OpenWeatherMap API key.
2. Open terminal/command prompt.
3. Run the app:
   ```bash
   python weather.py
   ```
4. Follow on-screen instructions.

---

## Code Explanation

### Import Statements
```python
import requests
from datetime import datetime
import time
```
- `requests`: for making HTTP requests to the API.
- `datetime`: to get the current day and time.
- `time`: for a short delay after each request.

### API Setup
```python
API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
```
- Replace `API_KEY` with your OpenWeatherMap key.

### get_weather()
- Sends a request to the API with city and unit.
- Returns a dictionary with weather info or an error message.

### display_weather()
- Displays formatted weather results if successful.
- Handles and shows any error if the request failed.

### get_time_and_day()
- Returns the current weekday and hour in format like `Monday, 1AM`.

### main()
- User chooses unit: Celsius (default) or Fahrenheit.
- Enters a city (or presses Enter to exit).
- Weather is fetched and displayed.
- Repeats until user exits.

---

## Example Output

```
=== Weather App ===
Choose temperature unit:
1. Celsius (°C) [default]
2. Fahrenheit (°F)
Enter 1 or 2: 1

Enter city name (or press Enter to exit): Tashkent
Monday, 1AM in Tashkent weather is:
Temperature: 18.5 C
Humidity: 45%
Condition: Clear sky
----------------------------------------
```

---

## License

This project is free to use for learning and academic purposes.
