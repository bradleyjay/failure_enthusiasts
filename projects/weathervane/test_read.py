from crud import read_data

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


