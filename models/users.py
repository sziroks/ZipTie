from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import DBConnector


class User(DBConnector.Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    email = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)

    books = relationship("Book", back_populates="owner")

    def __repr__(self):
        return f"User({self.id_user}, {self.name}, {self.email}, {self.age})"

    def stringify(self):
        return "User"