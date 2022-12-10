#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models.city import City


class State(BaseModel):
    """ Defines State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete_child'
                          back_populates='state')

    @property
    def cities(self):
        '''returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
        '''
        from models import storage
        related_cities = []

        cities = storage.all(City).items()  # gets the entire storage- a dict.
        for city in cities.values():  # cities.value returns city objects list
            if city.state_id == self.id:  # if the object.state_id == self.id
                related_cities.append(city)  # append to the cities list
        return related_cities
