from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configuration import parameters

database_host = parameters['database']['host']
database_username = parameters['database']['username']
database_password = parameters['database']['password']
database_name = parameters['database']['name']

engine = create_engine(f'postgresql://{database_username}:{database_password}@{database_host}/{database_name}')
session_maker = sessionmaker(bind=engine)
session = session_maker()
Base = declarative_base()
