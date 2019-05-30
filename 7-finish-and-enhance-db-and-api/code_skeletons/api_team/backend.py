import requests
import time
import datetime

class Weather_obj:

# Note: id is removed
# SHOULD BE REFACTORED -> instead import "weather object module" - this shouldn't exist in two places

    def __init__(self, time, summary, temperature, precipitation_intensity, precipitation_type, precipitation_probability):
            self.time = time
            self.summary = summary
            self.temperature = temperature
            self.precipitation_intensity = precipitation_intensity
            self.precipitation_type = precipitation_type
            self.precipitation_probability = precipitation_probability


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
    

    crud(parsed)

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

    
    crud(model_array)



def crud(an_input):
    # call the DB team's crud function here
    pass



while True:

    data = make_connection()
    

    ## Issue: what if this never hits midnight exactly? Breaks
    ## could wait to sync with the minute, etc...
    
    if datetime.datetime.now().time().hour == 0 and datetime.datetime.now().time().minute == 0:
        
        parse_future(data)
    
    parse_current(data)
    parse_future(data)
    
    # wait one minute
    time.sleep(60)




