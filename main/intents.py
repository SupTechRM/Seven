from genericpath import sameopenfile
import json
import random
import numpy
import spacy
import threading
import string
import re
import sys
import json
import playsound

from data.SpeechSynthesis import *
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import playsound

apikey = '3k6i8lvhuVL0xvMjdc3H0Fe5wciOJ-qN--UhqVPQNsev'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c0e720ca-1373-4cbb-959f-bae7d48795e0'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

# from core import packages
# from core.packages.Wolframalpha.WolframAlpha import QuestionSearchByMethod

nlp = spacy.load('en_core_web_sm')

with open('packages.json') as file:
    data = json.load(file)


Dict = {"Command Words": "", "Attributes": ""}


def get_command_words(str):
    doc = nlp(str)

    for ent in doc:
        if ent.pos_ == "VERB":
            Dict["Command Words"] = ent.text
            print("Command Words: ", Dict["Command Words"])
        else:
            Dict["Attributes"] = ent.text
            print("Attributes", Dict["Attributes"])


def intents(input_to):
    for intent in data['packages']:
        for pattern in intent['patterns']:
            if pattern.lower() in input_to.split():
                print("Found")
                print(intent['tag'])
                response = (random.choice(intent['responses']))
                with open('speech.mp3', 'wb') as audio_file:
                    res = tts.synthesize(response, accept='audio/mp3',
                                        voice='en-GB_JamesV3Voice').get_result()
                    audio_file.write(res.content)
                print(response)
                playsound.playsound('speech.mp3')

                if pattern.lower() in intent['patterns'] and intent['patterns'].index(pattern.lower()) == 0:
                    return intent["tag"]
                    if intent["tag"] == "CoronaInfo":
                        get_command_words(input_to)
                    else:
                        get_command_words(input_to)
                else:
                    return intent["tag"]
            else:
                """ Execute Wolframalpha """
                pass
