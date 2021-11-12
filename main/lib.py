from core.packages import __init__
from core.packages import *
from core import packages
import spacy
import threading
import string
import re
import sys
import json

nlp = spacy.load('en_core_web_sm')

sample_input = "play enimem on youtube run the latest news"


# Define a dictionary containing Command Words and Attributes
# Use spacy to find action words
# find adjacent value to the verb
# store in a dictionary based on action word to commmand and adjacent to attribute

Dict = {"Command Words": "", "Attributes": ""}

str = f''' {sample_input} '''



doc = nlp(str)
for ent in doc:
    if ent.pos_ == "VERB":
        Dict["Command Words"] = ent.text
        print("Command Words: ", Dict["Command Words"])
    else:
        Dict["Attributes"] = ent.text
        print("Attributes", Dict["Attributes"])


