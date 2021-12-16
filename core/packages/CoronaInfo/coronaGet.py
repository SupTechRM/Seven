import COVID19Py
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

def CoronaGet():
    covid = COVID19Py.COVID19(data_source="jhu")

    data = covid.getAll()

    latest = covid.getLatest()

    locations = covid.getLocations(timelines=True,
                                   rank_by='confirmed')

    print("Latest Data, \nConfirmed: " + str(latest["confirmed"]) + "\n. Deaths: " + str(
        latest["deaths"]) + "\n. Recovered: " + str(latest["recovered"]))


CoronaGet()
