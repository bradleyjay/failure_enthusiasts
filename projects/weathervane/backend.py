import requests
import time
import datetime
import os
from util.model import Weather_obj #check this
from crud import unpacker
#from CRUD_MODULE import add_data

api_key = str(os.environ.get('API_KEY'))

data_collected_timestamp = datetime.datetime.now().timestamp()

# def make_connection():
#     resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299')
#     data = resp.json()
#     return data

def parse_current():
    resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299')
    data = resp.json()
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

#________________________________________________

def parse_future():
    resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299' + 'hourly')
    data = resp.json()
    # print("this is it babbbbyyyy" + data)
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

#________________________________________________

def test_parse_future():
    resp = requests.get('https://api.darksky.net/forecast/' + api_key + '/40.756438,-73.990299' + '?' + 'hourly')
    data = resp.json()
    print(data)
    # filter for the next 24 hours
    #11:40pm (current day) -> 11:40pm (next day)
    # Request returns data every hour on the minute
    # hourly = data["hourly"]["data"]
    # print(hourly)
    #
    # model_array = []
    #
    # for i in hourly:
    #
    #     # object Weather_obj requires precipType
    #     if "precipType" not in i:
    #         i["precipType"] = "null"
    #
    #     # python uses seconds: this should yield say, 3600, for one hour. JS uses ms.
    #     data_age = i["time"] - data_collected_timestamp
    #
    #     # TODO: ROUND data_collected_timestamp TO MIDNIGHT
    #
    #     parsed = Weather_obj(
    #         data_collected_timestamp,
    #         data_age,
    #         i["time"],
    #         i["summary"],
    #         i["temperature"],
    #         i["precipIntensity"],
    #         i["precipType"],
    #         i["precipProbability"]
    #         )
    #
    #     model_array.insert(0,parsed)
    #
    # unpacker('predictive', model_array)
