from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import sessionmaker as session
from typing import Union

from models.books import Book
from models.users import User
from consts import TABLE_COLUMNS


class CrudHandler:
    def __init__(self, session: session) -> None:
        self.session: session = session

    def insert(self, model: Union[Book, User], params: dict):
        model_name = model().stringify()
        if model_name not in TABLE_COLUMNS:
            raise ValueError(f"Invalid model name {model_name}")

        if not all(key in TABLE_COLUMNS[model_name] for key in params):
            raise ValueError(
                f"Invalid parameters for table {model_name}. Expected: {TABLE_COLUMNS[model_name]}, got: {params.keys()}"
            )

        new_row = model(**params)
        self.session.add(new_row)
        self.session.commit()

    def select_joined(self):
        books_and_users = self.session.query(Book).options(joinedload(Book.owner)).all()
        return books_and_users


from db import DBConnector
from models.books import Book
from models.users import User

db = DBConnector()
print(db.build_db_url())
ch = CrudHandler(db.get_session())

new_user = {
    "name": "Tomek",
    "email": "test2@test.com",
    "age": 27,
}
new_book = {
    "title": "Test Book13",
    "description": "This is a test book 13.",
    "id_user": 4,
}
ch.insert(Book, new_book)
