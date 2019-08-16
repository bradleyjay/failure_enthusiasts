from crud import read_data
import time
import datetime


# start_time = '1564097280'
# end_time = '1564098720'
attributes = ['time', 'summary', 'temperature']
# table = 'actual_weather'

# data = read_data(start_time, end_time, attributes, table)
# print(data.keys())
# input()


# for attribute in attributes:
#     print(data[attribute])

# print(data)


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

    start_time = datetime.datetime.combine(datetime.datetime.today(), datetime.time.min)

    # - datetime.timedelta(days=0)   will give the  date at midnight two days ago

    end_time = datetime.datetime.now().timestamp()

    actual_data = read_data(start_time, end_time, attributes, 'actual_weather')
    predicted_data = read_data(start_time, end_time, attributes, 'predictive_weather')
    return actual_data, predicted_data






