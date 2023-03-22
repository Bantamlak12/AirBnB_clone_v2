#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from os import environ
=======
from sqlalchemy import Column, String, Float, Integer, ForeignKey

>>>>>>> 7b1492c8056aa62d35c994aaa45490024a47a602

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review',
                              cascade='all, delete', backref='place')
    else:
        @property
        def reviews(self):
            """ getter returns list of reviews """
            list_of_reviews = []
            all_reviews = models.strage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews
