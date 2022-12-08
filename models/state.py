#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import model


class State(BaseModel):
    """ Defines State class """
    __tablename__ = 'states'

    if models.storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete, delete_child'
                        back_populates='state')
    else:
        name = ""

        @property
        def cities(self):
            cities = models.storage.all('City').values()
            return [city for city in cities if city.state_id == self.id]

