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
    s1 = session.query(State).get(2)
    s1.name = 'New Mexico'
    session.add(s1)
    session.commit()
    print(s1.id)
