
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

class Initialisation:
    def __init__(self):

        # Define A Path for Json File Containing DB Data for User
        self.path = './user.json'
        
        # existence(variable -> checking for existence of path)
        self.existence = os.path.exists(self.path)

        # check_existence
        self.check_existence()
    
    def check_existence(self):
        # while existence
        if self.existence:
            self.runMain()
        
        # while existence not true
        else:
            # self.welcomeUser()
            self.yourName()
    
    """ Task Execution """

    def speakData(self, data):
        path = "main/data/speech/empyrean-app-332014-6fdfdc87b1df.json"
        # SpeechSynthesizer(data, path)
        print(data)

    def listen_Data(self):
        
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source:

                # Define the Recognizer
                r = sr.Recognizer()

                # the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=0.2)

                # Use Pause Threshold
                r.pause_threshold = 1

                audio = r.listen(source)

                # Using google to recognize audio
                inputtext = r.recognize_google(audio)

                # Lower input text
                inputtext = inputtext.lower()

                # Replace empty spaces
                inputtext = inputtext.replace(" ", "")

                return inputtext

        except Exception as e:
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            return self.listen_Data()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service{0}".format(e))

    def db_save(self, inputtext):

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
    
    def startDocumentation(self, inputtext):
        # Begin the app for marketing/explaining purposes
        self.speakData(
            f"{inputtext}, Follow through the documentation, and once you are done, just close the window and I'll be ready.")
        os.chdir("app")
        os.system("npm start")


    """ Proccess Execution """
    def runMain(self):
        # json_file(variable -> opening the file)
        with open(self.path) as json_file:

            # data(variable -> reading the file)
            data = json.load(json_file)
            
            # close json_file
            json_file.close()

            # cd main/python main.py (redirect to main)
            os.chdir("main")
            os.system("python main.py")
    
    def welcomeUser(self):
        # welcome_user(variable -> welcome user)
        # Introduce Seven

        self.speakData("A new user I see. Welcome. Welcome to Seven. Let me introduce myself. I'm Seven. I'm a damn brilliant guy. That's all. Here let me get you through setup. ")


    def yourName(self):
        # your_name(variable -> your name)
        # Introduce your name

        self.speakData("What is your name?")

        # your_name(variable -> your name)
        # Get your name

        self.your_name = self.listen_Data()

        if self.your_name:
            self.speakData("Is {} your name? ".format(self.your_name))
            
            self.your_name_confirm = self.listen_Data()
            if "yes" in self.your_name_confirm or "yeah" in self.user_input:
                self.speakData("Okay. Let's get started. ")
                self.db_save(self.your_name)
                self.startDocumentation(self.your_name)
                os.system("python main/main.py")


            else:
                self.yourName()





###############################
# Run Intialiasation Process
###############################

Initialisation = Initialisation()
