#!/usr/bin/python3
"""City class definition."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """City representation."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )

    state = relationship(
        "State",
        back_populates="cities"
    )
