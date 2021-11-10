import requests
import json

file = open('query.json')

data = json.load(file)
input = data['query']
appid = data['appid']

file.close()


def QuestionSearch(input, appid):
    response = requests.get("http://api.wolframalpha.com/v2/query?appid=" +
                            appid + "&input=" + input + "&output=json")
    jsonresp = response.json()
    outcome = jsonresp["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
    return outcome


result = QuestionSearch(input, appid)

print(result)
