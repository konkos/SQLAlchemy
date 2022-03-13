from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = "author"

    pk = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Author< ID = {self.id}, NAME = {self.name}>"


class Post(Base):
    __tablename__ = "post"

    pk = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)

    category_id = Column(Integer, ForeignKey('category.pk'))
    author_id = Column(Integer, ForeignKey('author.pk'))

    def __repr__(self):
        return f"Post< ID = {self.id}, TITLE = {self.title}, CONTENT = {self.content}, CATEGORY = {self.category_id}>"


class Category(Base):
    __tablename__ = "category"

    pk = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


    def __repr__(self):
        return f"Category< ID = {self.id}, NAME = {self.name}, Posts = {self.posts}>"
