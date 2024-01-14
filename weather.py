""""
PROGRAM NAME: weather.py
PROGRAM PURPOSE: Demontrates using API key, and using JSON
DATE WRITTEN: 12-13-23
PROGRAMMER: Ella Patten
"""

import requests
import datetime


x = 0
DEGREE_SYMBOL = '°'


API_KEY = "5e7d4b0f4563baa7c90921d1959cf074"
def main():
    # Print instructions
    print('''
-----------Thank you for using WeatherWagon------------
    Follow the prompts to enter desired location
    then type a quoted word below to see the:
      "longitude" for given location 
      "latitude" for given location  
      "cloudiness" for given location  
      "time" data retrieved 
      "percieved" temperature for given location
      "temperature" for given location
      "humidity" % for given location 
      Atmospheric "pressure" for given location
      Time of "sunrise" for given location
      Time of "sunset" for given location 
      "visibility" for given location
      "wind" speed for given location
      "done" to exit the program
          ''')
    # Get location from user and put location in API address
    location = input("Enter Your Desired City: ")
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
    # concatenate url and api key to return weather data
    final_url = weather_url + API_KEY
    # Format weather data into dictionary
    weather_data = requests.get(final_url).json()
    print()
    # check to make sure loction is valid
    try:
        #while there is a message that says there isn't that city, loop asking user for a valid location
        while weather_data['message'] == 'city not found':
            print("Please enter a valid City")
            print()
            # Use same location technique as before
            location = input("Enter Your Desired City: ")
            print()
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
            final_url = weather_url + API_KEY
            weather_data = requests.get(final_url).json()
    #When there is no longer a message value, run this code
    except KeyError:
        # ask user for the information they want
        var = input("Enter the key word for the information you would like to recieve. Input 'ex' for allowed entries, input 'done' to exit:  ")
        # While the user does not enter done and terminate the program, it prints to allow for more inputs
        while var != "done":
            print(response(weather_data, var))
            var = input("Enter the key word for the information you would like to recieve. Input 'ex' for allowed entries, input 'done' to exit:  ")
        print("Thank you for using the weather program!")


def timezone(hours):
    """
    Gets the hours of time difference from user/location
    and returns the time difference from UTC time
    """
    global y
    if hours == 1:
        y = 1
        return "(UTC + 01:00)"
    elif hours == 2:
        y = 2
        return "(UTC + 02:00)"
    elif hours == 3:
        y = 3
        return "(UTC + 03:00)"
    elif hours == 4:
        y = 4
        return "(UTC + 04:00)"
    elif hours == 5:
        y = 5
        return "(UTC + 05:00)"
    elif hours == 6:
        y = 6
        return "(UTC + 06:00)"
    elif hours == 7:
        y = 7
        return "(UTC + 07:00)"
    elif hours == 8:
        y = 8
        return "(UTC + 08:00)"
    elif hours == 9:
        y = 9
        return "(UTC + 09:00)"
    elif hours == 10:
        y = 10
        return "(UTC + 10:00)"
    elif hours == 11:
        y = 11
        return "(UTC + 11:00)"
    elif hours == 12:
        y = 12
        return "(UTC + 12:00)"
    elif hours == 13:
        y = 13
        return "(UTC + 13:00)"
    elif hours == -1:
        y = -1
        return "(UTC - 01:00)"
    elif hours == -2:
        y = -2
        return "(UTC - 02:00)"
    elif hours == -3:
        y = -3
        return "(UTC - 03:00)"
    elif hours == -4:
        y = -4
        return "(UTC - 04:00)"
    elif hours == -5:
        y = -5
        return "(UTC - 05:00)"
    elif hours == -6:
        y = -6
        return "(UTC - 06:00)"
    elif hours == -7:
        y = -7
        return "(UTC - 07:00)"
    elif hours == -8:
        y = -8
        return "(UTC - 08:00)"
    elif hours == -9:
        y = -9
        return "(UTC - 09:00)"
    elif hours == -10:
        y = -10
        return "(UTC - 10:00)"
    elif hours == -11:
        y = -11
        return "(UTC - 11:00)"
    elif hours == -12:
        y = -12
        return "(UTC - 12:00)"


def convert_time(time, zone):
    """
    Takes the current time in UTC and the time zone provided 
    from the dictionary and adds the amount of time needed to 
    provide the time in the timezone the user is in. 
    """
    date = int(time)
    time = datetime.datetime.utcfromtimestamp(date)
    timezon = int(zone) /3600
    timezone(timezon)
    time_change = datetime.timedelta(hours = y)
    time += time_change
    return time

def convert_temp(temp):
    # Converts Temp from Kelvin to F
    temperatre = (temp - 273.15) * 1.8 + 32
    return round(temperatre)

def convert_distance(meters):
    # converts m to km
    km = meters / 1000
    return km

def convert_pressure(press):
    # converts hPa to psi
    pressure = press * 0.0145038
    return pressure

def convert_speed(spee):
    # converts m/s to mph
    speed = spee * 2.237
    return round(speed, 2)

def response(lists, data):
    """
    Checks what "data" the user enters to grab from the weather_data "lists"
    and calls the necessary functions and returns the data that the user requested
    """
    # until the user inputs 'done' this will run
    while data.lower() != "done":
        if data == "ex." or data == "ex":
            # returns instructions for what the user can input
            return '''
            Type a quoted word below to see the:
            "longitude" for given location 
            "latitude" for given location  
            "cloudiness" for given location  
            "time" data retrieved 
            "percieved" temperature for given location
            "temperature" for given location
            "humidity" % for given location 
            Atmospheric "pressure" for given location
            Time of "sunrise" for given location
            Time of "sunset" for given location 
            "visibility" for given location
            "wind" speed for given location
            "done" to exit the program
                '''
            continue
        elif data.lower() == "longitude":
            #returns longitude of location
            longitude = lists["coord"]["lon"]
            return f'Longitude: {longitude}'
        elif data.lower() == "latitude":
            # returns latitude of location
            latitude = lists["coord"]["lat"]
            return f'Latitude {latitude}'
        elif data.lower() == "cloudiness":
            # returns the percent cloudy
            cloudy = lists['clouds']['all']
            return f"{cloudy}% cloudy"
        elif data.lower() == "time":
            # calls convert_time and takes timezone to calculate
            # current time data was retrieved in users time zone
            date = lists["dt"]
            timezones = lists["timezone"]
            time = convert_time(date, timezones)
            return f"Data retrieved on {time}"
        elif data.lower() == "percieved":
            # returns percieved temp in F after converting using convert_temp()
            temp = int(lists["main"]["feels_like"])
            return f"Feels like: {convert_temp(temp)}{DEGREE_SYMBOL}F"
        elif data.lower() == "temperature":
            # returns actual temp in F after converting using convert_temp()
            temp = int(lists["main"]["temp"])
            return f"Actual temperature: {convert_temp(temp)}{DEGREE_SYMBOL}F"
        elif data.lower() == "humidity":
            # returns humidity %
            humidity = lists['main']['humidity']
            return f"Humidity: {humidity}%"
        elif data.lower() == "pressure":
            # returns pressure in psi after converting using convert_pressure
            pressure = int(lists['main']['pressure'])
            return f"Pressure: {(convert_pressure(pressure)):.2f} psi"
        elif data.lower() == "sunrise":
            # returns time of sunrise after converting time useing convert_time
            # to the users time zone
            time = convert_time(lists['sys']['sunrise'], lists["timezone"])
            return f'Time of sunrise: {time.strftime("%I:%M:%S")}'
        elif data.lower() == "sunset":
            # returns time of sunset after converting time useing convert_time
            # to the users time zone
            time = convert_time(lists['sys']['sunset'], lists["timezone"])
            return f'Time of sunset: {time.strftime("%I:%M:%S")}'
        elif data.lower() == "visibility":
            # returns visibility % after converting m to km using convert_distance
            distance = int(lists['visibility'])
            return f"Visibility distance: {convert_distance(distance)} km"
        elif data.lower() == "wind":
            # returns wind speed in mph using convert_speed
            speed = (int(lists['wind']['speed']) )
            return f"Wind speed: {convert_speed(speed):.2f} mph"
        elif data.lower() == "time zone":
            # finds time difference from UTC using timezone()
            timezon = int(lists["timezone"])
            timezon /= 3600
            return f"Timezone: {timezone(timezon)}"
        elif data.lower() == "description":
            # returns the description of the weather at the users location
            description = lists['weather'][0]['description']
            return f"{description}"
        else:
            # if the user doesn't enter valid input, they will be instructed to 
            # enter ex. to show what valid inputs are. 
            return "Enter a correct key word. Enter 'ex' for a list of accepted values"


if __name__ == "__main__":
    main()