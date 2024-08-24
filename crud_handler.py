from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import sessionmaker as session
from typing import Union

from models.books import Book
from models.users import User
from consts import TABLE_COLUMNS, ROWS_PER_PAGE


class CrudHandler:
    def __init__(self, session: session) -> None:
        self.session: session = session  # type: ignore

    def create_entry(self, model: Union[Book, User], params: dict) -> None:
        """
        This function creates a new entry in the database based on the given model and parameters.

        Parameters:
        - model (Union[Book, User]): The model class representing the database table.
        - params (dict): A dictionary containing the column names and their corresponding values for the new entry.

        Returns:
        - None: The function does not return any value. It adds the new entry to the database and commits the changes.

        Raises:
        - ValueError: If the model name is invalid or if the parameters do not match the expected columns for the given model.
        """
        model_name: str = model().stringify()

        # I know that this is not the perfect solution for checking the model and its columns.
        # It might even not be necessary, as pydantic takes care of model validation.
        # Better safe than sorry, right?
        if model_name not in TABLE_COLUMNS:
            raise ValueError(f"Invalid model name {model_name}")

        if not all(key in TABLE_COLUMNS[model_name] for key in params):
            raise ValueError(
                f"Invalid parameters for table {model_name}. Expected: {TABLE_COLUMNS[model_name]}, got: {params.keys()}"
            )

        new_row: Union[Book, User] = model(**params)
        self.session.add(new_row)
        self.session.commit()

    def select_joined(self, page: int) -> list:
        """
        This function retrieves a list of books with their corresponding owners, using pagination.

        Parameters:
        - page (int): The page number to retrieve. The first page is represented by 1.

        Returns:
        - list: A list of Book objects, each with its owner loaded. The list is limited to ROWS_PER_PAGE entries.

        The function calculates the offset based on the provided page number and the number of rows per page.
        It then uses SQLAlchemy's query, joinedload, offset, and limit methods to fetch the desired data.
        """
        offset: int = (page - 1) * ROWS_PER_PAGE
        return (
            self.session.query(Book)
            .options(joinedload(Book.owner))
            .offset(offset)
            .limit(ROWS_PER_PAGE)
            .all()
        )
