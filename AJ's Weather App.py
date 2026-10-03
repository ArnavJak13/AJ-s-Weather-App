import requests

# OpenWeather API key used to access live weather data
api_key = "00319edae93176de343245d4afa5bb2c"

# Stores successfully searched cities
search_history = []

# Keeps the program running until the user chooses to exit
while True:
    # Ask the user to enter a city name
    city = input("Welcome to AJ's Weather App!\nPlease enter the city name: ").strip().title()

    # Ask the user to choose Celsius or Fahrenheit
    unit_choice = input("Choose temperature unit (C/F): ").upper()

    # Set the API unit system and temperature symbol
    if unit_choice == "C":
        units = "metric"
        symbol = "°C"

    elif unit_choice == "F":
        units = "imperial"
        symbol = "°F"

    else:
        print("Invalid choice. Using Celsius by default.")
        units = "metric"
        symbol = "°C"

    # Build the OpenWeather API URL using the selected city and units
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

    # Send the request to the weather API
    response = requests.get(url)

    # Status code 200 means the weather data was received successfully
    if response.status_code == 200:
        # Convert the API response into Python data
        data = response.json()

        # Extract the required weather information
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        feels_like = data["main"]["feels_like"]
        visibility = data.get("visibility", "N/A")
        country = data["sys"]["country"]

        # Convert wind speed to kilometres per hour
        if units == "metric":
            wind_speed_kmh = wind_speed * 3.6
        else:
            wind_speed_kmh = wind_speed * 1.60934

        # Add the city to search history if it has not already been searched
        if city not in search_history:
            search_history.append(city)

        # Display the weather information
        print(f"\nWeather in {city}, {country}:")
        print(f"\nTemperature: {temperature}{symbol}")
        print(f"Weather Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed_kmh:.2f} km/h")
        print(f"Feels Like: {feels_like}{symbol}")
        print(f"Visibility: {visibility / 1000:.2f} km")

    else:
        # Display an error message if the weather request was unsuccessful
        print("\nError fetching weather data.")
        print("Please check the city name and try again.")

    # Keep asking until the user enters a valid Y or N choice
    while True:
        choice = input("\nDo you want to check another city? (Y/N): ").upper()

        if choice == "Y":
            break

        elif choice == "N":
            # Display all successful searches before exiting
            print("\nSearch History:")

            if len(search_history) == 0:
                print("No successful searches.")

            else:
                for searched_city in search_history:
                    print(searched_city)

            print("\nThank you for using AJ's Weather App! See you next time!")
            exit()

        else:
            print("Please enter only Y or N.")