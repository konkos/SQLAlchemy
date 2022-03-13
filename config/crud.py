from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import DATABASE_URI
from models.models import Base

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
