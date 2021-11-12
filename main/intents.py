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
            if pattern.lower() in input_to.split() or pattern.lower().split() in input_to.split():
                print("Found")
                print(intent['tag'])
                print(random.choice(intent['responses']))
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
