from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.model import Weather_obj #check this
from create_db import Actual_weather, Predictive_weather
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def add_data(table, obj):
    db = create_engine(DATABASE_URL)
    DBsession = sessionmaker(db)
    session = DBsession()

    if table == 'actual':
        new_data = Actual_weather(
                    id = str(obj.time) + "_" + str(obj.data_collected_timestamp)
                    , time = obj.time
                    , summary = obj.summary
                    , temperature = obj.temperature
                    , precipitation_intensity = obj.precipitation_intensity
                    , precipitation_type = obj.precipitation_type
                    , precipitation_probability = obj.precipitation_probability
                    , data_age = obj.data_age
                    , data_collected_timestamp = obj.data_collected_timestamp
                   )
        session.add(new_data)
        session.commit()
        session.close()

    elif table == 'predictive':
        new_data = Predictive_weather(
                    id = str(obj.time) + "_" + str(obj.data_collected_timestamp)
                    , time = obj.time
                    , summary = obj.summary
                    , temperature = obj.temperature
                    , precipitation_intensity = obj.precipitation_intensity
                    , precipitation_type = obj.precipitation_type
                    , precipitation_probability = obj.precipitation_probability
                    , data_age = obj.data_age
                    , data_collected_timestamp = obj.data_collected_timestamp
                   )
        session.add(new_data)
        session.commit()
        session.close()

    else:
        print('table name should be actual or predictive')


def unpacker(table, model_array):
    while model_array:
        add_data(table, model_array.pop())

def read_data(start_time,  end_time, attributes, table):

# start_time, end_time MUST be strings
# attributes is an array of strings
# table is a string for table name

# Ultimate query structure:
# SELECT attribute1
#     , attribute2
#     , attibute3
# FROM table
# WHERE time >= start_time
#     AND time =< end_time;


    db = create_engine(DATABASE_URL)
    DBsession = sessionmaker(db)
    session = DBsession()
    attribute_string = ", ".join(attributes)

    sql_query = "SELECT " + attribute_string \
                    + " FROM  " + table \
                    + " WHERE time >= '" +  start_time \
                    + "' AND time <= '" + end_time
    if (table == "actual_weather"):
        sql_query += "';"
    else:
        sql_query += \
            "' AND data_collected_timestamp::decimal >= '" +  start_time \
            + "' AND data_collected_timestamp::decimal <= '" +  end_time \
            + "';"

    # unix timestamp needs to be converted
    # time and start_time are strings, so this might break
    # fetchall is required to actually send
    # https://docs.sqlalchemy.org/en/13/core/connections.html#sqlalchemy.engine.ResultProxy.fetchall
    #  fetchall has a soft close,  don't have to close session, but lets be adults
    data = db.execute(sql_query).fetchall()
    session.close()

    return data
