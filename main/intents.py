import random
import spacy
import json
from data.speech.RealtimeSpeech import SpeechSynthesizer
nlp = spacy.load('en_core_web_sm')

with open('./packages.json') as file:
    data = json.load(file)


Dict = {"Command Words": "", "Attributes": ""}


def get_command_words(str):
    doc = nlp(str)

    for ent in doc:
        if ent.pos_ == "VERB":
            Dict["Command Words"] = ent.text
            # print("Command Words: ", Dict["Command Words"])
        else:
            Dict["Attributes"] = ent.text
            # print("Attributes", Dict["Attributes"])


def intents(input_to):
    for intent in data['packages']:
        for pattern in intent['patterns']:
            if pattern.lower() in input_to.split():
                # print("Found")
                # print(intent['tag'])
                response = (random.choice(intent['responses']))
                try:
                    SpeechSynthesizer(
                        response, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                except Exception:
                    pass

                if pattern.lower() in intent['patterns'] and intent['patterns'].index(pattern.lower()) == 0:
                    return intent["tag"]
                else:
                    return intent["tag"]

            else:
                pass
