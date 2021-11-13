from data.speech.RealtimeMic import takeCommand
from intents import *
from data.speech.RealtimeSpeech import SpeechSyntesizer
import json
import webbrowser
import lib
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
    try:
        SpeechSyntesizer("Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")
    except:
        SpeechSyntesizer(
            "Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")

    user_input = takeCommand()
    user_input = user_input.lower()
    link = user_input.split()
    intents(user_input)

    if user_input.startswith('search '):
        try:
            link = '+'.join(link[1:])
            say = link.replace('+', ' ')
            # print(link)
            print("searching on google for " + say)
            webbrowser.open('https://www.google.co.in/search?q=' + link)
        
        except Exception as e:
            print(str(e))

