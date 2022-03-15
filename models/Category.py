from sqlalchemy import Column, Integer, String

from models.models import Base


class Category(Base):
    __tablename__ = "category"

    pk = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f"Category< ID = {self.pk}, NAME = {self.name}>"
