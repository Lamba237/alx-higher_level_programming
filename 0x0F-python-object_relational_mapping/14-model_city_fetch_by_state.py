#!/usr/bin/python3
"""
print state object with name passed as argument
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
