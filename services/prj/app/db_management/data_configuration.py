from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
import os

URI = "postgresql://*:*@localhost:*/*"
DB_ECHO = False

# To separate in to functions
if os.getenv('URI'):
    URI = os.environ['URI']


Engine = create_engine(URI, echo=bool(DB_ECHO))
Base = declarative_base()


def db_create(engine=Engine):
    if not database_exists(Engine.url):
        create_database(Engine.url)
    else:
        pass


Session = sessionmaker(bind=Engine)


def db_drop(engine=Engine):
    if database_exists(engine.url):
        drop_database(engine.url)
    else:
        pass
