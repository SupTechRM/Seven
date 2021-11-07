import os
import json
import webbrowser

path = '../Computer/user.json'

doesExist = os.path.exists(path)

if doesExist:
    opened = open('../Computer/user.json')
    data = json.load(opened)
    opened.close()
else:
    webbrowser.open(
        'http://localhost:3000/Computer/app/setup/setupUi_Main/userSetup/Frontend.html')
