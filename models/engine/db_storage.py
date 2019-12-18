#!/usr/bin/python3
from os import getenv
from sqlalchemy import text


class DBStorage:
    """ New Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class """
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                    getenv('HBNB_MYSQL_PWD'),
                                                    getenv('HBNB_MYSQL_HOST')
                                                    getenv('HBNB_MYSQL_DB')),
        pool_pre_ping=True)

        if get_env('HBNB_ENV') is 'test':
                sql = text('DROP DATABASE' + getenv('HBNB_MYSQL_DB'))
                self.__engine.execute(sql)
    def all(self, cls=None):
        dic = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + obj.id] = obj
        else:
            for 
