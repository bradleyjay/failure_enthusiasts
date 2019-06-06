from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Weather_obj
from create_db import Actual_weather

def make_connection():
    db = create_engine("postgres://weather_app_user:'1234'@localhost:5432/postgres")
    return db

def make_session(db):
    DBsession = sessionmaker(db)
    session = DBsession()
    return session

def create(table_name, Weather_obj):
    db = make_connection()
    session = make_session(db)
    if table_name == 'Actual_weather':
        new_data = Actual_weather(Weather_obj)  
    else:
        new_data = Predictive_weather(Weather_obj)
    session.add(new_data)
    session.commit()
blah = Weather_obj('1','1','1','1','1','1')
create('Actual_weather', blah)
    