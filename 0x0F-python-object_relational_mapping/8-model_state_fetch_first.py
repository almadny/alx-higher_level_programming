#!/usr/bin/python3
""" A Module that defines a model for connectin Database using SQLAlchemy """
import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        r = session.query(State).first()
        if r is None:
            print('Nothing')
        else:
            print(f"{r.id}: {r.name}")
