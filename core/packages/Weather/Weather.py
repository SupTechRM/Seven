#########################
# Weather
#########################

import requests
from pytemp import pytemp
import os
import playsound
import random
from gtts import gTTS
import json

# Instantiates a client


def SpeechSynthesizer(audio):
    response = gTTS(text=audio, lang="en")
    # The response's audio_content is binary.
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    response.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# Enter your API key here

def getLocation():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city_name = data['city']
    return city_name


def getWeather(city_name):
    file = open('../core/packages/Weather/user.json')
    data = json.load(file)
    api_key = data['weather_api']
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404" and x["cod"] != "401":

        y = x["main"]

        current_temperature = y["temp"]
        current_temperature = pytemp(current_temperature, 'kelvin', 'celsius')

        temperature_min = y["temp_max"]

        temperature_min = pytemp(temperature_min, 'kelvin', 'celsius')

        temperature_max = y["temp_min"]

        temperature_max = pytemp(temperature_max, 'kelvin', 'celsius')
        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        print("Current Temperature: " + str(round(current_temperature, 2)))
        print("Maximum Temperature: " + str(round(temperature_max, 2)))
        print("Minimum Temperature: " + str(round(temperature_min, 2)))
        print("Humidity: " + str(current_humidity) + "%")
    else:
        print("Sorry, Something Went Wrong...")
        pass


city = getLocation()
getWeather(city)