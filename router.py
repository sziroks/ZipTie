from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from typing import List

from api_models import UserModel, BookModel, BooksAndUsers, ResponseBooksAndUsers
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
        async def get_books_and_users(page: BooksAndUsers):
            try:
                content = self.request_handler.get_books_and_users(page.page)
                response = await self.parse_response(content)
                return JSONResponse(content=response, status_code=200)
            except Exception as e:
                self.request_handler.crud.session.rollback()
                return Response(content=f"Internal Server Error: {e}", status_code=500)

    @staticmethod
    async def parse_response(content) -> List[ResponseBooksAndUsers]:
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
