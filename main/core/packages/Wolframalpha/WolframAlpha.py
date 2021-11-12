import requests
import json
import WolframAlpha
from main.bridges import utils

file = open('apiData.json')

data = json.load(file)
appid = data['appid']

file.close()

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
        return utils.translate(finalAns)
    
    except Exception as e:
        response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                                appid + "&input=" + input + "&output=json")
        jsonresp = response.json()
        outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        return utils.translate(outcome)


