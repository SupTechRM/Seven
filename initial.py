import os
import speech_recognition as sr

while True:
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            r = sr.Recognizer()
            # the surrounding noise level
            r.pause_threshold = 1
            # listens for the user's input
            audio = r.listen(source)
            print("Listening...")

            # Using ggogle to recognize audio
            inputtext = r.recognize_google(audio)
            print(inputtext)
            inputtext = inputtext.lower()
            # print(inputtext)

            if " " in inputtext.strip() and "7" in inputtext.strip():
                os.system("python core.py")
                exit()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        continue
