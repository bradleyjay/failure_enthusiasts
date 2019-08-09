from crud import read_data
import time
import datetime


start_time = '1564097280'
end_time = '1564098720'
attributes = ['time', 'summary', 'temperature']
table = 'actual_weather'

data = read_data(start_time, end_time, attributes, table)
# print(data.keys())
# input()


# for attribute in attributes:
#     print(data[attribute])

print(data)


# query to now, or query today...something





# 2) Grab X from actual
def grab_from_actual(start_time, end_time, attributes):
    table = 'actual_weather'
    data = read_data(start_time, end_time, attributes, table)
    return data

# 3) Grab X from predicted 
def grab_from_predicted(start_time, end_time, attributes):
    table = 'predictive_weather'
    data = read_data(start_time, end_time, attributes, table)
    return data
# 1) Compare today

def compare_today(start_time, end_time, attributes):
    # start_time =  today, 00:00
    # end_time = today, 23:59

    start_time = datetime.datetime.now()

    # whats the date today
    today = datetime.date.today()   # 2019-04-13

    # datetime.datetime(2019, 8, 8, 20, 36, 52, 0).timestamp()
    # -> interpolate and run. maybe parse from datetime.date.today?


    # whats the format for converting a time an date to epoch

    end_time = datetime.datetime.now().timestamp()

    actual_data = read_data(start_time, end_time, attributes, 'actual_weather')
    predicted_data = read_data(start_time, end_time, attributes, 'predictive_weather')
    return actual_data, predicted_data
