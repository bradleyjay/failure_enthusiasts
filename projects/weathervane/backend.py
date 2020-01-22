import requests
import time
import datetime
import os
from util.model import Weather_obj #check this
from crud import unpacker
#from CRUD_MODULE import add_data

api_key = str(os.environ.get('API_KEY'))

data_collected_timestamp = datetime.datetime.now().timestamp()

def make_connection():
    resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299')
    data = resp.json()
    return data

def parse_current(data):
    resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299')
    currently = data["currently"]

    # object Weather_obj requires precipType
    if "precipType" not in currently:
        currently["precipType"] = "null"

    model_array = []

    parsed = Weather_obj(
        data_collected_timestamp,
        0,
        currently["time"],
        currently["summary"],
        currently["temperature"],
        currently["precipIntensity"],
        currently["precipType"],
        currently["precipProbability"]
        )
    # parsed = create_model(raw_data)

    model_array.append(parsed)
    unpacker('actual', model_array)

    # jankny test
    # print("this is the present summary")
    # print(parsed.summary)



def parse_future(data):
    hourly = data["hourly"]["data"]

    model_array = []

    for i in hourly:

        # object Weather_obj requires precipType
        if "precipType" not in i:
            i["precipType"] = "null"

        # python uses seconds: this should yield say, 3600, for one hour. JS uses ms.
        data_age = i["time"] - data_collected_timestamp

        # TODO: ROUND data_collected_timestamp TO MIDNIGHT

        parsed = Weather_obj(
            data_collected_timestamp,
            data_age,
            i["time"],
            i["summary"],
            i["temperature"],
            i["precipIntensity"],
            i["precipType"],
            i["precipProbability"]
            )

        model_array.insert(0,parsed)

    unpacker('predictive', model_array)
