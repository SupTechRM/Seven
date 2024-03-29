import speech_recognition as sr


class Stream_Speech:

    def takeCommand(self):

        # While listen -> True
        while True:
            # Initialize the recognizer
            r = sr.Recognizer()
            # Initialize the microphone
            with sr.Microphone() as source:
                # Listening
                try:
                    print("Listening...")

                    # Processing
                    r.pause_threshold = 1
                    audio = r.listen(source)

                    # Catch exceptions

                    print("Recognizing...")
                    # Using google for voice recognition.
                    query = r.recognize_google(audio, language='en-in')
                    print(f"User said: {query}\n")  # User query will be printed.
                except Exception:
                    # Say that again will be printed in case of improper voice
                    print("Say that again please...")
                    self.takeCommand()

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")

                except sr.RequestError as e:
                    print(
                        "Could not request results from Google Speech Recognition service{0}".format(e))
                try:
                    if query:
                        return query.lower()
                    else: # If query is not recognized
                        self.takeCommand()
                except UnboundLocalError:
                    pass
    
    def takeText(self):
        """ Use input (recognize -> text object) """
        
        # Take an input as query
        query = input("How can I help? ")
        query = query.lower()

        # If query is recognized
        if query:

            # Return the query
            return query

        else: # If query is not recognized
            self.takeText()

