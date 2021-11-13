"""
Import Packages
"""
import webbrowser
#################################
# Packages
#################################
put = "search albert on google"
link = put.split()

if put.startswith('search '):
    try:
        link = '+'.join(link[1:])
        say = link.replace('+', ' ')
        # print(link)
        print("searching on google for " + say)
        webbrowser.open('https://www.google.co.in/search?q=' + link)
    except Exception as e:
        print(str(e))
