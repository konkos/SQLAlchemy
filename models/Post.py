from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from .Like import like
from models.models import Base


class Post(Base):
    __tablename__ = "post"

    pk = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)

    category_id = Column(Integer, ForeignKey('category.pk', ondelete='SET NULL'))
    author_id = Column(Integer, ForeignKey('author.pk', ondelete='CASCADE'))

    category = relationship('Category', uselist=False, backref=backref('posts'))
    author = relationship('Author', uselist=False, backref=backref('posts'))
    
    liked_by = relationship('User',
                          secondary=like,
                          primaryjoin='User.id == like.c.user_id',
                          secondaryjoin='Post.id == like.c.post_id',
                          backref=backref('liked_posts'))

    # liked_by = relationship('Like', backref=backref('posts'))

    def __repr__(self):
        return f"Post< ID = {self.pk}, TITLE = {self.title}," \
               f" CONTENT = {self.content}, CATEGORY = {self.category_id}," \
               f" AUTHOR = {self.author_id}>"
