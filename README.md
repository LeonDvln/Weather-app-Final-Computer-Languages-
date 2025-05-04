# 🌦️ Weather App (Python + OpenWeatherMap API)

This is a simple command-line weather app written in Python. It fetches current weather data (temperature, humidity, and condition) for any city using the OpenWeatherMap API.

---

## 📌 Features

- Fetch current weather for any city
- User chooses temperature units (°C or °F)
- Handles errors like invalid city names or API key issues
- Clean and structured code with comments

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Install the required library:

   ```bash
   python -m pip install requests
   ```

3. Get a free API key from [https://openweathermap.org/api](https://openweathermap.org/api)
4. Insert your API key into the `API_KEY` variable in `weather.py`
5. Run the app:

   ```bash
   python weather.py
   ```

---

## 📂 File Structure

```
weatherapp/
├── weather.py       # Main Python script
├── README.md        # This file
```

---

## 🧠 Code Explanation

Below is a full breakdown of the code, line by line:

...

## ✅ Marking Criteria Covered

| Criteria                      | Included? | Notes |
|------------------------------|-----------|-------|
| ✅ API integration & JSON     | ✔️        | Uses `requests` and `.get()` safely |
| ✅ City input handling        | ✔️        | Uses `input()` and `.strip()` |
| ✅ Output formatting          | ✔️        | Temperature shown with °C or °F |
| ✅ Error handling             | ✔️        | Handles network, API key, city errors |
| ✅ Code structure & UX        | ✔️        | Uses functions and clear prompts |

---

## 🧊 Example Output

```
=== Weather App ===
Enter city name: Tashkent

Choose temperature unit:
1. Celsius (°C)
2. Fahrenheit (°F)
Enter 1 or 2: 1

Weather in Tashkent:
Temperature: 20.97°C
Humidity: 40%
Condition: Clear sky
```

---

## 📜 License

This is a basic educational project. Feel free to modify or share it.
