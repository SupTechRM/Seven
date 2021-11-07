import COVID19Py
import json


covid = COVID19Py.COVID19(data_source="jhu")

data = covid.getAll()

latest = covid.getLatest()
print("Latest Data:")
print("\nConfirmed: ", latest["confirmed"])
print("\nDeathes: ", latest["deaths"])
print("\nRecovered: ", latest["recovered"])

locations = covid.getLocations(timelines=True,
                               rank_by='confirmed')
