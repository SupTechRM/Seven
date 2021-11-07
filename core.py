import os
import json
import webbrowser

path = '../Computer/user.json'

doesExist = os.path.exists(path)

if doesExist:
    opened = open('../Computer/user.json')
    data = json.load(opened)
    print(data["name"])
    opened.close()
else:
    """Write an Algorithm to run Electron Start from Command Shell"""
    pass
