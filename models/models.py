from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Author(Base):
    __tablename__ = "Authors"
    id = Column(Integer, primary_key=True)


class Post(Base):
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True)


class Category(Base):
    __tablename__ = "Category"
    id = Column(Integer, primary_key=True)

