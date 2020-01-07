from crud import read_data
import time
import datetime


# start_time = '1564097280'
# end_time = '1564098720'
attributes = ['time', 'summary', 'temperature']
# table = 'actual_weather'

hour_interval = int( .5 * 3600) # 3600s = 1 hr, 1hr frequency rn
minute_interval = int( .5 * 60 )
# data = read_data(start_time, end_time, attributes, table)
# print(data.keys())
# input()


# for attribute in attributes:
#     print(data[attribute])

# print(data)


# query to now, or query today...something


# 2) Grab X from actual
def grab_from_actual(start_time, end_time, attributes, data_age=0, interval=0):
    table = 'actual_weather'
    data = read_data(start_time, end_time, attributes, table, data_age, interval)
    return {"actual_data": data}

# 3) Grab X from predictive


def grab_from_predictive(start_time, end_time, attributes, data_age=3600, interval=hour_interval):
    table = 'predictive_weather'
    data = read_data(start_time, end_time, attributes, table, data_age, interval)
    return {"predictive_data": data}
# 1) Compare today


def compare_today(attributes):

    start_time = str(datetime.datetime.combine(
        datetime.datetime.today(), datetime.time.min).timestamp())

    # - datetime.timedelta(days=0)   will give the  date at midnight two days ago

    end_time = str(datetime.datetime.now().timestamp())

    actual_data = read_data(start_time, end_time, attributes, 'actual_weather')

    # hardcoding interval for now, but could be parameter in future
    predictive_data = read_data(
        start_time, end_time, attributes, 'predictive_weather', )
    return {"actual_data": actual_data, "predictive_data": predictive_data}


def compare_today_fake():
    return 'Hey'
