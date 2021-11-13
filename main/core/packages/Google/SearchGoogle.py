import webbrowser
from bridges import utils

def SearchGoogle(query):
    webbrowser.open("https://www.google.com/search?q=" + query)
    return utils.translate("Searched Google For "+ query)
    

