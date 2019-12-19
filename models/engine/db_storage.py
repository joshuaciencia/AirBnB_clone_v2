#!/usr/bin/python3
""" Usage of SQLAlchemy """
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """ New Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                    getenv('HBNB_MYSQL_PWD'),
                                                    getenv('HBNB_MYSQL_HOST'),
                                                    getenv('HBNB_MYSQL_DB')),
        pool_pre_ping=True)
        if getenv('HBNB_ENV') is 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """ 
            Condition that query all types of objects 
            Returns a dictionary
        """
        dic = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + "." + obj.id] = obj
        else:
            cls_list = [State, City, User, Place, Review]
            for c in cls_list:
                for obj in self.__session.\
                query(c).\
                all():
                    dic[type(obj).__name__ + "." + obj.id] = obj
        return dic
    
    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
