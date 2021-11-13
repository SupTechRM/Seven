import os

import playsound

from data.speech.RealtimeMic import takeCommand
from intents import *
from data.speech.RealtimeSpeech import SpeechSyntesizer
import json

# Take Speech Recognition input and process it realtime running a main function
# main function will take the query
# query is sample input from which intent will be called, the modules will be runned
# speech synthesis as a response


#####################################
# Main Function
#####################################
file = open('../user.json')

data = json.load(file)
name = data['name']

file.close()

while True:
    SpeechSyntesizer("Welcome " + name +
                 ". As I have already introduced myself, I am Seven. You can now as me for help.")
    playsound.playsound("speech.mp3")
    user_input = takeCommand()
    user_input = user_input.lower()
    foundpackage = intents(user_input)
    print(type(foundpackage))
    if foundpackage:
        os.chdir("../core/packages/" + str(foundpackage))
        os.system("python3 " + str(foundpackage) + ".py")