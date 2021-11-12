import os
import json
import webbrowser

path = './user.json'

existence = os.path.exists(path)

if existence:
    opened = open('user.json')
    data = json.load(opened)
    opened.close()
    # redirect to lib.py
else:
    print("User json doesn't exist")
    # os.system("cd app")
    # os.system("npm start")