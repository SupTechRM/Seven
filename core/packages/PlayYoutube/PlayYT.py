import pywhatkit as kit
import os
import playsound
import random
from gtts import gTTS

# Instantiates a client


def SpeechSynthesizer(audio):
    response = gTTS(text=audio, lang="en")
    # The response's audio_content is binary.
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    response.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def PlayYTTVideo(string):
    kit.playonyt(string)
    SpeechSynthesizer("Opening")



os.system("python ../../../main/runmain.py")
