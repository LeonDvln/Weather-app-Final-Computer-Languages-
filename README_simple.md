# Weather App

**Description**

This is a simple command-line weather application written in Python. It uses the OpenWeatherMap API to fetch and display weather information for a specified city.

**Features**

- Allows the user to enter a city name.
- Lets the user choose between Celsius and Fahrenheit.
- Fetches temperature, humidity, and weather description.
- Handles errors such as invalid city name, API key issues, and network problems.

**How to Run**

1. Make sure Python 3 is installed on your system.
2. Install the required library using the command:

   python -m pip install requests

3. Get a free API key from https://openweathermap.org/api.
4. Replace the placeholder in the script with your actual API key.
5. Run the script:

   python weather.py

**Code Explanation**

- The script uses the `requests` module to make an HTTP request to OpenWeatherMap.
- It defines a `get_weather` function to fetch weather data and handle errors.
- A `display_weather` function is used to print the output or any error messages.
- The `main` function handles user input and ties everything together.
- The script uses `.get()` methods when reading JSON data to avoid key errors.
- It includes input validation and error messages for better user experience.

**Marking Criteria**

- API integration & JSON parsing: Included
- City input handling: Included
- Output formatting in °C/°F: Included
- Error handling & robustness: Included
- Code structure and UX: Included

**Example Output**

Enter city name: London  
Choose temperature unit:  
1. Celsius  
2. Fahrenheit  
Enter 1 or 2: 1  

Weather in London:  
Temperature: 15.3°C  
Humidity: 60%  
Condition: Light rain
