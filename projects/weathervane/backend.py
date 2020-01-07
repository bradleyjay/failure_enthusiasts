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
    currently = data["currently"]

    # data_age =

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

    print("this is for the future \n")

    for i in hourly:

        print("\n" + str(i) + "\n\n")

        # object Weather_obj requires precipType
        if "precipType" not in i:
            i["precipType"] = "null"

        # python uses seconds: this should yield say, 3600, for one hour. JS uses ms.
        data_age = i["time"] - data_collected_timestamp

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
        # print("this is one of them: \n" + str(parsed.time))


    unpacker('predictive', model_array)



# def add_data(table, obj):
#     # table can be 'actual' or 'predicitive'
#     # obj is the 'model' object, i.e. Weather_obj
#     # for 'future', list of models is ok, DB team will unpack
#     # replace with imported add_data
#     pass



while True:

# change "time to next minute" to "time to next hour" for the real thing

    # begin the  minute
    print("\n\n starting  new  minute")

    # calculate time to next minute, wait
    time_to_next_minute = 60 - datetime.datetime.now().time().second
    print("time to  next minute: " + str(time_to_next_minute))
    time.sleep(time_to_next_minute)


    # state the time, grab data
    print("time now: " + str(datetime.datetime.now().time()))
    data = make_connection()


    if datetime.datetime.now().time().hour == 0 and datetime.datetime.now().time().minute == 0:

        parse_future(data)

    parse_current(data)
    parse_future(data)   # for now
