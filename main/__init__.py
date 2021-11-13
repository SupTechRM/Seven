<<<<<<< HEAD
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
#
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
#
#
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#
#
# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")
#
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#
#     else:
#         speak("Good Evening!")
#
#     speak("I am Seven . Please tell me how may I help you")
#
#
#
#
#
# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()
#
#
=======
import pyttsx3 #pip install pyttsx3

import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Seven . Please tell me how may I help you")       





if __name__ == "__main__":
    wishMe()
   

        
>>>>>>> 1e88bea48dce26eebd01da1610eadf65bdc6d3d8
