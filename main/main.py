from data.realtime_mic import takeCommand
from intents import *
from data.SpeechSynthesis import speech_Speak
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
    speech_Speak("Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")
    user_input = takeCommand()
    user_input = user_input.lower()
    intents(user_input)
