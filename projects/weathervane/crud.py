from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.model import Weather_obj #check this 
from create_db import Actual_weather, Predictive_weather

def add_data(table, obj):
    db = create_engine("postgres://weather_app_user:1234@localhost:5432/postgres")
    DBsession = sessionmaker(db)
    session = DBsession()
    if table == 'actual':
        new_data = Actual_weather(
                    time = obj.time
                    , summary = obj.summary
                    , temperature = obj.temperature
                    , precipitation_intensity = obj.precipitation_intensity
                    , precipitation_type = obj.precipitation_type
                    , precipitation_probability = obj.precipitation_probability
                   )
        session.add(new_data)
        session.commit()
        session.close()
    elif table == 'predictive':
        new_data = Predictive_weather(
                    time = obj.time
                    , summary = obj.summary
                    , temperature = obj.temperature
                    , precipitation_intensity = obj.precipitation_intensity
                    , precipitation_type = obj.precipitation_type
                    , precipitation_probability = obj.precipitation_probability
                   )
        session.add(new_data)
        session.commit()
        session.close()
    else:
        print('table name should be actual or predictive')


def unpacker(table, model_array):
    while model_array:
        add_data(table, model_array.pop())
        # print(model_array[-1])

# blah = Weather_obj("1","1","1","3","1","1")
# blah2 = Weather_obj("1","2","1","1","1","1")

# model_array = [blah, blah2]

# unpacker('actual', model_array)

# def read_data(start_time,  end_time, attributes, table):
#     # Ultimate query structure:
#     # SELECT attribute1
#     #     , attribute2
#     #     , attibute3
#     # FROM table
#     # WHERE time >= start_time
#     #     AND time =< end_time;
#     db = create_engine("postgres://weather_app_user:1234@localhost:5432/postgres")
#     DBsession = sessionmaker(db)
#     session = DBsession()
#     attribute_string = ", ".join(attributes)
#     sql_query = "SELECT " + attribute_string \
#                     + " FROM  " + table \
#                     + " WHERE to_timestamp(extract(epoch from time))::date >= '" +  start_time \
#                     + "' AND to_timestamp(extract(epoch from time)) <= '" + end_time \
#                     + "';"
#     # unix timestamp needs to be converted
#     # time and start_time are strings, so this might break
#     sql_query
#     print(sql_query)
#     print( db.execute(sql_query))
#     print(type(db.execute(sql_query)))