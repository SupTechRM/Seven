# #######################
# """
# Import Packages -> Core.py
# """
# #######################

import json
import playsound
from datetime import date
import os
import speech_recognition as sr
import random
import time
import datetime
import json
from main.data.speech.RealtimeSpeech import SpeechSynthesizer


# Define A Path for Json File Containing DB Data for User
path = './user.json'

# existence(variable -> checking for existence of path)
existence = os.path.exists(path)

# while existence
if existence:
    # open(variable -> opening the file)
    opened = open('user.json')

    # data(variable -> reading the file)
    data = json.load(opened)

    # close opened
    opened.close()

    # cd main/python main.py (redirect to main)
    os.chdir("main")
    os.system("python main.py")

# if not existence(new user)
else:
    # Define Variable for Speech Synthesis
    # Open mp3 file

    # Play File
    SpeechSynthesizer("A new user I see. Welcome. Welcome to Seven. Let me introduce myself. I'm Seven. I'm a damn brilliant guy. That's all. Here let me get you through setup. Spell your name.", path="main/data/speech/empyrean-app-332014-6fdfdc87b1df.json")

    while True:

        # use the microphone as source for input.
        with sr.Microphone() as source:

            # Define the Recognizer
            r = sr.Recognizer()

            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)

            # Use Pause Threshold
            r.pause_threshold = 1

            time.sleep(2)
            print("Listening....")
            audio = r.listen(source)

            # Using google to recognize audio
            inputtext = r.recognize_google(audio)

            # Lower input text
            inputtext = inputtext.lower()

            # Replace empty spaces
            inputtext = inputtext.replace(" ", "")
            if inputtext:
                SpeechSynthesizer(
                    f"Is {inputtext} your name? If Yes(Press y), If No(Press n)", path="./main/data/speech/empyrean-app-332014-6fdfdc87b1df.json")

                checkTrue = input("Is your name {0}? (y/n)".format(inputtext))
                if checkTrue == "y":
                    dateCreated = str(datetime.date.today().day) + "/" + \
                        str(datetime.date.today().month) + \
                        "/" + str(datetime.date.today().year)
                    jsonData = {"name": inputtext, "dateCreated": dateCreated}

                    # Dump Data
                    jsonString = json.dumps(jsonData)

                    # Open Json File
                    jsonFile = open("user.json", "w")

                    # Write data
                    jsonFile.write(jsonString)
                    jsonFile.close()

                else:
                    os.system("python core.py")

            # Define variables for user.json
            dateCreated = str(datetime.date.today().day) + "/" + \
                str(datetime.date.today().month) + "/" + str(datetime.date.today().year)
            jsonData = {"name": inputtext, "dateCreated": dateCreated}

            # Dump Data
            jsonString = json.dumps(jsonData)

            # Open Json File
            jsonFile = open("user.json", "w")

            # Write data
            jsonFile.write(jsonString)
            jsonFile.close()

        # Begin the app for marketing/explaining purposes
        SpeechSynthesizer(
            f"{inputtext}, Follow through the documentation, and once you are done, just close the window and I'll be ready.", path="main/data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        os.chdir("app")
        os.system("npm start")

        os.system("python main/main.py")
