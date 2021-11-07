from sys import platform
import os
import json


def openApp(ApptoOpen):
    if platform == "darwin":
        os.system("open -a " + ApptoOpen)
    else:
        pass
    # How to open files in windows??!?!??!!


File = open('openApp.json')

data = json.load(File)
fileName = data['file_name']

File.close()

openApp(fileName)
