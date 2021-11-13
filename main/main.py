import playsound

from data.speech.RealtimeMic import takeCommand
from intents import *
from data.speech.RealtimeSpeech import SpeechSyntesizer
import json
import webbrowser
import lib
import os

#####################################
# Main Function
#####################################
file = open('../user.json')

data = json.load(file)
name = data['name']

file.close()

while True:
    try:
        SpeechSyntesizer(
            "Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")
    except:
        SpeechSyntesizer(
            "Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.")

    # playsound.playsound("speech.mp3")
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

            # Weather

    elif "weather" in user_input:
        try:
            os.system("python core/packages/Weather/Weather.py")

        except Exception as a:
            print(a)

            # Corona

    elif "corona" in user_input or "covid" in user_input:
        try:
            os.system("python core/packages/CoronaInfo/coronaGet.py")

        except Exception as b:
            print(b)

            # SpeedTest

    elif "test" in user_input:
        try:
            os.system("python core/packages/Speedtest/Speedtest.py")

        except Exception as c:
            print(c)

            # To Do

    elif "todo" in user_input:
        try:
            os.system("python core/packages/Todo/todo.py")

        except Exception as d:
            print(d)

            # News

    elif "news" in user_input:
        try:
            os.system("python core/packages/News/NewsFromBBC.py")

        except Exception as e:
            print(e)

    else:
        try:
            with open("apiData.json") as file:
                data = json.load(file)
                data["input"] = user_input
                json.dump(data, open("apiData.json", "w"), indent=4)
            os.system("python3 core/packages/Wolframalpha/WolframAlpha.py")
            print("Run")
        except Exception as e:
            print(e)










