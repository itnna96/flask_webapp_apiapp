import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_USER=os.environ.get('DB_USER') ; assert DB_USER
DB_PASS=os.environ.get('DB_PASS') ; assert DB_PASS
DB_HOST=os.environ.get('DB_HOST') ; assert DB_HOST
DB_NAME=os.environ.get('DB_NAME') ; assert DB_NAME
DB_URL=f'mysql+mysqldb://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'  #TODO why DB_HOST=localhost:port NOT working, but 127.0.0.1:port working?

# print(f'{DB_URL=}'); import sys; sys.exit()

scoped_engine = create_engine(DB_URL)

session_factory = sessionmaker(bind=scoped_engine)
dbsession       = scoped_session(session_factory)
