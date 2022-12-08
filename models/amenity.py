#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = Column(ForeignKey('places.id'), nullable=False)

        amenities = relationship('Place', back_populates='amenities')

    else:
        amenity_id = ""
        name = ""
