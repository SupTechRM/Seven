import speech_recognition as sr


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Recognizing...")
            # Using google for voice recognition.
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")  # User query will be printed.
            if query:
                return query
            else:
                takeCommand()
    except Exception:
        print("Please say again, I couldn't detect it.")
        # takeCommand()
