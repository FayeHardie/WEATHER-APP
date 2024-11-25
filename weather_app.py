#Welcome message


print("Welcome to this weather app")


#User input - city name
def user_input():
    city_name = input("Please enter city name: ")
    return city_name

#storing weather data in a dictonary
weather_data = {
            "London": {
                "conditions": "Cloudy",
                "temperature": "10°C",
                "wind_speed": "12 km/h",
                "humidity": "81%"
        },
            "Tokyo": {
                "conditions": "Cloudy",
                "temperature": "11°C",
                "wind_speed": "17 km/h",
                "humidity": "56%"
        },
            "Paris": {
                "conditions": "Foggy",
                "temperature": "11°C",
                "wind_speed": "11 km/h",
                "humidity": "83%"
        },
            "Toronto": {
                "conditions": "Sunny",
                "temperature": "13°C",
                "wind_speed": "12 km/h",
                "humidity": "47%"
        },
            "Sydney": {
                "conditions": "Cloudy",
                "temperature": "18°C",
                "wind_speed": "9 km/h",
                "humidity": "86%"
            }
        }



#displaying the weather data in a readable manner
def display(city_name):
    city = city_name.title()
    try: 
        city_weather = weather_data[city]
        conditions = city_weather["conditions"]
        temp = city_weather["temperature"]
        wind = city_weather["wind_speed"]
        humid = city_weather["humidity"]

        print(f"The weather for {city} is: \nConditions: {conditions} \nTemperature: {temp} \nWind Speed{wind} \nHumidity: {humid}")
    except KeyError:
        print("Error: Data not available or invalid entry")


    
city_name = user_input()
display(city_name)
