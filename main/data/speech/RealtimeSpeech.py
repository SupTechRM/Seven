import os
import playsound
import random
from gtts import gTTS

# Instantiates a client


def SpeechSynthesizer(audio, path="empyrean-app-332014-6fdfdc87b1df.json"):
    response = gTTS(text=audio, lang="en", tld="co.in")
    # The response's audio_content is binary.
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    response.save(filename)
    playsound.playsound(filename)
    os.remove(filename)