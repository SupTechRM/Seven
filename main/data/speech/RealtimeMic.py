import speech_recognition as sr


def takeCommand():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print("Listening")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            continue
        if query:
            return query.lower()
        else:
            continue
