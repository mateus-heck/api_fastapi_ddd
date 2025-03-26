from sqlmodel import create_engine, Session
from sqlalchemy.engine import Engine

class Database:
    def __init__(self, db_url: str):
        self.engine: Engine = create_engine(db_url, echo=True)

    def get_session(self) -> Session:
        return Session(self.engine)


database = Database("sqlite:///database.db")