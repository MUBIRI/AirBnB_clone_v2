#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv
from models.base_models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


classes = [User, State, City, amenity, Place, Review]

class DBStorage:
    """ DB Storage engine"""
    __engine = None
    __session = None

    # Dialect+driver://username:password@host:port/database
    def __init__(self):
        """Public instance method"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = detenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        url =f'mysql+mysqldb://{user}:{pwd}@{host}/{db}'

        self.__engine = create_engine(url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict_of_objects = {}

        if cls is None:
            for _class in classes:
                list_of_objs = self.__session.query(_class).all()

                for obj in list_of_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict_of_objects[key] = obj
            
            return dict_of_objects

        cls = eval(cls) if type(cls) is str else cls

        if cls not in classes:
            return None

        list_of_objs = self.__session.query(cls).all()

        for obj in list_of_objs:
            key = obj.__clas__.__name__ + '.' + obj.id
            dict_of_objects[key] = obj
        return dict_of_objects

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self:):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)

        self.__session = Session()

