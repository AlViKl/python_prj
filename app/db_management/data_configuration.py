from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

URI = "postgresql://*:*@localhost:*/*"
DB_ECHO = "False"

# To separate in to functions
if os.getenv('URI'):
    URI = os.environ['URI']
if os.getenv('DB_ECHO'):
    DB_ECHO = os.environ['DB_ECHO']
else:
    DB_ECHO = False


Engine = create_engine(URI, echo=DB_ECHO)
Base = declarative_base()

if not database_exists(Engine.url):
    create_database(Engine.url)

Session = sessionmaker(bind=Engine)
