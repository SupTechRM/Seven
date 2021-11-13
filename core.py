import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import playsound
from datetime import date

from main.data.speech.RealtimeMic import takeCommand
import os
import speech_recognition as sr


path = './user.json'

existence = os.path.exists(path)

if existence:
    opened = open('user.json')
    data = json.load(opened)
    opened.close()
    os.chdir("main")
    os.system("python3 main.py")
else:
    apikey = '3k6i8lvhuVL0xvMjdc3H0Fe5wciOJ-qN--UhqVPQNsev'
    url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c0e720ca-1373-4cbb-959f-bae7d48795e0'

    authenticator = IAMAuthenticator(apikey)
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url(url)
    with open('speech.mp3', 'wb') as audio_file:

        res = tts.synthesize("Oh, Looks like you are a new user. I am Seven, I will just initialize, wait a few seconds.", accept='audio/mp3',
                             voice='en-US_KevinV3Voice').get_result()
        audio_file.write(res.content)

    playsound.playsound('speech.mp3')


    # use the microphone as source for input.
    with sr.Microphone() as source:

        r = sr.Recognizer()
        # the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=0.2)

        # listens for the user's input
        with open('speech.mp3', 'wb') as audio_file:
            res = tts.synthesize("Please spell your name", accept='audio/mp3',
                                 voice='en-US_KevinV3Voice').get_result()
            audio_file.write(res.content)

        playsound.playsound('speech.mp3')
        audio = r.listen(source)

        # Using ggogle to recognize audio
        inputtext = r.recognize_google(audio)
        inputtext = inputtext.lower()
        inputtext = inputtext.replace(" ", "")

        dateCreated = str(date.today().day) + "/" + str(date.today().month) + "/" + str(date.today().year)
        jsonData = {"name": inputtext, "dateCreated": dateCreated}
        jsonString = json.dumps(jsonData)
        jsonFile = open("user.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

    os.chdir("app")
    os.system("npm start")



