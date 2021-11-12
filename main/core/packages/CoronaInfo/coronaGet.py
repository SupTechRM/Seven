import COVID19Py
import json

def translate(text):
    print(text)

def CoronaGet():
    covid = COVID19Py.COVID19(data_source="jhu")

    data = covid.getAll()

    latest = covid.getLatest()

    locations = covid.getLocations(timelines=True,
                                   rank_by='confirmed')

    return translate("Latest Data, \nConfirmed: " + str(latest["confirmed"]) + "\n Deaths: " + str(latest["deaths"]))

CoronaGet()
