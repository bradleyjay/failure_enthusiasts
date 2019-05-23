from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine('postgres://user_bot:user_bot@localhost:5432/testbase')
base = declarative_base()

class weatherbase(base):
    __tablename__ = 'testbase'
    id = Column(Integer, primary_key=True)
    summary = Column(String(250), nullable=False)  # forces this data input
    time = Column(String(250))
    temperature = Column(String(250))
    
DBSession = sessionmaker(db)  #ORM for session
session = DBSession()

base.metadata.create_all(db)     #creates schema

new_weather_data = weatherbase(summary = 'Yeeep', time = '1558051320', temperature = '75')


session.add(new_weather_data)   #session.add is the insert
session.commit()                # actually do the ^^

print("Did the thing.")
