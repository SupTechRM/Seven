""" Packages """
from data.speech.RealtimeSpeech import SpeechSynthesizer
from data.speech.RealtimeMic import takeCommand
import language_tool_python
import json
import webbrowser
import pywhatkit as kit
import wolframalpha
import requests
import random
from sys import platform
import os

tool = language_tool_python.LanguageTool('en-US')


""" Speech Data """

#####################################
# Main Function
#####################################

# Gather Variable Data

""" Define Name """
file = open('../user.json')

data = json.load(file)
name = data['name']

file.close()

""" Define Wolframalpha ID """
app_id = '47P9L8-VHY6GJ54G8'

# Introduce User (Random Generated)

# SpeechSynthesizer("Welcome " + name + ". As I have already introduced myself, I am Seven. You can now as me for help.",
#                   "data/speech/empyrean-app-332014-6fdfdc87b1df.json")


class Seven:
    def __init__(self):
        """ Introduce """

        self.user_input = takeCommand()
        self.user_input_link = self.user_input.lower().split()

        """ Wolframalpha """
        self.app_id = '47P9L8-VHY6GJ54G8'

        """ Main Proccess """
        self.main()

    def introduction(self, name):
        try:
            SpeechSynthesizer("Hello " + name + ". I am Seven. I am here to assist you with your daily tasks. You can ask me for help.",
                              "data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        except Exception:
            return Exception

    def intents(self, user_input):

        # intent check
        for intent in data['packages']:
            # check pattern
            for pattern in intent['patterns']:
                if self.user_input.lower().lower() in pattern.lower():
                    response = (random.choice(intent['responses']))
                    try:
                        SpeechSynthesizer(
                            response, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                    except Exception:
                        print(Exception)

                    if pattern.lower() in intent['patterns'] and intent['patterns'].index(pattern.lower()) == 0:
                        pass
                    else:
                        return intent["tag"]

                else:
                    pass

    def main(self):
        try:
            while True:

                # Search (Default Search Engine)
                if "search" in self.user_input.lower():
                    try:
                        # Look for Search and Keep and Empty item
                        user_input = self.user_input.lower().replace("search ", "")

                        # Open link in browser
                        webbrowser.open(
                            'https://www.google.co.in/search?q=' + self.user_input.lower())
                        os.system("python main.py")

                    except Exception as SearchException:
                        return SearchException

                # Play video on Youtube
                elif "play" in self.user_input.lower():
                    try:
                        # Look for Play and Keep and Empty item
                        user_input = self.user_input.lower().replace("play ", "")

                        # Play the Video
                        kit.playonyt(user_input)

                    except Exception as PlayException:
                        return PlayException

                # Open link in browser
                elif "open" in self.user_input.lower():
                    # Open a webpage
                    try:
                        # Look for Open and Keep and Empty item
                        user_input = self.user_input.lower().replace("open ", "")

                        # Open the webpage
                        webbrowser.open('https://www.' + user_input + '.com')

                        #

                    except Exception as OpenException:
                        return OpenException

                # Check Weather Data
                elif "weather" in self.user_input.lower():
                    try:
                        os.system("python ../core/packages/Weather/Weather.py")

                    except Exception as WeatherException:
                        return WeatherException

                elif "corona" in self.user_input.lower() or "covid" in self.user_input.lower():
                    try:
                        os.system(
                            "python ../core/packages/CoronaInfo/coronaGet.py")

                    except Exception as CovidException:
                        return CovidException

                # Network/Internet Check
                elif "internet" in self.user_input.lower() or "network" in self.user_input.lower():
                    try:
                        SpeechSynthesizer(
                            "Checking your network speed", path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                        os.system(
                            "python ../core/packages/Speedtest/Speedtest.py")

                    except Exception as NetworkException:
                        return NetworkException

                # See for Todo List
                elif "todo" in self.user_input.lower() or "to do" in self.user_input.lower():
                    try:
                        os.system("python ../core/packages/Todo/todo.py")

                    except Exception as TodoException:
                        return TodoException

                # Get News
                elif "news" in self.user_input.lower():
                    try:
                        os.system(
                            "python ../core/packages/News/NewsFromBBC.py")

                    except Exception as NewsException:
                        return NewsException

                ####################################
                # GESTURE
                ####################################

                # Volume Controller
                elif "volume controller" in self.user_input.lower() or "volume" in self.user_input.lower():

                    try:
                        if platform == "darwin":
                            os.system(
                                "python ../models/gesture/core/ControllerVolumeMac/VolumeHandControlAdvanced.py")
                        elif platform == "win32":
                            os.system(
                                "python ../models/gesture/core/ControllerVolume/VolumeController.py")

                    except Exception as ControllerVolumeException:
                        return ControllerVolumeException

                elif "mouse controller" in self.user_input.lower() or "mouse" in self.user_input.lower():
                    try:
                        os.system(
                            "python ../models/gesture/core/VirtualMouse/VirtualMouse.py")
                    except Exception as ControllerMouseException:
                        return ControllerMouseException

                #############################
                # """ Functions """
                #############################

                elif "exit" in self.user_input.lower() or "stop":
                    exit()

                elif "help" in self.user_input.lower():
                    pass

                else:
                    client = wolframalpha.Client(self.app_id)
                    res = client.query(self.user_input.lower())
                    ans = next(res.results).text
                    SpeechSynthesizer(
                        ans, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        except Exception:
            response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                                    app_id + "&input=" + user_input + "&output=json")
            jsonresp = response.json()
            outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
            if outcome:
                SpeechSynthesizer(
                    outcome, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")


if __name__ == "__main__":
    seven = Seven()
    seven.main()
