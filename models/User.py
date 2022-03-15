from sqlalchemy import Table, Column, Integer, ForeignKey

from models.models import Base

User = Table('user',
             Base.metadata,
             Column('pk', Integer(), primary_key=True),
             Column('author_id', ForeignKey('author.pk'), unique=True))
