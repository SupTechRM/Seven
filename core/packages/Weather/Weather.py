#########################
# Weather
#########################

import requests
import json
from pytemp import pytemp

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import playsound

apikey = '3k6i8lvhuVL0xvMjdc3H0Fe5wciOJ-qN--UhqVPQNsev'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c0e720ca-1373-4cbb-959f-bae7d48795e0'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


def SpeechSyntesizer(audio):
    try:
        with open('speech.mp3', 'wb') as audio_file:
            res = tts.synthesize(audio, accept='audio/mp3',
                                 voice='en-GB_JamesV3Voice').get_result()
            audio_file.write(res.content)

    except Exception as e:
        print(e)
        with open('speech.mp3', 'wb') as audio_file:
            res = tts.synthesize(audio, accept='audio/mp3',
                                 voice='en-GB_JamesV3Voice').get_result()
            audio_file.write(res.content)



# Enter your API key here
api_key = "f726177bc0a3668ac48870d798d9a623"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def getLocation():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city_name = data['city']
    location = data['loc'].split(',')

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
        print(json.dumps(temperature_max))

        SpeechSyntesizer("Current Temperature: " + str(round(current_temperature, 2)))
        SpeechSyntesizer("Maximum Temperature: " + str(round(temperature_max, 2)))
        SpeechSyntesizer("Minimum Temperature: " + str(round(temperature_min, 2)))
        SpeechSyntesizer("Humidity: " + str(current_humidity) + "%")
        # return utils.translate("Weather Successfully Accessed")


    else:
        # return utils.translate("City not Found")
        pass

city = getLocation()
getWeather(city)