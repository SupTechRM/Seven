import pywhatkit as kit
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

import playsound

apikey = 'hS-rPVvT204ye5fuInLK0hicBBnFCSo0DnJCFUBx6o-g'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c0e720ca-1373-4cbb-959f-bae7d48795e0'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


def SpeechSyntesizer(audio):
    try:
        with open('speech.mp3', 'wb') as audio_file:
            res = tts.synthesize(audio, accept='audio/mp3',
                                 voice='en-GB_JamesV3Voice').get_result()
            audio_file.write(res.content)

    except Exception as e:
        print(e)
        with open('speech.mp3', 'wb') as audio_file:
            res = tts.synthesize(audio, accept='audio/mp3',
                                 voice='en-GB_JamesV3Voice').get_result()
            audio_file.write(res.content)

def PlayYTTVideo(string):
    kit.playonyt(string)
    SpeechSyntesizer("Opening")

PlayYTTVideo("Something")