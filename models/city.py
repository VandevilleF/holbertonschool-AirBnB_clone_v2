#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    # New relationship with Place class
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
=======
    state_id = Column(String(60), ForeignKey('states.id', ondelete="CASCADE"),
                      nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities",
                          passive_deletes=True)
>>>>>>> 617c4052bd7eb4484e863e51c44fd3a423b9c700
