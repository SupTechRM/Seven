import speech_recognition as sr

def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Listening")

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            pass
    
    return query