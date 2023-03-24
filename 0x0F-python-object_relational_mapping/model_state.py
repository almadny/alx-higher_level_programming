#!/usr/bin/python3
""" A Module that defines a model for connectin Database using SQLAlchemy """
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
        Column, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                       .format('root', 'root'), pool_pre_ping=True)
Base = declarative_base()


class State(Base):
    """ Model that defines states table in MySQL """

    __tablename__ = "states"
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
