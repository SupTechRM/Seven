from sys import platform
import os
import json


def openApp(ApptoOpen):
    if platform == "darwin":
        os.system("open -a " + ApptoOpen)
    else:
        pass
    # How to open files in windows??!?!??!!


file = open('openApp.json')

data = json.load(file)
fileName = data['file_name']

file.close()

openApp(fileName)
