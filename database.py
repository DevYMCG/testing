from typing import Generator
from config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHELMY_DATABASE_URL= setting.DATABASE_URL

engine = create_engine(SQLALCHELMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency Injection
def get_db()->Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
