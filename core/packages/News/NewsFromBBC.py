import requests
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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

def NewsFromBBC():

    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        # printing all trending news
        print(i + 1, results[i])

    SpeechSyntesizer(results)


