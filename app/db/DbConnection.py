import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')

engine = create_engine(DEV_DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
base = declarative_base()

def get_session():
	db_session = session()

	try:
		yield db_session
	finally:
		db_session.close()
