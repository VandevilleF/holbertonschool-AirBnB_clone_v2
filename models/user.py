<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel):
    """ The User class, representing users """
=======
#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
>>>>>>> 617c4052bd7eb4484e863e51c44fd3a423b9c700
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

<<<<<<< HEAD
    # Relationship with Place
    places = relationship("Place", backref="user", cascade="all, delete-orphan")

class Place(BaseModel):
    """ The Place class, representing places """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Reference from Place to User
    user = relationship("User", back_populates="places")
=======
    places = relationship("Place", cascade="all, delete", backref="user",
                          passive_deletes=True)
    reviews = relationship("Review", cascade="all, delete", backref="user")
>>>>>>> 617c4052bd7eb4484e863e51c44fd3a423b9c700
