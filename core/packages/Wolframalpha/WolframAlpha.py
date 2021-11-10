import wolframalpha
import json

file = open('query.json')

data = json.load(file)
dataquery = data['query']


def Questionsearch(query):
    client = wolframalpha.Client('47P9L8-VHY6GJ54G8')
    res = client.query(query)
    output = next(res.results). text
    return output


output = Questionsearch(dataquery)
print(output)

file.close()
