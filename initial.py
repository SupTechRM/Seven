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
            r.adjust_for_ambient_noise(source, duration=0.2)

            # listens for the user's input
            audio = r.listen(source)
            print("Listening")

            # Using ggogle to recognize audio
            inputtext = r.recognize_google(audio)
            inputtext = inputtext.lower()
            # print(inputtext)

            if " " in inputtext.strip() and "7" in inputtext.strip():
                os.system("python3 core.py")
                exit()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        continue
