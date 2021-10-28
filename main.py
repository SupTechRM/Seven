import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as sp
import datetime
import os
# import simpleaudio as sa



r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

def speak(stringspeak):
    sp.speak(stringspeak)

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  ")

    else:
        speak("Good Evening  ")

wishme()

with sr.Microphone() as source:
    speak("How may I help you today?")
    audio = r3.listen(source)

if 'Google' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    with sr.Microphone() as source:
        speak("Search your query.")
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            speak(get)
            wb.get().open_new(url + get)
        except sr.UnknownValueError:
            speak('error')
        except sr.RequestError as e:
            speak('failed'.format(e))
elif 'GitHub' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.github.com/'
    with sr.Microphone() as source:
        speak("Do you want to search anything? Say 'no' if not.")
        audio = r2.listen(source)
        if 'no' in r2.recognize_google(audio):
            wb.get().open_new(url)
            speak("Okay, opening...")
    try:
        get = r2.recognize_google(audio)
        speak(get)
        url = "https://www.github.com/search?q="
        wb.get().open_new(url + get)
    except sr.UnknownValueError:
        speak('error')
    except sr.RequestError as e:
        speak('failed'.format(e))
elif 'YouTube' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/'
    with sr.Microphone() as source:
        speak("Do you want to search anything? Say 'no' if not.")
        audio = r2.listen(source)
        if 'no' in r2.recognize_google(audio):
            wb.get().open_new(url)
    try:
        get = r2.recognize_google(audio)
        speak(get)
        url = "https://www.youtube.com/results?search_query="
        wb.get().open_new(url + get)
    except sr.UnknownValueError:
        speak('error')
    except sr.RequestError as e:
        speak('failed'.format(e))
elif 'Gmail' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin#inbox'
    try:
        wb.get().open_new(url)
    except sr.UnknownValueError:
        speak('error')
    except sr.RequestError as e:
        speak('failed'.format(e))
elif 'application' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Which app should I open?")
        audio = r2.listen(source)
        get = r2.recognize_google(audio)
        if os.name == 'nt':
            os.startfile("C:/ProgramData/Microsoft/Windows/ Start Menu/Programs/" + get + ".lnk")
        else:
            if ' ' in get:
                half = get.replace(" ", "\ ")
            try:
                os.system("open -a " + half.capitalize())
            except sr.UnknownValueError:
                speak('error')
            except sr.RequestError as e:
                speak('failed'.format(e))







