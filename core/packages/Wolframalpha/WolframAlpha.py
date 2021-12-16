import requests
import json
import WolframAlpha
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



file = open('../../../main/apiData.json')

data = json.load(file)
inputtext = data['input']

file.close()
appid = "47P9L8-VHY6GJ54G8"

def QuestionSearchByMethod(input, appid):
    try:
        client = WolframAlpha.Client(appid)
        res = client.query(input)
        ans = next(res.results).text
        LISTED_STR = ["WolframAlpha", "Stephen"]
        for phrase in LISTED_STR:
            if phrase in ans:
                finalAns = ""
            else:
                finalAns = ans
        print(finalAns)

    except Exception as e:
        response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                                appid + "&input=" + input + "&output=json")
        jsonresp = response.json()
        outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        print(outcome)

QuestionSearchByMethod(inputtext, appid)
