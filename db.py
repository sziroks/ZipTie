from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import sessionmaker as session
from sqlalchemy.orm.decl_api import DeclarativeMeta
import os
from typing import List
from consts import (
    DB_HOST,
    DB_NAME,
    DB_URL_PREFIX,
    ENV_DB_USER,
    ENV_DB_PASS,
)
from singleton_meta import SingletonMeta


class DBConnector(metaclass=SingletonMeta):
    Base: DeclarativeMeta = declarative_base()

    def __init__(self) -> None:
        self.engine: Engine = create_engine(self.build_db_url(), echo=True)
        self.SessionLocal: session = sessionmaker(
            autoflush=False, autocommit=False, bind=self.engine
        )

    def get_session(self) -> session:
        return self.SessionLocal()

    def build_db_url(self) -> str:
        self.check_env_variables([ENV_DB_USER, ENV_DB_PASS])
        return f"{DB_URL_PREFIX}{os.environ.get(ENV_DB_USER)}:{os.environ.get(ENV_DB_PASS)}@{DB_HOST}/{DB_NAME}"
    
    @staticmethod
    def check_env_variables(env_variables: List[str]):
        for env_var in env_variables:
            if not os.environ.get(env_var):
                raise ValueError(f"Missing environment variable: {env_var}")

