from Seven.main.data.speech.RealtimeSpeech import SpeechSyntesizer
import playsound


def translate(text):
    SpeechSyntesizer(text)
    playsound.playsound('speech.mp3')

translate("Hello man!")