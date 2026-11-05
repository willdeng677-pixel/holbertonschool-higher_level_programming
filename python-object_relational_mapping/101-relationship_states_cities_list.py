#!/usr/bin/python3
"""List all states and their cities."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).options(
        joinedload(State.cities)
    ).order_by(State.id.asc()).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
