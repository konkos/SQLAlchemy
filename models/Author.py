from sqlalchemy import Column, Integer, String

from models.models import Base


class Author(Base):
    __tablename__ = "author"

    pk = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Author< ID = {self.pk}, NAME = {self.name}>"
