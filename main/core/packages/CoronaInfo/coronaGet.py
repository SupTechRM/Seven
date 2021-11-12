import COVID19Py
import json

from main.bridges import utils

def CoronaGet(country):
    covid = COVID19Py.COVID19(data_source="jhu")

    data = covid.getAll()

    latest = covid.getLatest()

    locations = covid.getLocations(timelines=True,
                                   rank_by='confirmed')

    return utils.translate("Latest Data, \nConfirmed: ", latest["confirmed"], "\n Deaths: ", latest["deaths"], "\n Recovered: ", latest["recovered"])
