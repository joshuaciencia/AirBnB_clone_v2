#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import Base

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship(
        "City", backref="state", cascade="delete")
    

    @property
    def cities(self):
        """ Getter attribute """
        cities = []
        for city in models.storage.all(City).values():
            if (city.state_id == self.id):
                cities.append(city)
        return cities
