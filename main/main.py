""" Packages """
from data.speech.RealtimeSpeech import SpeechSynthesizer
from data.speech.RealtimeMic import takeCommand
import json
import webbrowser
import pywhatkit as kit
import wolframalpha
import requests
import random
from sys import platform
import os



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
app_id = '8QU8RA-TE2GAVWTKL'

class Seven:
    def __init__(self):
        """ Introduce """
        
        """ Wolframalpha """
        self.app_id = '8QU8RA-TE2GAVWTKL'



    def introduction(self, name):
        try:
            SpeechSynthesizer("Hello " + name + ". I am Seven. I am here to assist you with your daily tasks. You can ask me for help.",
                              "data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        except Exception:
            return Exception

    def intents(self, user_input):

        # intent check
        for intent in self.data['packages']:
            # check pattern
            for pattern in intent['patterns']:
                if self.user_input.lower() in pattern.lower():
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

        self.user_input = input("What can I do for you? ")
        self.user_input_link = self.user_input.split()

        try:
            # Search (Default Search Engine)
            if "search" in self.user_input:
                try:
                    # Look for Search and Keep and Empty item
                    user_input = self.user_input.replace("search ", "")

                    # Open link in browser
                    webbrowser.open(
                        'https://www.google.co.in/search?q=' + self.user_input)


                except Exception as SearchException:
                    return SearchException

            # Play video on Youtube
            elif "play" in self.user_input:
                try:
                    # Look for Play and Keep and Empty item
                    user_input = self.user_input.replace("play ", "")

                    # Play the Video
                    kit.playonyt(user_input)

                except Exception as PlayException:
                    return PlayException

            # Open link in browser
            elif "open" in self.user_input:
                # Open a webpage
                try:
                    # Look for Open and Keep and Empty item
                    user_input = self.user_input.replace("open ", "")

                    # Open the webpage
                    webbrowser.open('https://www.' + user_input + '.com')

                except Exception as OpenException:
                    return OpenException

            # Check Weather Data
            elif "weather" in self.user_input:
                try:
                    os.system("python ../core/packages/Weather/Weather.py")

                except Exception as WeatherException:
                    return WeatherException

            elif "corona" in self.user_input or "covid" in self.user_input:
                try:
                    os.system("python ../core/packages/CoronaInfo/coronaGet.py")

                except Exception as CovidException:
                    return CovidException

            # Network/Internet Check
            elif "internet" in self.user_input or "network" in self.user_input:
                try:
                    SpeechSynthesizer("Checking your network speed",
                                      "data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                    os.system("python ../core/packages/Speedtest/Speedtest.py")

                except Exception as NetworkException:
                    return NetworkException

            # See for Todo List
            elif "todo" in self.user_input or "to do" in self.user_input:
                try:
                    os.system("python ../core/packages/Todo/todo.py")

                except Exception as TodoException:
                    return TodoException

            # Get News
            elif "news" in self.user_input:
                try:
                    os.system("python ../core/packages/News/NewsFromBBC.py")

                except Exception as NewsException:
                    return NewsException

            ####################################
            # GESTURE
            ####################################

            # Volume Controller
            elif "volume controller" in self.user_input or "volume" in self.user_input:

                try:
                    if platform == "darwin":
                        os.system(
                            "python ../models/gesture/core/ControllerVolumeMac/VolumeHandControlAdvanced.py")
                    elif platform == "win32":
                        os.system(
                            "python ../models/gesture/core/ControllerVolume/VolumeController.py")

                except Exception as ControllerVolumeException:
                    return ControllerVolumeException

            elif "mouse controller" in self.user_input or "mouse" in self.user_input:
                try:
                    os.system(
                        "python ../models/gesture/core/VirtualMouse/VirtualMouse.py")
                except Exception as ControllerMouseException:
                    return ControllerMouseException

            #############################
            # """ Functions """
            #############################

            elif "exit" in self.user_input or "stop":
                exit()

            elif "help" in self.user_input:
                pass
            else:
                try:
                    client = wolframalpha.Client(self.app_id)
                    res = client.query(self.user_input)
                    ans = next(res.results).text
                    print(ans)
                    SpeechSynthesizer(
                        ans, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                except Exception:
                    response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                                            app_id + "&input=" + self.user_input + "&output=json")
                    jsonresp = response.json()
                    outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
                    SpeechSynthesizer(outcome, path="data/speech/empyrean-app-332014-6fdfdc87b1df.json")
        except Exception:
            pass

if __name__ == "__main__":
    while True:
        seven = Seven()
        seven.main()
