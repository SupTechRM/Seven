#########################
# Weather
#########################

import requests
from pytemp import pytemp
import os
import playsound
import random
from gtts import gTTS

# Instantiates a client


def SpeechSynthesizer(audio):
    response = gTTS(text=audio, lang="en")
    # The response's audio_content is binary.
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    response.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# Enter your API key here
api_key = "f726177bc0a3668ac48870d798d9a623"

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def getLocation():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city_name = data['city']
    return city_name


def getWeather(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

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
        pass


city = getLocation()
getWeather(city)