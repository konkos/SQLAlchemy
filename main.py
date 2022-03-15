import random
from contextlib import contextmanager

from config import crud
from config.crud import Session
from models.models import Author, Post, Category, User, Like


@contextmanager
def db():
    session = Session()

    yield session

    session.close()


def restart_db():
    crud.recreate_database()

    posts = []

    with db() as session:
        for i in range(10):
            author = Author(name=f'author {i}')
            category = Category(name=f'category {i}')
            post = Post(title=f'title {i}', content=f'content {i}', author=author, category=category)

            posts.append(post)

        session.add_all(posts)

        session.commit()

    # add users
    with db() as session:
        for author in session.query(Author).all():
            session.execute(User.insert(), {'author_id': author.pk})
            session.commit()

    # add likes
    with db() as session:
        users = session.query(User).all()
        posts = session.query(Post).all()

        for post in posts:
            random_author = users[random.randint(0, len(users)-1)]
            session.execute(Like.insert(), {'user_id': random_author.pk, 'post_id': post.pk})
        session.commit()


if __name__ == '__main__':
    restart_db()

    pass
