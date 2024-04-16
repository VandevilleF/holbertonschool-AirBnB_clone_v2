#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'  # Table name

    # City ID (foreign key to cities.id)
    city_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # User ID (foreign key to users.id)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Name of the place
    name = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Description of the place (optional)
    description = Column(String(1024))

    # Numbers of rooms
    number_rooms = Column(Integer, nullable=False, default=0)

    # Number of bathroom
    number_bathrooms = Column(Integer, nullable=False, default=0)

    # Maximum number of guests
    max_guest = Column(Integer, nullable=False, default=0)

    # Price per night
    price_by_night = Column(Integer, nullable=False, default=0)

    # Latitude coordinate (optional)
    latitude = Column(Float)

    # Longitude coordinate (optionnal)
    longitude = Column(Float)

    amenity_ids = []
