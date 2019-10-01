import query_suite
import datetime
from query_suite import compare_today
from query_suite import grab_from_actual
from query_suite import grab_from_predictive

print('\n\n compare_today  \n\n')
print(compare_today(['time', 'temperature']))

start_time = str(datetime.datetime.combine(
    datetime.datetime.today(), datetime.time.min).timestamp())

# - datetime.timedelta(days=0)   will give the  date at midnight two days ago
end_time = str(datetime.datetime.now().timestamp())

print('\n\n grab_from_actual  \n\n')
print(grab_from_actual(start_time, end_time, ['time', 'temperature']))


print('\n\n grab_from_predictive  \n\n')
print(grab_from_predictive(start_time, end_time, ['time', 'temperature']))
