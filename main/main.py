<<<<<<< HEAD
from data.realtime_mic import takeCommand
from intents import *
from data.SpeechSynthesis import speech_Speak
import json
=======
from data.RealtimeMic import takeCommand
from intents import intents
>>>>>>> 1e88bea48dce26eebd01da1610eadf65bdc6d3d8

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
<<<<<<< HEAD
    speech_Speak("Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")
    user_input = takeCommand()
=======
    user_input = input("Enter: ")
>>>>>>> 1e88bea48dce26eebd01da1610eadf65bdc6d3d8
    user_input = user_input.lower()
    intents(user_input)