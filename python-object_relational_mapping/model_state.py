#!/usr/bin/python3
"""State class definition."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """State class."""

    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )
