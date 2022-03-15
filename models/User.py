from sqlalchemy import Table, Column, Integer, ForeignKey

from models.models import Base

user_table = Table('user',
                   Base.metadata,
                   Column('pk', Integer(), primary_key=True),
                   Column('author_id', ForeignKey('author.pk'), unique=True))


class User(Base):
    __table__ = user_table

    def __repr__(self):
        return f"PK:{self.pk}, AuthorID:{self.author_id}"
