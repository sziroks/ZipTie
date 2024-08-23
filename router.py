from fastapi import APIRouter, Response
from sqlalchemy.exc import IntegrityError

from api_models import UserModel, BookModel
from request_handler import RequestHandler


class Router:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.request_handler = RequestHandler()
        self.add_routes()

    def add_routes(self):

        @self.router.post("/create-user")
        async def create_user(user: UserModel):
            try:
                self.request_handler.create_entry(user)
                return Response(content="Created", status_code=201)
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)

        @self.router.post("/create-book")
        async def create_book(book: BookModel):
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
        async def get_books_and_users():
            try:
                content = self.request_handler.get_books_and_users()
                return Response(content=content, status_code=200)
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)
