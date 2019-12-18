#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """ Getter attribute """
            cs = []
            for city in models.storage.all(City).values():
                if (city[id] == self.id):
                    cs.append(city)
            return cs
