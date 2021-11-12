from genericpath import sameopenfile
import json
import random
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

input_to = str("play youtube")

with open('packages.json') as file:
    data = json.load(file)


words = []
labels = []
docs_x = []
docs_y = []

for intent in data['packages']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)

        if pattern in input_to.split():
            print(intent["tag"])
        else:
            print("not found")

        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])



