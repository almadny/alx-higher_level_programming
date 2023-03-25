#!/usr/bin/python3
""" A Module that defines a model for connectin Database using SQLAlchemy """
import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    stat = session.query(State, City).join(
                         City, State.id == City.state_id).all()
    for (state, city) in stat:
        print(f"{state.name}: ({city.id}) {city.name}")
