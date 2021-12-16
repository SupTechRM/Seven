################################
# Speedtest Access Reach Internet
################################


import os
import speedtest
import os
import playsound
import random
from gtts import gTTS


def SpeechSynthesizer(audio):
    response = gTTS(text=audio, lang="en")
    # The response's audio_content is binary.
    filename = "./output" + str(random.randint(1, 100)) + ".mp3"
    response.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


wifi = speedtest.Speedtest()


def InternetSpeedTest(wifi):
    download = wifi.download()
    upload = wifi.upload()
    print("Dowload Speed:" + str(round(download, 2)) + ".Upload Speed:" + str(int(round(download, 2))))


InternetSpeedTest(wifi)
