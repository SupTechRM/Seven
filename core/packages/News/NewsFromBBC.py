import requests
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


res = NewsFromBBC()
