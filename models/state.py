#!/usr/bin/python3
"""
State Class from Models Module
"""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """State class handles all application states"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """"""
            from models import storage
            city_list = []
            cities_dict = storage.all(cls="City")
            for k,v in cities_dict.items():
                if v.get("state_id") == self.id:
                    city_list.append(v)
            return city_list
