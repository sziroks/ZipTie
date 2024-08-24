from db import DBConnector
from crud_handler import CrudHandler
from typing import Union
from api_models import BookModel, UserModel
from models.books import Book
from models.users import User


class RequestHandler:
    def __init__(self) -> None:
        self.db: DBConnector = DBConnector()
        self.crud: CrudHandler = CrudHandler(self.db.get_session())

    def create_entry(self, params: Union[BookModel, UserModel]) -> None:
        if isinstance(params, UserModel):
            self.crud.create_entry(User, params.model_dump())
            return
        self.crud.create_entry(Book, params.model_dump())

    def get_books_and_users(self, page) -> list:
        return self.crud.select_joined(page)
