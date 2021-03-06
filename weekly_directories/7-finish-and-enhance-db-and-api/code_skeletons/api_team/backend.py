import requests
import time
import datetime
from model import Weather_obj
#from CRUD_MODULE import add_data


def make_connection():
    resp = requests.get('https://api.darksky.net/forecast/c49ab0cc157f5ad35bdb1a9b0769853e/40.756438,-73.990299')
    data = resp.json()
    return data

def parse_current(data):
    currently = data["currently"]
    
    # object Weather_obj requires precipType
    if "precipType" not in currently:
        currently["precipType"] = "null"

    parsed = Weather_obj(
        currently["time"], 
        currently["summary"], 
        currently["temperature"], 
        currently["precipIntensity"], 
        currently["precipType"], 
        currently["precipProbability"]
        )
    # parsed = create_model(raw_data)
    

    add_data('actual', parsed)

    # jankny test
    print("this is the present summary")
    print(parsed.summary)



def parse_future(data):
    hourly = data["hourly"]["data"]
    
    model_array = []

    print("this is for the future \n")

    for i in hourly:

        print("\n" + str(i) + "\n\n")

        # object Weather_obj requires precipType
        if "precipType" not in i:
            i["precipType"] = "null"

        parsed = Weather_obj(
            i["time"], 
            i["summary"], 
            i["temperature"], 
            i["precipIntensity"], 
            i["precipType"], 
            i["precipProbability"]
            )
        
        model_array.insert(0,parsed)
        print("this is one of them: \n" + str(parsed.time))

    
    add_data('predictive', model_array)



def add_data(table, obj):
    # table can be 'actual' or 'predicitive'
    # obj is the 'model' object, i.e. Weather_obj
    # for 'future', list of models is ok, DB team will unpack
    # replace with imported add_data
    pass



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
        
    








