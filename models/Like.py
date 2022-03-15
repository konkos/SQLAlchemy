from sqlalchemy import Table, Column, Integer, ForeignKey

from models.models import Base

Like = Table('like',
             Base.metadata,
             Column('pk', Integer(), primary_key=True),
             Column('user_id', ForeignKey('user.pk', ondelete='CASCADE'), index=True),
             Column('post_id', ForeignKey('post.pk', ondelete='CASCADE'), index=True))
