from config import crud
from config.crud import Session
from models.models import Author, Post, Category


def restart_db():
    crud.recreate_database()

    authors = []
    posts = []
    categories = []

    for i in range(10):
        authors.append(Author(name=f"author {i}"))
        posts.append(Post(title=f"title {i}", content=f"content {i}"))
        categories.append(Category(name=f"category {i}"))

    with Session.begin() as session:
        session.add_all(authors)
        session.add_all(posts)
        session.add_all(categories)
        session.commit()

    with Session.begin() as session:
        currCat = session.query(Category).first()
        currPost = session.query(Post).first()
        currAuthor = session.query(Author).first()

        print(currPost)
        print(currCat)
        print(currAuthor)

        currPost.category_id = session.query(Category).first().pk
        currPost.author_id = session.query(Author).first().pk

        print(currPost)

        session.add(currPost)
        session.commit()


if __name__ == '__main__':
    restart_db()
    # with Session.begin() as session:
    #     p = session.query(Post).join(Category).filter(Post.pk == 1).first()
    #     print(p.category_id)
# LEFT OFF HERE
# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
