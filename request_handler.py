from db import DBConnector
from crud_handler import CrudHandler
from typing import Union
from api_models import BookModel, UserModel
from models.books import Book
from models.users import User

class RequestHandler:
    def __init__(self) -> None:
        self.db = DBConnector()
        self.crud = CrudHandler(self.db.get_session())

    def create_entry(self, params: Union[BookModel, UserModel]) -> bool:
        if isinstance(params, UserModel):
            return self.crud.insert(User, params.model_dump())
        return self.crud.insert(Book, params.model_dump())
    
    def get_books_and_users(self) -> bool:
        return self.crud.select_joined()
