from fastapi import FastAPI
from router import Router
import uvicorn


class Server:
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.router: Router = Router()
        self.app.include_router(self.router.router)

    def start_server(self) -> None:
        uvicorn.run(self.app)
