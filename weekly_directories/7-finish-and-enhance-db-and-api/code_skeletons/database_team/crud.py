from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Weather_obj
from create_db import Actual_weather, Predictive_weather

def add_data(table, obj):
    db = create_engine("postgres://weather_app_user_new:1234@localhost:5432/postgres")
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

blah = Weather_obj("1","1","1","1","1","1")
add_data('predictive',blah)
