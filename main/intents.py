import json
import random
import numpy

sample_input = ""


with open('packages.json') as file:
    data = json.load(file)


patterns = []

for pattern in (data["packages"][5]["patterns"]):
    print(pattern)
    patterns.append(pattern.lower())
    sample_input = str(sample_input.split())
    for patternEach in patterns:
        if patternEach in sample_input:
            print("Found a match")
        else:
            print("No match")
        

print(patterns)



