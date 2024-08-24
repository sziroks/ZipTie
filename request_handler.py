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
        """
        Creates a new entry in the database based on the provided parameters.

        Parameters:
        params (Union[BookModel, UserModel]): The parameters to create the entry.
            If it's an instance of UserModel, a new User entry will be created.
            If it's an instance of BookModel, a new Book entry will be created.

        Returns:
        None
        """
        if isinstance(params, UserModel):
            self.crud.create_entry(User, params.model_dump())
            return
        self.crud.create_entry(Book, params.model_dump())

    def get_books_and_users(self, page) -> list:
        """
        Retrieves a list of books and their corresponding users from the database.

        Parameters:
        page (int): The page number for pagination. Each page contains a specified number of records.

        Returns:
        list: A list of dictionaries, where each dictionary represents a book and its associated user.
            The dictionary has the following structure:
            {
                'book_id': int,
                'book_title': str,
                'user_id': int,
                'user_name': str
            }
        """
        return self.crud.select_joined(page)
