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
import os
import playsound
from data.speech.RealtimeSpeech import SpeechSyntesizer
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
                filename = 'speech' + str(random.randint(1, 100)) + '.mp3'
                SpeechSyntesizer(response)

                if pattern.lower() in intent['patterns'] and intent['patterns'].index(pattern.lower()) == 0:
                    return intent["tag"]
                else:
                    return intent["tag"]

            else:
                pass
