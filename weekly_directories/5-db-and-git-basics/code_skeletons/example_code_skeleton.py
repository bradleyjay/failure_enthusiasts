from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine('postgres://USERNAME:PASSWORD@localhost:5432/DBNAME')
base = declarative_base()

class OBJECT(base):
    __tablename__ = 'DBNAME'
    
DBSession = sessionmaker(db)
session = DBSession()

base.metadata.create_all(db)
