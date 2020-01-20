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
    cities = relationship(
        "City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') is not 'db':
        @property
        def cities(self):
            """ Getter attribute """
            cs = []
            for city in models.storage.all(City).values():
                if (city.state_id == self.id):
                    cs.append(city)
            return cs
