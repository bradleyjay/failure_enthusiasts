from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_tables():
    db = create_engine("postgres://weather_app_user_new:1234@localhost:5432/postgres")
    DBsession = sessionmaker(db)
    session = DBsession()
    base.metadata.create_all(db)
    session.close()

create_tables()

# print(blah.time)
# new_data = Actual_weather(blah)
# new_data = Actual_weather(summary="1")
