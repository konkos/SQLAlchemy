from contextlib import contextmanager

from config import crud
from config.crud import Session
from models.models import Author, Post, Category


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


if __name__ == '__main__':
    # restart_db()
    pass

