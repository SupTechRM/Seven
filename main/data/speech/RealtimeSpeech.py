import playsound
import sys
import pyttsx3
from gtts import gTTS
import random


class SpeechSynthesis():
    def __init__(self, speech_synthesiszer_module="pyttsx3", voice="com.apple.speech.synthesis.voice.daniel"):

        self.driver = ""
        self.synthesizer_module = speech_synthesiszer_module
        self.voice_chosen = voice

        if sys.platform != "darwin":
            self.driver = "sapi5"

        elif sys.platform == "darwin":
            self.driver = "nsss"
        else:
            self.driver = "espeak"

    def synthesize(self, audio):
        if self.synthesizer_module == "pyttsx3":
            engine = pyttsx3.init(self.driver)
            self.pyvoice = engine.setProperty(
                'voice', self.voice_chosen)
            """ RATE"""
            rate = engine.getProperty('rate')   # getting details of current speaking rate
            engine.setProperty('rate', 122)     # setting up new voice rate
            engine.say(audio)
            engine.runAndWait()
            engine.stop()

        elif self.synthesizer_module == "gTTS":
            tts = gTTS(text=audio, lang="en_GB", slow=False)
            filename = "audio" + random.randint(1, 100) + ".mp3"
            tts.save(filename)
            playsound.playsound(filename)
        else:
            engine = pyttsx3.init(self.driver)
            engine.say(audio)
            engine.runAndWait()
            engine.stop()

    def print_text(self, text):
        print(text)


