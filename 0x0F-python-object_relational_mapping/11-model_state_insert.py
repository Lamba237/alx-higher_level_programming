#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_new = State(name="Louisiana")
    session.add(state_new)
    session.commit()
    print(state_new.id)
    session.close()
