from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.models import Base


class Author(Base):
    __tablename__ = "author"

    pk = Column(Integer, primary_key=True)
    name = Column(String)

    # user_id = Column(Integer, ForeignKey('user.pk'))
    user = relationship('User', uselist=False, backref=backref('authors'))

    def __repr__(self):
        return f"Author< ID = {self.pk}, NAME = {self.name}>"
