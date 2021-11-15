import speech_recognition as sr


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            # Using google for voice recognition.
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            # print(e)
            # Say that again will be printed in case of improper voice
            print("Say that again please...")
            takeCommand()
    
    return query
    
