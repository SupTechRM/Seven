import os
import json
import webbrowser

path = './user.json'

existence = os.path.exists(path)

if existence:
    opened = open('user.json')
    data = json.load(opened)
    opened.close()
else:
    # webbrowser.open(
    #     "http://localhost:3000/Computer/app/setup/setupUi_Main/userSetup/Frontend.html")
    pass
