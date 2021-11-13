from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import playsound

apikey = '3k6i8lvhuVL0xvMjdc3H0Fe5wciOJ-qN--UhqVPQNsev'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c0e720ca-1373-4cbb-959f-bae7d48795e0'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

def speech_Speak(text):
    # Speak
    with open('./speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, accept='audio/mp3',
                            voice='en-US_KevinV3Voice').get_result()
        audio_file.write(res.content)

