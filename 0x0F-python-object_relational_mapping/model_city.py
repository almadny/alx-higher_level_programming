#!/usr/bin/python3
""" A Module that defines a model for connectin Database using SQLAlchemy """
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
        Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                       .format('root', 'root'), pool_pre_ping=True)


class City(Base):
    """ Model that defines states table in MySQL """

    __tablename__ = "cities"
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
