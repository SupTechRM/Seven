from data.speech.RealtimeMic import takeCommand
from intents import *
from data.speech.RealtimeSpeech import SpeechSynthesizer
import json
import webbrowser
import os
import pywhatkit as kit
import wolframalpha
import requests

#####################################
# Main Function
#####################################

file = open('../user.json')

data = json.load(file)
name = data['name']

file.close()

app_id = '47P9L8-VHY6GJ54G8'


# SpeechSynthesizer("Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.",
#                   "data/speech/empyrean-app-332014-6fdfdc87b1df.json")


while True:

    user_input = takeCommand()
    user_input = user_input.lower()
    link = user_input.split()
    intents(user_input)

    if user_input.startswith('search ') or 'search' in user_input:
        try:
            link = '+'.join(link[1:])
            print(link)
            say = link.replace('+', ' ')
            webbrowser.open('https://www.google.co.in/search?q=' + link)

        except Exception as e:
            print(str(e))

            # Weather
    elif user_input.startswith('play ') or "play" in user_input:
        try:
            link = '+'.join(link[1:])
            say = link.replace('+', ' ')
            # print(link)
            kit.playonyt(say)
        except Exception as e:
            print(str(e))

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

    elif "volume controller" in user_input:
        try:
            os.system("python Seven/models/gesture/core/GestureExecute.py")
        except Exception as e:
            print(e)
    
    elif "mouse controller" in user_input:
        try:
            os.system("python Seven/models/gesture/core/GestureExecute.py")
        except Exception as e:
            print(e)
    
    elif "mouse controller" in user_input:
        try:
            os.system("python Seven/models/gesture/core/GestureExecute.py")
        except Exception as e:
            print(e)
    
    elif "exit" in user_input or "stop":
        exit()
    
    else:
        try:
            client = wolframalpha.Client(app_id)
            res = client.query(user_input)
            ans = next(res.results).text
            SpeechSynthesizer(ans, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        except Exception:
            response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                                    app_id + "&input=" + user_input + "&output=json")
            jsonresp = response.json()
            outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
            SpeechSynthesizer(outcome, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")

