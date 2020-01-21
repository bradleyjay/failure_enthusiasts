from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

import os

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
    data_age = Column(Integer())
    data_collected_timestamp = Column(String())

class Predictive_weather(base):
    __tablename__ = 'predictive_weather'
    id = Column(Integer(), primary_key=True)
    time = Column(String())
    summary = Column(String())
    temperature = Column(String())
    precipitation_intensity = Column(String())
    precipitation_type = Column(String())
    precipitation_probability = Column(String())
    data_age = Column(Integer())
    data_collected_timestamp = Column(String())
