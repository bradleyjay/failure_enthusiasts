from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Actual_weather(base):
    __tablename__ = 'actual_weather'
    id = Column(Integer(), primary_key=True)
    time = Column(String())
    summary = Column(String())
    temperature = Column(String())
    precipitation_intensity = Column(String())
    precipitation_type = Column(String())
    precipitation_probability = Column(String())

class Predictive_weather(base):
    __tablename__ = 'predictive_weather'
    id = Column(Integer(), primary_key=True)
    time = Column(String())
    summary = Column(String())
    temperature = Column(String())
    precipitation_intensity = Column(String())
    precipitation_type = Column(String())
    precipitation_probability = Column(String())

def create_tables():
    db = create_engine("postgres://weather_app_user_new:1234@localhost:5432/postgres")
    DBsession = sessionmaker(db)
    base.metadata.create_all(db)
    session = DBsession()
    session.close()

create_tables()

# print(blah.time)
# new_data = Actual_weather(blah)
# new_data = Actual_weather(summary="1")
