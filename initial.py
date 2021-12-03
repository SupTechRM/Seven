# Import Packages

import os
import speech_recognition as sr

class OnSeven:
    def __init__(self):
        
        """ On Seven -> Detect(Start Core) """
        self.start()

    def start(self):
        # Continue listening
        while True:

            # Use Try/Except to troubleshoot errors
            try:
                # use the microphone as source for input.n
                with sr.Microphone() as source:

                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    r = sr.Recognizer()

                    # the surrounding noise level
                    r.pause_threshold = 1

                    # listens for the user's input
                    audio = r.listen(source)
                    print("Listening...")

                    # Using google speech recognition to recognize audio
                    inputtext = r.recognize_google(audio)

                    # Proccesing and Logging Recognized Text
                    inputtext = inputtext.lower()

                    # If Seven in Inputtext then execute the following
                    if " " in inputtext.strip() and "7" in inputtext.strip():
                        # Redirect to core.py
                        os.system("python core.py")

                        # Exit Current File
                        exit()

            # Troubleshoot for Speech Requesting Errors
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            # Unknown error Continue
            except sr.UnknownValueError:
                continue

##########################
# While Seven -> OnSeven
##########################

OnSeven = OnSeven()
