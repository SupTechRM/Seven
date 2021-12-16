""" Packages """

# Speech Library Import
from data.speech.RealtimeSpeech import SpeechSynthesizer
from data.speech.RealtimeMic import Stream_Speech

# Module base import 
import json
import webbrowser
import pywhatkit as kit
import wolframalpha
import random
from sys import platform
import os
import ssl
import time

# Import Seven Functions
# from lib.introduction.introduction import IntroClass
# from lib.tryExec.tryExec import TryExample

""" ssl context """
ssl._create_default_https_context = ssl._create_unverified_context


#####################################
# Main Function
#####################################

# Gather Variable Data

""" Define Name """
file = open('../user.json')

data = json.load(file)
name = data['name']

file.close()

""" Seven Class (Run Data -> Main) """
class Seven:
    def __init__(self):

        """ Wolframalpha """
        file = open('../user.json')
        data = json.load(file)
        self.app_id = data['wolframalpha_api']

    def speak(self, data):
        SpeechSynthesizer(data)
        print(data)

    def wolframalpha(self, user_input):
        try:
            # Define Wolfram Client
            client = wolframalpha.Client(self.app_id)
            res = client.query(user_input)
            answer = next(res.results).text
           
            # Define a Whitelisted
            whiteListed = ["Wolfram|Alpha", "Wolframlpha", "Wolfram alpha", "Wolfram", "Stephen"]
            
            # if answer in whiteListed
            if any(x in answer for x in whiteListed):
                # Check for "name" or "created" or "developed" or "built" in x
                if any(x in answer for x in ["name", "created", "developed", "built", "birthday", "made"]):
                    return self.speak("I am Seven. I was created by Rishabh Mishra, Shubham Mishra, and Sarthak Rawool. To be honest the day I was finally considered in a beta version was November 15th 2021 IST 21:12, Do I know the seconds? No I don't know. I like to call that my starting point. Since then I've learned a lot. ")
                answer = "I'm sorry, I can't answer that"
            else:
                answer = answer

            # Speak Answer
            self.speak(answer)

        except Exception:
            response = random.choice(["Hey, Couldn't find an answer! ", "I don't know what you're talking about. ", "Ok, No answer to that."])
            self.speak("Would you like me to search this on google? ")

            # Create the Speech Object and Listen based on State
            self.object = Stream_Speech()
            self.user_input = self.object.takeCommand()

            if "yes" in self.user_input or "yeah" in self.user_input or "would love it" in self.user_input:
                webbrowser.open("https://www.google.com/search?q=" + user_input)
                response = random.choice(["K, I got your back.", "Sure thing, Right Away.", "Alright, I'll do it."])
                self.speak(response)
            else:
                response = random.choice(["Ok I'm here if you need anything else", "Ok my man, I'm here for any other help.", "Sorry if I did not get that. I must have missed a keyword, you can try again. ", "Hey I'm here, alright."])
                self.speak("Ok I'm here if you need anything else")

    def main(self):
        
        # Create the Speech Object and Listen based on State
        self.object = Stream_Speech()
        self.user_input = self.object.takeCommand()
        print(self.user_input)
        
        # Proccess user spoken data
        self.user_input = self.user_input.lower()
        self.user_input_link = self.user_input.split()

        try:
            # Search (Default Search Engine)
            if "search" in self.user_input:
                try:
                    # Look for Search and Keep and Empty item
                    user_input = self.user_input.replace("search ", "")

                    # Open link in browser
                    webbrowser.open(
                        'https://www.google.co.in/search?q=' + user_input )

                    # Speak out
                    response = random.choice([f"Here is what I found for {user_input}", f"Oookay, searching for {user_input} in your browser", "Well that's factual? ", "Got It", "I'm on it",
                                              f"So, {user_input}. Something dear to you I presume. ", "Interesting", "My man, Fantastic interest. I'm searching..", "Should I search or not? I'll search. "])
                    self.speak(response)

                except Exception as SearchException:
                    self.speak(SearchException)

            # Play video on Youtube
            elif "play" in self.user_input:
                try:
                    # Look for Play and Keep and Empty item
                    user_input = self.user_input.replace("play ", "")

                    # Play the Video
                    kit.playonyt(user_input)

                    # Speak out
                    response = random.choice([f"Playing {user_input} on youtube", "God, That's got to be fantastic", "Man I love that", "Damn, that's interesting", "You've got some taste, eh? ", "I watched it, it's spectacular.",
                                              "You watched that? I watched it a few ages ago. Burn. My jokes are presumably the best on the planet.", "O'l Sakes, That's the art", f"That was beatiful. In the time of playing it for you, I finished the whole video. "])
                    self.speak(response)

                except Exception as PlayException:
                    self.speak(PlayException)

            # Open link in browser
            elif "open" in self.user_input:
                # Open a webpage
                try:
                    # Look for Open and Keep and Empty item
                    user_input = self.user_input.replace("open ", "")

                    # Open the webpage
                    webbrowser.open('https://www.' + user_input + '.com')

                    # Speak out
                    response = random.choice([f"Opening {user_input}. Great website. ", "I mostly do my work there. It's a haven of learning.", f"Anyhows, {user_input}, pretty popular.", "Bleep that website. Horrible UI. ",
                                              "It's good. Could use a bit of designing, but it's fine. Well content is what matters.", f"Ok, I'mma open this {user_input} for you.", "You're boring me, kid."])
                    self.speak(response)

                except Exception as OpenException:
                    return OpenException

            # Check Weather Data
            elif "weather" in self.user_input:
                try:
                    os.system("python ../core/packages/Weather/Weather.py")
                    response = random.choice(
                        ["I'm on it. ", "Getting Weather Info", "You know, you have a delightful weather. For me it's just digital heat, sometimes cold. ", "Weather, my favourite thing to use as an excuse. "])
                    self.speak()
                except Exception as WeatherException:
                    return WeatherException

            elif "corona" in self.user_input or "covid" in self.user_input:
                try:
                    os.system("python ../core/packages/CoronaInfo/coronaGet.py")
                    response = random.choice(["I'm on it. ", "Getting Corona Info", "Hey Stay Safe", "Wear your mask when you go outside man",
                                              f"{name}, you've got to take care of yourself.", "Wishing your family and you to stay safe and when in problems to be able to face it."])
                    self.speak(response)

                except Exception as CovidException:
                    return CovidException

            # Network/Internet Check
            elif "internet" in self.user_input or "network" in self.user_input:
                try:
                    SpeechSynthesizer("Checking your network speed")
                    os.system("python ../core/packages/Speedtest/Speedtest.py")
                    response = random.choice(["Checking your internet", "That's delicate.", "Wonderful.",
                                              "Wonder how I process stuff. Whoo! ", "Checking results... So far so good."])
                    self.speak(response)

                except Exception as NetworkException:
                    return NetworkException

            # See for Todo List
            elif "exit" in self.user_input or "bye" in self.user_input:
                response = random.choice(["Okay, Bye!", "See you later.", "Have a nice day.",
                                              "Adios! ", "Bye!", "Good Bye!"])
                SpeechSynthesizer(response)
                exit()
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
            elif "sleep" in self.user_input or "bye" in self.user_input or "stop" in self.user_input:
                response = random.choice(["Well, That's my cue.", "Adios", f"See you, {name}. I'll be back in a bit. "])
                self.speak(response)
                os.system("python ../initial.py")

            elif "help" in self.user_input or "documentation" in self.user_input:
                try:
                    os.system("python ../core/packages/Help/Help.py")
                except Exception as HelpException:
                    return HelpException
                response = random.choice(["Sure opening the documentation", "Ok", "Right helping you out."])
                self.speak(response)

            else:
                self.wolframalpha(self.user_input)

        except Exception as e:
            print(e)


# introObj = IntroClass()
# tryExampleObj = TryExample()

if __name__ == "__main__":
    while True:
        seven = Seven()
        seven.main()
