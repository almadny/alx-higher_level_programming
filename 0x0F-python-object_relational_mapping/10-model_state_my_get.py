#!/usr/bin/python3
""" A Module that defines a model for connectin Database using SQLAlchemy """
import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State.id).filter(State.name == sys.argv[4]).all()
    if len(states) == 0:
        print('Not Found')
    else:
        for state in states:
            for item in state:
                print(item)
