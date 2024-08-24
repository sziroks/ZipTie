from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from typing import List

from api_models import UserModel, BookModel, BooksAndUsers, ResponseBooksAndUsers
from request_handler import RequestHandler


class Router:
    def __init__(self) -> None:
        """
        Initialize the Router class.

        This class is responsible for defining and handling API routes. It initializes an APIRouter instance,
        a RequestHandler instance, and adds routes to the router.

        Parameters:
        None

        Returns:
        None
        """
        self.router = APIRouter()
        self.request_handler = RequestHandler()
        self.add_routes()

    def add_routes(self) -> None:
        """
        This function adds routes to the API router.

        The router includes three routes:
        1. POST /create-user: Creates a new user.
        2. POST /create-book: Creates a new book.
        3. GET /books-and-users: Retrieves a list of books and their owners.

        Parameters:
        self: The instance of the Router class.

        Returns:
        None
        """

        @self.router.post("/create-user")
        async def create_user(user: UserModel) -> Response:
            """
            Creates a new user.

            Parameters:
            user (UserModel): The user data to be created.

            Returns:
            Response: A response indicating the success or failure of the operation.
            """
            try:
                self.request_handler.create_entry(user)
                return Response(content="Created", status_code=201)
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)

        @self.router.post("/create-book")
        async def create_book(book: BookModel) -> Response:
            """
            Creates a new book.

            Parameters:
            book (BookModel): The book data to be created.

            Returns:
            Response: A response indicating the success or failure of the operation.
            If the user ID does not exist, a 400 status code is returned.
            """
            try:
                self.request_handler.create_entry(book)
                return Response(content="Created", status_code=201)
            except IntegrityError as e:
                self.request_handler.crud.session.rollback()
                return Response(
                    content=f"User ID: {book.id_user} does not exist", status_code=400
                )
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)

        @self.router.get("/books-and-users")
        async def get_books_and_users(page: BooksAndUsers):
            """
            Retrieves a list of books and their owners.

            Parameters:
            page (BooksAndUsers): The page number for pagination.

            Returns:
            JSONResponse: A JSON response containing the list of books and their owners.
            If an error occurs, a 500 status code is returned.
            """
            try:
                content: list = self.request_handler.get_books_and_users(page.page)
                response = await self.parse_response(content)
                return JSONResponse(content=response, status_code=200)
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)

    @staticmethod
    async def parse_response(content: list) -> List[dict]:
        """
        Parses the content and returns a list of dictionaries representing books and their owners.

        This function takes a list of BookModel instances as input, extracts relevant information,
        and constructs a list of dictionaries. Each dictionary contains the book's ID, title, description,
        user ID, owner's name, email, and age.

        Parameters:
        content (list): A list of BookModel instances representing books and their owners.

        Returns:
        List[dict]: A list of dictionaries, where each dictionary represents a book and its owner.
        Each dictionary has the following keys: 'id_book', 'title', 'description', 'id_user', 'name',
        'email', and 'age'.
        """
        response_list: List[ResponseBooksAndUsers] = [
            ResponseBooksAndUsers(
                id_book=book.id_book,
                title=book.title,
                description=book.description,
                id_user=book.id_user,
                name=book.owner.name,
                email=book.owner.email,
                age=book.owner.age,
            )
            for book in content
        ]
        return [item.model_dump() for item in response_list]
