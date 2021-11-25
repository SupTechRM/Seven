""" Packages """
from data.speech.RealtimeSpeech import SpeechSynthesizer
from data.speech.RealtimeMic import Stream_Speech
import json
import webbrowser
import pywhatkit as kit
import wolframalpha
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
        self.introduction()
        
        """ Wolframalpha """
        self.app_id = '8QU8RA-TE2GAVWTKL'

        """ Define Listening State """
        self.state = True

    def speak(self, data):
        path = "data/speech/empyrean-app-332014-6fdfdc87b1df.json"
        SpeechSynthesizer(data, path)
        print(data)

    def introduction(self, name):
        try:
            response = random.choice([f"Hey {name}, I'm Seven. Here to help you out.", "Hey Dude, I'm ready to help you out.", f"Hey Buns, (insert laughing sound), {name}, How you doin'? I am ready to help"])
            self.speak(response)
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
    
    def wolframalpha(self, user_input):
        client = wolframalpha.Client(self.app_id)
        res = client.query(user_input)
        try:
            answer = next(res.results).text
            self.speak(answer)
        except:
            response = random.choice(["Hey, Couldn't find an answer! ", "I don't know what you're talking about. ", "Ok, No answer to that."])
            self.speak("Would you like me to search this on google? ")

            # Create the Speech Object and Listen based on State
            self.object = Stream_Speech()
            self.user_input = self.object.takeCommand(self.state)

            if "yes" in self.user_input or "yeah" in self.user_input or "would love it" in self.user_input:
                webbrowser.open("https://www.google.com/search?q=" + user_input)
                response = random.choice(["K, I got your back.", "Sure thing, Right Away.", "Alright, I'll do it."])
                self.speak(response)
            else:
                self.speak("Ok I'm here if you need anything else")

    def main(self):
        
        # Create the Speech Object and Listen based on State
        self.object = Stream_Speech()
        self.user_input = self.object.takeCommand(self.state)
        
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
                    SpeechSynthesizer("Checking your network speed",
                                      "data/speech/empyrean-app-332014-6fdfdc87b1df.json")
                    os.system("python ../core/packages/Speedtest/Speedtest.py")
                    response = random.choice(["Checking your internet", "That's delicate.", "Wonderful.",
                                              "Wonder how I process stuff. Whoo! ", "Checking results... So far so good."])
                    self.speak(response)

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

            elif "exit" in self.user_input:
                exit()
            
            elif "help" in self.user_input:
                try:
                    os.system("python ../core/packages/Help/Help.py")
                except Exception as HelpException:
                    return HelpException

            elif "start" in self.user_input or "wake up" in self.user_input:
                self.state = True

                response = random.choice(["Back to Work! ", "I'm here", "You know, I would normally say at your service, but you did kind of wake me from my peace sleep. It's ok, Go ahead. "])
                self.speak(response)
            
            elif "sleep" in self.user_input or "stop" in self.user_input:
                self.state = False
                response = random.choice(["Well, That's my cue.", "Adios", "See you, {name}. I'll be back in a bit. "])
                self.speak(response)

            else:
                self.wolframalpha(self.user_input)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    while True:
        seven = Seven()
        seven.main()
